const puppeteer = require('puppeteer');

function protoCheck(url){
    try {
        (async () => {
            const browser = await puppeteer.launch();
            const page = await browser.newPage();
            try {
                await page.goto(url);
            } catch (error) {
                console.log(error);
                process.exit(1);
            }
            try {
                const result = await page.evaluate(_ => {
                    return Promise.resolve(prototype);
                })
                console.log("[+] " + url + " appears to be vulnerabile!")
                } catch (error) {
                    console.log(error);
                    process.exit(1);
            }
            try {
                await browser.close();
            } catch (error) {
                console.log(error);
                process.exit(1);
            }
        })();
    } catch (error) {
        console.log(error);
        process.exit(1);
    } 
}

function getUrl(url){
    try {
        (async () => {
            const browser = await puppeteer.launch();
            const page = await browser.newPage();
            try {
                await page.goto(url);
            } catch (error) {
                console.log(error);
                process.exit(1);
            }
            try {
                const final_url = await page.evaluateHandle(() => window.location.href);
                console.log(final_url._remoteObject.value);
            } catch (error) {
                console.log(error);
                process.exit(1);
            }

            try {
                await browser.close();
            } catch (error) {
                console.log(error);
                process.exit(1);
            }
        })();
    } catch (error) {
        console.log(error);
        process.exit(1);
    }
}

if (process.argv[3]){
    getUrl(process.argv[2]);
} else {
    protoCheck(process.argv[2]);
}