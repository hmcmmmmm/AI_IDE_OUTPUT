// 抓取雪球文章正文块与图片
const fs = require('fs');
const { chromium } = require('playwright-core');
const CHROME = 'C:\\Users\\zifeng\\.agent-browser\\browsers\\chrome-155.0.8059.84\\chrome.exe';
const OUT = 'G:\\AI_IDE_output\\workbuddy_out\\内容整理\\_work\\raw\\xueqiu.json';

(async () => {
  const browser = await chromium.launch({ executablePath: CHROME, headless: true, args: ['--no-sandbox'] });
  const ctx = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36',
    viewport: { width: 1440, height: 900 },
    locale: 'zh-CN',
  });
  const page = await ctx.newPage();
  await page.goto('https://xueqiu.com/8353820992/406787553', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(6000);
  for (let i = 0; i < 10; i++) { await page.evaluate(() => window.scrollBy(0, window.innerHeight)); await page.waitForTimeout(350); }
  await page.waitForTimeout(600);
  const data = await page.evaluate(() => {
    const root = document.querySelector('.article__bd__detail') || document.querySelector('article') || document.body;
    const imgs = [...root.querySelectorAll('img')].map((im, i) => ({ i: i + 1, src: im.src, w: im.naturalWidth, h: im.naturalHeight }));
    return { title: document.title, text: root.innerText, imgs };
  });
  fs.writeFileSync(OUT, JSON.stringify(data, null, 1), 'utf8');
  console.log('title=' + data.title + ' len=' + data.text.length + ' imgs=' + data.imgs.length);
  data.imgs.forEach((x) => console.log('  ', x.i, x.w + 'x' + x.h, x.src));
  await browser.close();
})();
