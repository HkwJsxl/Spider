import requests
import csv
import time

f = open('detailInfo.csv', mode='w', encoding='utf_8_sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '店铺名称',
    '店铺类别',
    '店铺区名',
    '人均售价',
    '店铺评分',
    '评论条数',
    '详情页',
])
csv_writer.writeheader()  # 写入表头
num = 1
for page in range(0, 321, 32):
    print(f'正在爬取{num}页数据'.center(50, '-'))
    time.sleep(2)
    url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/123'
    headers = {
        'Referer': 'https://hd.meituan.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    }
    data = {
        'uuid': '5a8e65b518cf447c812f.1642238855.1.0.0',
        'userid': '3549015582',
        'limit': '32',
        'offset': f'{page}',
        'cateId': '-1',
        'q': '烤肉',
        'token': 'l0cHfarV7eF4Cp28EW1rt3fjJIQAAAAA9A8AAP0Noy-T-rjGwM-9wm9YK5BeqrQFxdbTLqLcYnsmJyiU5sCoLaZQ2zvt3jPH0kCTjQ',
    }
    proxies = {
        # 'http': 'http://183.173.116.203:10080', 'https': 'http://183.173.116.203:10080',
        # 'http': 'http://140.249.73.79:26421', 'https': 'http://140.249.73.79:26421'
        'http': 'http://1.14.122.251:1080', 'https': 'http://1.14.122.251:1080'
    }
    html_data = requests.get(url=url, headers=headers, params=data, proxies=proxies).json()
    searchResult = html_data['data']['searchResult']
    for info_data in searchResult:
        deals = info_data['deals']
        info_searchResult = {
            '店铺名称': info_data['title'],
            '店铺类别': info_data['backCateName'],
            '店铺区名': info_data['areaname'],
            '人均售价': info_data['avgprice'],
            '店铺评分': info_data['avgscore'],
            '评论条数': info_data['comments'],
            '详情页': f'https://www.meituan.com/meishi/{info_data["id"]}/',
        }

        # i = 1
        # for info_data in deals:
        #     info_searchResult[f'店铺优惠{i}'] = info_data['title']
        #     i += 1

        csv_writer.writerow(info_searchResult)
        print(info_searchResult)
    num += 1
