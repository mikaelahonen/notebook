const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('http://google.com', {waitUntil: 'networkidle2'});
  await page.pdf({path: 'output/capture.pdf', format: 'A4'});

  await browser.close();
})();
