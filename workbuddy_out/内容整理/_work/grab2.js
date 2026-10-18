// 按 DOM 顺序输出「段落 / 图片」序列，用于精确还原图文排版
const fs = require('fs');
const { chromium } = require('playwright-core');

const CHROME = 'C:\\Users\\zifeng\\.agent-browser\\browsers\\chrome-155.0.8059.84\\chrome.exe';
const URL = 'https://zhuanlan.zhihu.com/p/2075617575262762743';
const OUT = 'G:\\AI_IDE_output\\workbuddy_out\\内容整理\\_work\\raw\\zhihu_blocks.json';

(async () => {
  const browser = await chromium.launch({ executablePath: CHROME, headless: true, args: ['--no-sandbox'] });
  const ctx = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36',
    viewport: { width: 1440, height: 900 },
    locale: 'zh-CN',
  });
  const page = await ctx.newPage();
  await page.goto(URL, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(6000);
  try { await page.waitForSelector('.Post-RichText', { timeout: 30000 }); } catch (e) { console.log('  fallback: no .Post-RichText'); }
  for (let i = 0; i < 14; i++) {
    await page.evaluate(() => window.scrollBy(0, window.innerHeight));
    await page.waitForTimeout(350);
  }
  await page.waitForTimeout(800);

  const blocks = await page.evaluate(() => {
    const root = document.querySelector('.Post-RichText') || document.querySelector('article') || document.querySelector('.RichText') || document.body;
    const out = [];
    let imgIdx = 0;
    const walk = (node) => {
      node.childNodes.forEach((ch) => {
        if (ch.nodeType === 1) {
          const tag = ch.tagName.toLowerCase();
          if (tag === 'img') {
            imgIdx += 1;
            out.push({
              type: 'img',
              idx: imgIdx,
              src: ch.getAttribute('data-original') || ch.getAttribute('data-actualsrc') || ch.getAttribute('data-src') || ch.src,
            });
          } else if (tag === 'figure') {
            const im = ch.querySelector('img');
            if (im) {
              imgIdx += 1;
              out.push({
                type: 'img',
                idx: imgIdx,
                src: im.getAttribute('data-original') || im.getAttribute('data-actualsrc') || im.getAttribute('data-src') || im.src,
                caption: (ch.querySelector('figcaption') || {}).innerText || '',
              });
            }
          } else if (/^(p|h1|h2|h3|h4|blockquote|li|pre)$/.test(tag)) {
            const t = ch.innerText.trim();
            if (t) out.push({ type: tag === 'p' ? 'p' : 'h', tag, text: t });
          } else {
            walk(ch);
          }
        }
      });
    };
    walk(root);
    return out;
  });

  fs.writeFileSync(OUT, JSON.stringify(blocks, null, 1), 'utf8');
  console.log('blocks=' + blocks.length + ' imgs=' + blocks.filter((b) => b.type === 'img').length);
  await browser.close();
})();
