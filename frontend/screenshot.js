import { chromium } from 'playwright';

(async () => {
    const browser = await chromium.launch();
    const page = await browser.newPage();

    await page.setViewportSize({ width: 1280, height: 720 });

    console.log('Taking screenshot of Home');
    await page.goto('http://localhost:5173/');
    await page.waitForTimeout(2000);
    await page.screenshot({ path: '../static/img/screenshot_home.png' });

    console.log('Taking screenshot of Locations');
    await page.goto('http://localhost:5173/locations');
    await page.waitForTimeout(4000); // map might take longer
    await page.screenshot({ path: '../static/img/screenshot_locations.png' });

    console.log('Taking screenshot of Rewards');
    await page.goto('http://localhost:5173/rewards');
    await page.waitForTimeout(2000);
    await page.screenshot({ path: '../static/img/screenshot_rewards.png' });

    console.log('Taking screenshot of Sorting');
    await page.goto('http://localhost:8000/sorting/');
    await page.waitForTimeout(2000);
    await page.screenshot({ path: '../static/img/screenshot_sorting.png' });

    console.log('Taking screenshot of Challenges');
    await page.goto('http://localhost:8000/challenges/');
    await page.waitForTimeout(2000);
    await page.screenshot({ path: '../static/img/screenshot_challenges.png' });

    console.log('Done');
    await browser.close();
})();
