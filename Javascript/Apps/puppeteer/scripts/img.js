const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('http://google.com');
  await page.screenshot({path: 'output/google.png'});

  await browser.close();
})();
