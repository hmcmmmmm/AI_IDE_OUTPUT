# -*- coding: utf-8 -*-
"""Clean YouTube auto-generated VTT into readable transcript."""
import re, sys, json

def ts_to_sec(t):
    h, m, s = t.split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)

def clean_vtt(path):
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    blocks = re.split(r'\n\s*\n', raw)
    cues = []
    for b in blocks:
        lines = [l for l in b.split('\n') if l.strip()]
        tl = None
        for i, l in enumerate(lines):
            if '-->' in l:
                tl = l.split('-->')[0].strip()
                body = lines[i+1:]
                break
        if not tl:
            continue
        text_lines = [re.sub(r'<[^>]+>', '', l).strip() for l in body]
        text_lines = [t for t in text_lines if t]
        if not text_lines:
            continue
        # last line is the newest rolling line
        cues.append((ts_to_sec(tl), text_lines[-1]))

    # dedupe rolling repeats
    out = []
    for t, txt in cues:
        txt = re.sub(r'\s+', ' ', txt).strip()
        if not txt:
            continue
        if out and (txt == out[-1][1] or out[-1][1].endswith(txt)):
            continue
        if out and txt.startswith(out[-1][1]) and len(txt) - len(out[-1][1]) < 60:
            out[-1] = (out[-1][0], txt)
            continue
        out.append((t, txt))
    return out

def to_paragraphs(cues, gap=6.0, maxlen=900):
    paras, cur, start = [], [], None
    last_t = None
    for t, txt in cues:
        if start is None:
            start = t
        if last_t is not None and (t - last_t > gap or sum(len(x) for x in cur) > maxlen):
            paras.append((start, ' '.join(cur)))
            cur, start = [], t
        cur.append(txt)
        last_t = t
    if cur:
        paras.append((start, ' '.join(cur)))
    return paras

def fmt(t):
    m, s = divmod(int(t), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"

if __name__ == '__main__':
    src = sys.argv[1]
    cues = clean_vtt(src)
    paras = to_paragraphs(cues)
    words = sum(len(p[1].split()) for p in paras)
    with open('transcript_plain.txt', 'w', encoding='utf-8') as f:
        for t, p in paras:
            f.write(f'[{fmt(t)}] {p}\n\n')
    print(f'cues={len(cues)} paras={len(paras)} words={words}')
    for t, p in paras[:6]:
        print(f'[{fmt(t)}] {p[:200]}')
