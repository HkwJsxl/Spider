import requests
import re
import json
import csv

f = open('疫情数据.csv', mode='w', encoding='utf-8_sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    'area',
    'confirmedRelative',
    'curConfirm',
    'confirmed',
    'crued',
    'died',
])
csv_writer.writeheader()
url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
}
response = requests.get(url=url, headers=headers).text
main_info = re.findall('<script type="application/json" id="captain-config">(.*?)</script>', response)[0]
main_info = json.loads(main_info)
caseList = main_info['component'][0]['caseList']
for case in caseList:
    dict_data = {
        'area': case['area'],  # 地区
        'confirmedRelative': case['confirmedRelative'],  # 新增人数
        'curConfirm': case['curConfirm'],  # 现有人数
        'confirmed': case['confirmed'],  # 累计人数
        'crued': case['crued'],  # 治愈人数
        'died': case['died'],  # 治愈人数
    }
    print(dict_data)
    csv_writer.writerow(dict_data)
