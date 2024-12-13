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

        for data in flipData.css('div[class="tUxRFH"]'):
            lapTitle = data.css_first('div[class="KzDlHZ"]').text()
            lapImg = {'imgAlt':data.css_first('img[class="DByuf4"]').attrs['alt'],
                      'imgSrc': data.css_first('img[class="DByuf4"]').attrs['src']}
            lapPrice = data.css_first('div[class="Nx9bqj _4b5DiR"]').text()
            lapSpec = data.css_first('ul[class="G4BRas"]').text()
            lapRatRev = data.css_first('div[class="_5OesEi"]').text()

        
            print(  )
            print()
        