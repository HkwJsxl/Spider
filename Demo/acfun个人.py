import pprint
import json
import requests
import re
from tqdm import tqdm

headers = {
    'cookie': 'csrfToken=mUipIA-wgqwtDpCQ7PXKT2M9; _did=web_957330453AABF67E; webp_supported=%7B%22lossy%22%3Atrue%2C%22lossless%22%3Atrue%2C%22alpha%22%3Atrue%2C%22animation%22%3Atrue%7D; lsv_js_player_v2_main=89abb7; auth_key=62693769; ac_username=%E6%98%AF%E6%B3%A1%E6%A4%92; stochastic=MzcyaXU5c3BkZWQ%3D; acPasstoken=ChVpbmZyYS5hY2Z1bi5wYXNzdG9rZW4ScHXtkz3rM-mv6nDDCqKBm9UPFi0GEeC59xnw_5Vgc62hgfT52QhH_K7apulkc2YXTWo5ugPHM9MEURWH4Pvp4a0i9sC-jZdh855SZlfsprrJTIrQk-KWKHwCZ6DMP981fEGAZ3u-80EXzoISxr5MD_4aEsE0X1zyB8j-3PWulytMu8UuACIghjkRXze8vf2mxD2jEVqJJMe-Tx85nF5cHmxDNIpZMBkoBTAB; acPostHint=c4fa6cb810e41b64744cb93c945568f692c6; ac_userimg=https://imgs.aixifan.com/newUpload/62693769_5ee0b9ce016b4a2ab319486f8b62e484.jpg; cur_req_id=686556921242A603_self_2d45c537a4f93b4689463857c3114dd1; cur_group_id=686556921242A603_self_2d45c537a4f93b4689463857c3114dd1_0; isCloseVisit=1642953600000; safety_id=AAK9OIQoTbd7P58GVPO8ndim; _did=web_957330453AABF67E',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
}
mian_url = 'https://www.acfun.cn/u/4537972'
mian_res = requests.get(url=mian_url, headers=headers).text
# print(mian_res)
mediaId = re.findall('<a href="/v/(.*)" target="_blank" class="ac-space-video weblog-item" data-wbinfo=.*>',
                     mian_res)
# print(mediaId)
for id_ in mediaId:
    url = f'https://www.acfun.cn/v/{id_}'
    response = requests.get(url=url, headers=headers).text
    # print(response)
    html_data = re.findall('window.pageInfo = window.videoInfo = (.*);', response)[0]
    # print(html_data)
    json_data = json.loads(html_data)
    # pprint.pprint(json_data)
    title_info = json_data['title']
    title_info = re.sub(r'[/\":<>*?|\n]]', '', title_info)
    name = json_data['user']['name']
    info = json_data['currentVideoInfo']['ksPlayJson']
    info = json.loads(info)
    m3u8_url = info['adaptationSet'][0]['representation'][0]['backupUrl'][0]
    # pprint.pprint(m3u8_url)
    res = requests.get(url=m3u8_url, headers=headers).text
    res_info = re.sub('#EXT.*', '', res).split()
    # print(res_info)
    for ts in tqdm(res_info):
        ts_url = 'https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/' + ts
        content = requests.get(url=ts_url, headers=headers).content
        title = ts.split('.')[1]
        with open(f'video/{title_info}.mp4', 'ab') as f:
            f.write(content)
    # print(title_info, name, title, ts_url)
    print(f'{title_info}---下载完成'.center(50, '-'))
