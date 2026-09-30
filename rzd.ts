import { chromium, Page, Locator } from "playwright";

async function rzd_tickets() {

    const browser = await chromium.launch({ headless: false });
    const context = await browser.newContext();
    const page = await context.newPage();

    try {

        await page.goto("https://ticket.rzd.ru/main", { waitUntil:"networkidle" });

        await page.waitForSelector(
            '[data-testid="route-search-from-node-field"] input[role="combobox"]', 
            { timeout: 15000 }
        );

        const fromfield = page.locator(
            '[data-testid="route-search-from-node-field"] input[role="combobox"]'
        );
        await fromfield.fill('Ростов-на-Дону');

        await page.waitForTimeout(500);

        const tofield = page.locator(
            '[data-testid="route-search-to-node-field"] input[role="combobox"]'
        );

        await tofield.fill("Санкт-Петербург");
        
        await page.waitForTimeout(500);

    }

    finally {
        console.log("Тест завершен!");
        await browser.close();
    }

}

rzd_tickets();