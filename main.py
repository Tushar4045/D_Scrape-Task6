import pandas as pd
from Utils.extractHtml import getHtml

flipUrl = 'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g'
if __name__ == '__main__':
    flipData = getHtml(websiteUrl=flipUrl, showbrowser=True,screenshotName='laptop')
    lapTitle = [t.text() for t in flipData.css('div[class="KzDlHZ"]')]
    lapPrice = [p.text().strip() for p in flipData.css('div[class="Nx9bqj _4b5DiR"]')]
    lapSpec = [s.text()for s in flipData.css('div[class="_6NESgJ"]')]
    lapRating = [r.text() for r in flipData.css('span[class="Y1HWO0"]')]
    lapData = {
           'Title':lapTitle,
           'Price':lapPrice,
           'Specifications': lapSpec,
           'Rating':lapRating
        }
    df = pd.DataFrame(lapData)
    lpDf = df.replace({r'[“”‘’]': '"'}, regex=True)

    lpDf.to_csv('laptop.csv')