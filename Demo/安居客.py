import requests
import parsel
import csv

f = open('安居客.csv', mode='w', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['详情页',
                                           '名称',
                                           '属性',
                                           '价格',
                                           '开盘',
                                           '交房',
                                           '户型',
                                           '地址',
                                           '地址详情页',
                                           '手机号', ])
csv_writer.writeheader()
for page in range(1, 3):
    print(f'正在爬取第{page}页'.center(50, '-'))
    url = f'https://hd.fang.anjuke.com/loupan/all/p{page}/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers).text
    selector = parsel.Selector(response)
    link_list = selector.css('.key-list.imglazyload > div > a.pic::attr("href")').getall()
    for link in link_list:
        html_data = requests.get(url=link, headers=headers).text
        parse_data = parsel.Selector(html_data)
        name = parse_data.css('.basic-fst h1::text').get()
        tags = ','.join(parse_data.css('.basic-parms-wrap > div > div > div.tags a::text').getall()).replace(' ', '')
        price = parse_data.css('div.basic-parms-wrap > dl > dd.price > p > em::text').get()
        start = parse_data.css('.basic-parms-wrap > dl > dd:nth-child(4) > span::text').get()
        admit = parse_data.css('.basic-parms-wrap > dl > dd:nth-child(6) > span::text').get()
        types = parse_data.css('.basic-parms-wrap > dl > dd.ajust > div > a::text').get()
        address = parse_data.css(
            '.basic-parms-wrap > dl > dd.last-line.g-overflow > a.lpAddr-text.g-overflow::text').get().strip()
        address_link = parse_data.css(
            '.basic-parms-wrap > dl > dd.last-line.g-overflow > a.lpAddr-text.g-overflow::attr("href")').getall()[0]
        phone = parse_data.css('#phone_show_soj > p > strong::text').get()
        data_dict = {
            '详情页': link,
            '名称': name,
            '属性': tags,
            '价格': price,
            '开盘': start,
            '交房': admit,
            '户型': types,
            '地址': address,
            '地址详情页': address_link,
            '手机号': phone,
        }
        csv_writer.writerow(data_dict)
        print(data_dict)
