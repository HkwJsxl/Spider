import requests
import demjson
import json
import pandas as pd

data_list = []
for page in range(15, 2000, 30):
    url = f'https://mfm.video.qq.com/danmu?otype=json&callback=jQuery191007901292477663402_1642858672996&target_id=7626117232%26vid%3Dn0041aa087e&session_key=0%2C0%2C0&timestamp={page}'
    headers = {
        # 'cookie': 'RK=GDLQtsCqEP; ptcz=e598de8d32a48d8b2a036b763604b34d0e5d41bbc0bc89adf37ca075e51264c7; tvfe_boss_uuid=2f54e3d09274069c; pgv_pvid=2230046660; video_platform=2; video_guid=744c858379718e45; o_cookie=562172420; pac_uid=1_562172420; eas_sid=t156Y4O0H0t9C0R3O0t0t0M8m3; luin=o0562172420; main_login=qq; vuserid=454142099; login_time_init=1641709419; _video_qq_version=1.1; _video_qq_main_login=qq; _video_qq_appid=3000501; _video_qq_vuserid=454142099; _video_qq_login_time_init=1641709419; fqm_pvqid=36260b0a-2a8a-488c-b5ec-04ded58eb627; lskey=00010000407213dfe78ad62fb62360a0226641c3a0645562a3b4a9108f5ad5696711043da25c9e0bcc95d697; vversion_name=8.2.95; video_omgid=744c858379718e45; vusession=v2Z4MEN_X8pvih0oiAaWPQ..; _video_qq_vusession=v2Z4MEN_X8pvih0oiAaWPQ..; pgv_info=ssid=s850541216; next_refresh_time=6592; _video_qq_next_refresh_time=6592; login_time_last=2022-1-23 10:29:20',
        # 'referer': 'https://v.qq.com/',
        # 'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        # 'sec-ch-ua-mobile': '?0',
        # 'sec-ch-ua-platform': '"Windows"',
        # 'sec-fetch-dest': 'script',
        # 'sec-fetch-mode': 'no-cors',
        # 'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    }
    data = {
        'otype': 'json',
        # 'callback': 'jQuery191007901292477663402_1642858672996',
        'target_id': '7626117232&vid=n0041aa087e',
        # 'session_key': '0,0,0',
        'timestamp': f'{page}',
        # '_': '1642858673019',
    }
    response = requests.get(url=url, headers=headers, data=data).text
    # enc = demjson.encode(response, encoding='utf-8')
    # json_data = json.loads(enc)
    # print(json_data)
    # print(response)
    response = json.loads(response, strict=False)
    comments = response['comments']
    for comment in comments:
        data_dict = {}
        data_dict['opername'] = comment['opername']
        data_dict['content'] = comment['content']
        data_list.append(data_dict)
        print(data_dict)

save_data = pd.DataFrame(data_list)
save_data.to_csv('danmu.csv', mode='w', encoding='utf-8-sig')
