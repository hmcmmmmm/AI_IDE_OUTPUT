const { chromium } = require('playwright-core');
(async () => {
  const b = await chromium.launch({
    executablePath: 'C:\\Users\\zifeng\\.agent-browser\\browsers\\chrome-155.0.8059.84\\chrome.exe',
    headless: true,
  });
  const p = await b.newPage({ viewport: { width: 1440, height: 1000 }, deviceScaleFactor: 1 });
  await p.goto('file:///G:/AI_IDE_output/workbuddy_out/%E5%86%85%E5%AE%B9%E6%95%B4%E7%90%86/HotChips2026/06_%E6%B7%B1%E5%BA%A6%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A/HotChips2026_%E6%B7%B1%E5%BA%A6%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A.html', { waitUntil: 'load' });
  await p.waitForTimeout(1500);
  await p.screenshot({ path: 'G:/AI_IDE_output/workbuddy_out/内容整理/HotChips2026/_work/shot_top.png' });
  // 滚动到第一个 figure
  await p.evaluate(() => document.querySelector('figure').scrollIntoView());
  await p.waitForTimeout(1200);
  await p.screenshot({ path: 'G:/AI_IDE_output/workbuddy_out/内容整理/HotChips2026/_work/shot_fig.png' });
  // 表格区
  await p.evaluate(() => document.querySelectorAll('table')[1].scrollIntoView());
  await p.waitForTimeout(800);
  await p.screenshot({ path: 'G:/AI_IDE_output/workbuddy_out/内容整理/HotChips2026/_work/shot_tbl.png' });
  const info = await p.evaluate(() => ({
    h: document.body.scrollHeight,
    figs: document.querySelectorAll('figure').length,
    broken: Array.from(document.images).filter(i => !i.complete || i.naturalWidth === 0).length,
    tables: document.querySelectorAll('table').length,
  }));
  console.log(JSON.stringify(info));
  await b.close();
})();
