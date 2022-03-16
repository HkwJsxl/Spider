import csv
import time
import requests


def get_response(url, page):
    data = {
        # 'callback': 'getMerchandiseIds',
        'app_name': 'shop_pc',
        'app_version': '4.0',
        'warehouse': 'VIP_BJ',
        'fdc_area_id': '101103104',
        'client': 'pc',
        'mobile_platform': '1',
        'province_id': '101103',
        'api_key': '70f71280d5d547b2a7bb370a529aeea1',
        'user_id': '505534273',
        'mars_cid': '1646530621737_436d311042bf0e83b38ed94a0fe3a1d1',
        'wap_consumer': 'b',
        'standby_id': 'nature',
        'keyword': '口红',
        'lv3CatIds': '',
        'lv2CatIds': '',
        'lv1CatIds': '',
        'brandStoreSns': '',
        'props': '',
        'priceMin': '',
        'priceMax': '',
        'vipService': '',
        'sort': '0',
        'pageOffset': page,
        'channelId': '1',
        'gPlatform': 'PC',
        'batchSize': '120',
        '_': '1646530832970',
    }
    response = requests.get(url=url, headers=headers, params=data)
    return response


def parse_pid(json_data):
    products = json_data['data']['products']
    pid_list = [index['pid'] for index in products]
    return pid_list


def parse_data(pid_list):
    pid_str = ','.join(pid_list)
    data_1 = {
        'app_name': 'shop_pc',
        'app_version': '4.0',
        'warehouse': 'VIP_BJ',
        'fdc_area_id': '101103104',
        'client': 'pc',
        'mobile_platform': '1',
        'province_id': '101103',
        'api_key': '70f71280d5d547b2a7bb370a529aeea1',
        'user_id': '505534273',
        'mars_cid': '1646530621737_436d311042bf0e83b38ed94a0fe3a1d1',
        'wap_consumer': 'b',
        'productIds': pid_str,
        'scene': 'search',
        'standby_id': 'nature',
        'extParams': '{"stdSizeVids": "", "preheatTipsVer": "3", "couponVer": "v2", "exclusivePrice": "1","iconSpec": "2x", "ic2label": 1}',
        'context': '',
        '_': '1646530832972',
    }
    v2_url = 'https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/module/list/v2'
    res = requests.get(url=v2_url, headers=headers, params=data_1).json()
    for content in res['data']['products']:
        attrs = content['attrs']
        attr = ','.join([i['name'] + ': ' + i['value'] for i in attrs])
        title = content['title']
        price = content['price']['salePrice']
        shop_name = content['brandShowName']
        brandId = content['brandId']
        productId = content['productId']
        href = f'https://detail.vip.com/detail-{brandId}-{productId}.html'
        data_dict = {
            '品牌': shop_name,
            '标题': title,
            '价格': price,
            '商品属性': attr,
            '详情页': href,
        }
        csv_writer.writerow(data_dict)
        print(data_dict)


if __name__ == '__main__':
    f = open('商品.csv', mode='w', encoding='utf-8-sig', newline='')
    csv_writer = csv.DictWriter(f, fieldnames=['品牌',
                                               '标题',
                                               '价格',
                                               '商品属性',
                                               '详情页', ])
    csv_writer.writeheader()
    url = 'https://mapi.vip.com/vips-mobile/rest/shopping/pc/search/product/rank'
    headers = {
        'cookie': 'vip_first_visitor=1; vip_address=%257B%2522pid%2522%253A%2522101103%2522%252C%2522cid%2522%253A%2522101103104%2522%252C%2522pname%2522%253A%2522%255Cu6cb3%255Cu5317%255Cu7701%2522%252C%2522cname%2522%253A%2522%255Cu90af%255Cu90f8%255Cu5e02%2522%257D; vip_province=101103; vip_province_name=%E6%B2%B3%E5%8C%97%E7%9C%81; vip_city_name=%E9%82%AF%E9%83%B8%E5%B8%82; vip_city_code=101103104; vip_wh=VIP_BJ; vip_ipver=31; mst_area_code=104104; mars_cid=1646530621737_436d311042bf0e83b38ed94a0fe3a1d1; mars_sid=b8b15641a3b3f571cc9c28b5602be2b8; VIP_QR_FIRST=1; vipshop_passport_src=https%3A%2F%2Fwww.vip.com%2F; _jzqco=%7C%7C%7C%7C%7C1.1207188721.1646530653021.1646530653021.1646530653021.1646530653021.1646530653021.0.0.0.1.1; PASSPORT_ACCESS_TOKEN=2E4C3900A207E09532084B3AA1A56EA41B04CDBE; VipRUID=505534273; VipUID=7c2ed36e42d7f9bb70294ef94f61ba24; VipRNAME=ph_*****************************0c3; VipLID=0%7C1646530751%7C85dc8b; VipDegree=D1; user_class=b; VipUINFO=luc%3Ab%7Csuc%3Ab%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A0%7Cul%3A3105; vpc_uinfo=fr713%3A0%2Cfr674%3AD1%2Cfr1051%3A0%2Cfr766%3A0%2Cfr259%3AS0-4%2Cfr896%3A0%2Cfr0901%3A0%2Cfr884%3A0%2Cfr863%3A0%2Cfr249%3AB%2Cfr392%3A310505%2Cfr398%3A0%2Cfr408%3A0%2Cfr344%3A0%2Cfr444%3AA%2Cfr251%3AB%2Cfr848%3A0%2Cfr328%3A3105%2Cfr902%3A0%2Cfr901%3A0%2Cfr980%3A0; pg_session_no=17; vip_tracker_source_from=; waitlist=%7B%22pollingId%22%3A%22BC6066BB-99A2-4FCF-B928-4D58F5B133F6%22%2C%22pollingStamp%22%3A1646531102031%7D',
        'referer': 'https://category.vip.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36', }
    for page in range(0, 601, 120):
        pid_list = parse_pid(get_response(url, page).json())
        parse_data(pid_list[:50])
        parse_data(pid_list[50:100])
        parse_data(pid_list[100:])
        time.sleep(1.5)
