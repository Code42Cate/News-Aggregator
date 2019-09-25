const puppeteer = require('puppeteer');
const assert = require('assert');

(async () => {
  const browser = await puppeteer.launch({
    headless: false
  });
  const page = await browser.newPage();
  await page.goto('http://localhost:5000');

  assert.strictEqual(await page.evaluate(() => {
    console.log(document.getElementById('pagination').style.visibility);
    return window.getComputedStyle(document.getElementById('pagination'), null).visibility === 'hidden';
  }), true, 'PAGINATION VISIBLE BEFORE ARTICLES GOT LOADED');

  await page.waitForResponse((response) => response.url() === 'http://localhost:5000/api/v1/articles/20');
  
  assert.strictEqual(await page.evaluate(() => {
    return document.getElementById('pagination').style.visibility === 'visible';
  }), true, 'PAGINATION VISIBLE BEFORE ARTICLES GOT LOADED');


  assert.strictEqual(await page.evaluate(() => {
    return document.getElementById('articletable').rows.length === 20;
  }), true, 'NOT ENOUGH TABLE ROWS');

  assert.strictEqual(await page.evaluate(() => {
    return document.getElementById('addlabel') !== undefined; 
  }), true, 'ADD LABEL BUTTON NOT FOUND');


  console.log('OK');
  await browser.close();

})();