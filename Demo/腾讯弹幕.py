import requests
import demjson
import json
import pandas as pd

data_list = []
for page in range(15, 2000, 30):
    url = f'https://mfm.video.qq.com/danmu?otype=json&callback=jQuery191007901292477663402_1642858672996&target_id=7626117232%26vid%3Dn0041aa087e&session_key=0%2C0%2C0&timestamp={page}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    }
    data = {
        'otype': 'json',
        'target_id': '7626117232&vid=n0041aa087e',
        # 'session_key': '0,0,0',
        'timestamp': f'{page}',
        # '_': '1642858673019',
    }
    response = requests.get(url=url, headers=headers, data=data).text
    response = json.loads(response, strict=False)
    comments = response['comments']
    for comment in comments:
        data_dict = {'opername': comment['opername'], 'content': comment['content']}
        data_list.append(data_dict)
        print(data_dict)

save_data = pd.DataFrame(data_list)
save_data.to_csv('danmu.csv', mode='w', encoding='utf-8-sig')
