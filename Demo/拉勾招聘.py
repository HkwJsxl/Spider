import re
import requests
import parsel

# url = 'https://www.lagou.com/beijing-zhaopin/Python/?labelWords=label'
# for page in range(1, 30):
url = 'https://www.lagou.com/beijing-zhaopin/Python/?filterOption=3&sid=0f3228ad7e95420983086b0ed174625a'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Cookie': 'LG_HAS_LOGIN=1; hasDeliver=0; privacyPolicyPopup=false; user_trace_token=20220114191712-88f148c2-abe0-4e64-9b6b-02ad0a1e485b; __lg_stoken__=151a0832da1e646b9a5bba8d11d04938bc1b8b29942034b4eba78619838927e2838c6c1bdcb688954f41033a807d8d87ae4f5f791d0ccd0a1755b688c1ca45c78ac10e56c292; _ga=GA1.2.1731891002.1642159232; LGUID=20220114192029-f6b3cf07-015c-41ab-a8f4-408350eb6af0; RECOMMEND_TIP=true; smidV2=20220114192314f28893edb4b137b32855ef0b4fbc0caf006cd1597ce6d5f10; thirdDeviceIdInfo=%5B%7B%22channel%22%3A1%2C%22thirdDeviceId%22%3A%22WHJMrwNw1k/Fca09zO5Svs0IjsXaIZQI738k6Dbjvg/QqocUjQRZ4SlpL34gXn1nnY294vWClzBBAdCUQ/00kxh/l0t50hvIqdCW1tldyDzmQI99+chXEimvKdHVN+CH79lCUKKcsmkSqmJzoPeggwzYmmmXo8LlTkQE5YcNLqNriNYPfoOP/blpQZJfdN5nkhsxXOHq1QfsjgzZIaYhnXu8Vg+5pExYXNoWjuqqGGQgDhxe4/3frKNM2e/xNaYrx1487582755342%22%7D%2C%7B%22channel%22%3A2%7D%5D; user-finger=9b83da9334b43f5f60c7e201c1b5b324; index_location_city=%E5%8C%97%E4%BA%AC; JSESSIONID=ABAAAECAAEBABII59DE47E03285363BC60E4C00CC56551A; X_HTTP_TOKEN=a114af805604087812313224619e8b6ce70494ab28; WEBTJ-ID=20220115152208-17e5c9d70eecc6-013f7867260354-f791b31-1327104-17e5c9d70ef107e; _putrc=DF49E2C86F9AE3BB123F89F2B170EADC; gate_login_token=22ceb7dca7b1f8b99c3e9c7b859b0bedfb9445c7ab0a3283941f96999a9feb1a; login=true; unick=%E7%94%A8%E6%88%B78210; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fbeijing-zhaopin%2FPython%2F%3FlabelWords%3Dlabel; LGSID=20220115152204-39848ef7-aa30-4eaf-a068-5ed131c79145; _gat=1; sensorsdata2015session=%7B%7D; SEARCH_ID=3a89772bdc0043a69562b1ddb28496ca; LGRID=20220115152207-4e003a55-f520-4388-8233-b00aabff0a3b; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2223540357%22%2C%22first_id%22%3A%2217e4e3159203dc-0c35197b4da0cd-f791b31-1327104-17e4e315921d36%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22lagou%22%2C%22%24latest_utm_medium%22%3A%22pctopbanner%22%2C%22%24latest_utm_campaign%22%3A%22%E5%A4%A7%E5%8E%82%E9%9D%A2%E8%AF%95%E7%9B%B4%E9%80%9A%E5%8D%A1%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2297.0.4692.71%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217e4e3159203dc-0c35197b4da0cd-f791b31-1327104-17e4e315921d36%22%7D',
    'Host': 'www.lagou.com',
    'Referer': 'https://www.lagou.com/beijing-zhaopin/Python/7/?filterOption=3&sid=0f3228ad7e95420983086b0ed174625a',
}

response = requests.get(url=url, headers=headers).text
# print(response)
selector = parsel.Selector(response)  # 把html字符串转换为selector对象
# info_data = selector.css('#s_position_list > ul::text').getall()
# info_data = selector.xpath('//*[@id="s_position_list"]/ul/li[1]/text()').getall()
info_data = re.findall(
    '<li class="con_list_item default_list" data-index="(.*?)" data-positionid="(.*?)" data-salary="(.*?)" data-company="(.*?)" data-positionname="(.*?)" data-companyid="(.*?)" data-hrid="(.*?)" data-adword="0">',
    response)
# print(info_data)
for i in info_data:
    print(i)
# print(f'第{page}页已完成')
# <li class="con_list_item default_list" data-index="0" data-positionid="9954763" data-salary="18k-35k" data-company="华为" data-positionname="python开发工程师" data-companyid="158819" data-hrid="23318857" data-adword="0">
# <li class="con_list_item default_list" data-index="1" data-positionid="9467240" data-salary="8k-16k" data-company="云孚科技" data-positionname="初级Python研发工程师" data-companyid="242209" data-hrid="8655761" data-adword="0">
