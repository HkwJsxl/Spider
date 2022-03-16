import requests
from lxml import etree
import csv

url = "https://quotes.toscrape.com/"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

res = requests.get(url, headers=headers).text
html = etree.HTML(res)
queto_list = html.xpath('//div[@class="col-md-8"]')
lists = []
for queto in queto_list:
    # 名言正文
    title = queto.xpath('./div[@class="quote"]/span[1]/text()')
    # 作者
    authuor = queto.xpath('./div[@class="quote"]/span[2]/small/text()')
    # 名言标签
    tags = queto.xpath('./div[@class="quote"]/div[@class="tags"]/a[@class="tag"]/text()')
    # 将数据统一添加进列表中保存
    lists.append(title)
    lists.append(authuor)
    lists.append(tags)

    with open("./名人名言.csv", 'w', encoding='utf-8-sig', newline='\n') as f:
        writer = csv.writer(f)
        for i in lists:
            writer.writerow(i)
