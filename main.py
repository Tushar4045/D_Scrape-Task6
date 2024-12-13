import pandas as pd
import re
from Utils.extractHtml import getHtml

flipUrl = 'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g'
if __name__ == '__main__':
    flipData = getHtml(websiteUrl=flipUrl,showbrowser=True,screenshotName='laptop')
    allLap =[]
    for data in flipData.css('div[class="tUxRFH"]'):
            lapTitle = data.css_first('div[class="KzDlHZ"]').text()
            imgAlt = data.css_first('img[class="DByuf4"]').attrs['alt']
            imgSrc = data.css_first('img[class="DByuf4"]').attrs['src']
            lapPrice = data.css_first('div[class="Nx9bqj _4b5DiR"]').text()
            lapSpec = data.css_first('ul[class="G4BRas"]').text()
            lapRateRev = data.css_first('div[class="_5OesEi"]').text()
            lapData = {
                'Title':lapTitle,
                'imgAlt':imgAlt,
                'immgSrc': imgSrc,
                'Price':lapPrice,
                'Specifications': lapSpec,
                'RateRev':lapRateRev
                }
            allLap.append(lapData)
    df = pd.DataFrame(allLap)
    lpDf = df.replace({r'[â‚¹Â]': '', r'(\S)&(\S)': r'\1 & \2' }, regex=True)


    lpDf.to_csv('laptop.csv', encoding='utf-8-sig', index=False)



