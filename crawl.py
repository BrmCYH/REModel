import requests
from bs4 import BeautifulSoup
pathlist = ['https://mp.weixin.qq.com/s/OU3ObJg4aea1yw6zWXq4KA']
for i in pathlist:
    infos = requests.get(i)
    soup = BeautifulSoup(infos.content, 'html.parser')
    spans = soup.find_all("span")
    for span in spans:
        x = span.get_text(strip=True, separator = 
                      ' ')
        print(x)


