// 用 playwright-core 驱动已安装的 Chrome，一次性抓取页面正文与图片 URL
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright-core');

const CHROME = 'C:\\Users\\zifeng\\.agent-browser\\browsers\\chrome-155.0.8059.84\\chrome.exe';
const OUTDIR = 'G:\\AI_IDE_output\\workbuddy_out\\内容整理\\_work\\raw';

const TARGETS = [
  { key: 'zhihu_mem', url: 'https://zhuanlan.zhihu.com/p/2075617575262762743' },
];

(async () => {
  const browser = await chromium.launch({
    executablePath: CHROME,
    headless: true,
    args: ['--disable-blink-features=AutomationControlled', '--no-sandbox'],
  });
  const ctx = await browser.newContext({
    userAgent:
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36',
    viewport: { width: 1440, height: 900 },
    locale: 'zh-CN',
  });
  await ctx.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });

  for (const t of TARGETS) {
    const page = await ctx.newPage();
    try {
      await page.goto(t.url, { waitUntil: 'domcontentloaded', timeout: 60000 });
      // 等正文出现（知乎反爬 JS 需要执行）
      await page.waitForTimeout(6000);
      try {
        await page.waitForSelector('.Post-RichText, article, .RichText', { timeout: 30000 });
      } catch (e) {
        console.log('  [warn] rich-text selector not found');
      }
      // 滚动到底触发懒加载图片
      for (let i = 0; i < 12; i++) {
        await page.evaluate(() => window.scrollBy(0, window.innerHeight));
        await page.waitForTimeout(400);
      }
      await page.evaluate(() => window.scrollTo(0, 0));
      await page.waitForTimeout(800);

      const data = await page.evaluate(() => {
        const root =
          document.querySelector('.Post-RichText') ||
          document.querySelector('article') ||
          document.querySelector('.RichText') ||
          document.body;
        const imgs = [...root.querySelectorAll('img')].map((im, i) => ({
          i: i + 1,
          src: im.getAttribute('data-original') || im.getAttribute('data-actualsrc') || im.getAttribute('data-src') || im.src,
          alt: im.alt || '',
          w: im.naturalWidth,
          h: im.naturalHeight,
        }));
        return {
          title: document.title,
          url: location.href,
          textLen: root.innerText.length,
          text: root.innerText,
          imgs,
        };
      });

      fs.writeFileSync(path.join(OUTDIR, t.key + '.json'), JSON.stringify(data, null, 1), 'utf8');
      console.log(`${t.key}: title="${data.title}" textLen=${data.textLen} imgs=${data.imgs.length}`);
      data.imgs.forEach((im) => console.log('   ', im.i, im.w + 'x' + im.h, im.src));
    } catch (e) {
      console.log(`${t.key} ERROR: ${e.message}`);
    }
    await page.close();
  }
  await browser.close();
})();
