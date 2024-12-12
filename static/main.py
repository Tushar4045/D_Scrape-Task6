from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
import pandas as pd

flipUrl = 'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g'

if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url=flipUrl)
        page.wait_for_load_state('networkidle')
        page.wait_for_load_state('domcontentloaded')
        page.wait_for_timeout(1000)
        page.screenshot(full_page=True,path='./flip.png')
        flipHtml = page.inner_html('body')
        flipData = HTMLParser(flipHtml)
        
        lapTitle = [t.text() for t in flipData.css('div[class="KzDlHZ"]')]
        lapPrice = [p.text().strip() for p in flipData.css('div[class="Nx9bqj _4b5DiR"]')]
        lapSpec = [s.text()for s in flipData.css('div[class="_6NESgJ"]')]
        lapRating = [r.text() for r in flipData.css('span[class="Y1HWO0"]')]
        # flipImg = {
        #     'imgAlt': [a.attributes.get('alt') for a in flipData.css('div [class="yPq5Io"]'). ]
        # }
        lapData = {
           'Title':lapTitle,
           'Price':lapPrice,
           'Specifications': lapSpec,
           'Rating':lapRating
        }
        df = pd.DataFrame(lapData)
        # df['Price'] = df['Price'].str.replace(r'[^\d₹.,]', '', regex=True)
        lpDf = df.replace({r'[“”‘’]': '"'}, regex=True)

        lpDf.to_csv('laptop.csv')