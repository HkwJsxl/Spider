import requests
import parsel
import csv

f = open('猫咪.csv', mode='w', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    'shop', 'title', 'price', 'promise', 'num', 'age', 'variety', 'prevention', 'read_num', 'phone', 'is_purebred',
    'page_url',
])
csv_writer.writeheader()
for page in range(1, 5):
    print(f'正在爬取第{page}页内容'.center(50, '-'))
    url = f'http://maomijiaoyi.com/index.php?/chanpinliebiao_c_2_{page}--24.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    }
    res = requests.get(url=url, headers=headers).text
    selector = parsel.Selector(res)
    href = selector.css('#content > div.breeds_floor > div > div > a::attr(href)').getall()
    for href_url in href:
        page_url = 'http://maomijiaoyi.com' + href_url
        response = requests.get(url=page_url, headers=headers).text
        selector = parsel.Selector(response)
        shop = selector.css(
            '#content > .center_1220.detail > .right > .dinming::text').get().strip()  # 店名
        title = selector.css(
            '#content > .center_1220.detail > .left.top > .detail_text > .title::text').get().strip()  # 标题
        price = selector.css(
            '#content > .center_1220.detail > .left.top > .detail_text > .info1 > div > .red.size_24::text').get()  # 价格
        promise = selector.css(
            '#content > .center_1220.detail > .left.top > .detail_text > .info1 > div:nth-child(2) > span::text').get().replace(
            '卖家承诺: ', '')  # 承诺
        num = selector.css(
            '#content > .center_1220.detail > .left.top > .detail_text > .info2 > div:nth-child(1) > .red::text').get()  # 在售只数
        age = selector.css(
            '#content > .center_1220.detail > .left.top > .detail_text > .info2 > :nth-child(2) > .red::text').get()  # 年龄
        variety = selector.css(
            '#content > .center_1220.detail > .left.top > .detail_text > .info2 > :nth-child(3) > .red::text').get()  # 品种
        prevention = selector.xpath(
            '//*[@id="content"]/div[3]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/span/text()').get().strip()  # 疫苗情况
        read_num = selector.css(
            '#content > .center_1220.detail > .left.top > .detail_text > .info1 > :nth-child(1) > :nth-child(4)::text').get()  # 浏览次数
        phone = selector.css(
            '#content > .center_1220.detail > .left.top > .detail_text > .user_info > :nth-child(2) > .c333::text').get()  # 联系电话
        is_purebred = selector.css(
            '#content > .center_1220.detail > .left.top > .gougou_info > .xinxi_neirong > div:nth-child(1) > .item_neirong > div:nth-child(1) > span::text').get().strip()  # 是否纯种
        dict_data = {
            'shop': shop,
            'title': title,
            'price': price,
            'promise': promise,
            'num': num,
            'age': age,
            'variety': variety,
            'prevention': prevention,
            'read_num': read_num,
            'phone': phone,
            'is_purebred': is_purebred,
            'page_url': page_url,
        }
        csv_writer.writerow(dict_data)
        print(dict_data)
