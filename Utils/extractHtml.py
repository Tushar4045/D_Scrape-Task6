from selectolax.parser import HTMLParser
from playwright.sync_api import sync_playwright

def getHtml(websiteUrl, showbrowser = True, screenshotName = ''):
    with sync_playwright() as p:
            browser = p.chromium.launch(headless= not showbrowser)
            page = browser.new_page()
            page.goto(url=websiteUrl)
            page.wait_for_load_state('networkidle')
            page.wait_for_load_state('domcontentloaded')
            page.wait_for_timeout(1000)
            page.screenshot(full_page=True,path=f'./{screenshotName}.png')
            pageHtml = page.inner_html('body')
            pageData = HTMLParser(pageHtml)
            return pageData