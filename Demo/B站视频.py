import json
import time
import requests
import re
import subprocess
import os

# 获取BV号 抓取type数据包
main_url = 'https://api.bilibili.com/x/web-interface/search/type?context=&page=1&order=click&keyword=%E6%AF%8F%E5%A4%A9%E4%B8%80%E9%81%8D%EF%BC%8C%E9%98%B2%E6%AD%A2%E6%97%A9%E6%81%8B&duration=0&tids_2=&from_source=webtop_search&from_spmid=333.1007&platform=pc&__refresh__=true&_extra=&search_type=video&tids=0&highlight=1&single_column=0'
headers = {
    'cookie': '_uuid=17D39D2A-A21E-8043-92AD-B1B6F2AF4EC320579infoc; b_nut=1636032226; buvid3=06201A74-4D4D-4BFD-B069-FED89C254CB9148826infoc; buvid_fp=06201A74-4D4D-4BFD-B069-FED89C254CB9148826infoc; buvid_fp_plain=06201A74-4D4D-4BFD-B069-FED89C254CB9148826infoc; SESSDATA=ba30c108%2C1651584260%2C8b69f%2Ab1; bili_jct=bde1afe7475a50bf6dc17fafafa2f303; DedeUserID=506963849; DedeUserID__ckMd5=6bbdace67271ad46; sid=jwmr0br2; blackside_state=1; rpdid=|(JYl)kkk)mR0J\'uYJY|JJu~u; LIVE_BUVID=AUTO5616362112472401; PVID=1; video_page_version=v_old_home; i-wanna-go-back=-1; b_ut=5; fingerprint3=39df0467a8ac842fbec247cd80b4a3a2; fingerprint=12d37e45743125341a6784d0c9a199c4; fingerprint_s=0a74d2020f65156ad539465b08013659; CURRENT_QUALITY=120; CURRENT_BLACKGAP=0; bp_video_offset_506963849=633345459612549100; innersign=1; CURRENT_FNVAL=4048',
    'referer': 'https://search.bilibili.com/all?keyword=%E6%AF%8F%E5%A4%A9%E4%B8%80%E9%81%8D%EF%BC%8C%E9%98%B2%E6%AD%A2%E6%97%A9%E6%81%8B&from_source=webtop_search&spm_id_from=333.1007&order=click&duration=0&tids_1=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
}
response = requests.get(url=main_url, headers=headers).json()
res_json = response['data']['result']
for bv in res_json:
    bv_id = bv['bvid']
    print(f'\033[1;33m{bv_id}\033[0m')
    url = f'https://www.bilibili.com/video/{bv_id}'
    res = requests.get(url=url, headers=headers).text
    title = re.findall('<h1 title="(.*?)" class="video-title">', res)[0]
    title = re.sub(r'[/:*?"<>|\]]', '', title)
    playinfo = re.findall('<script>window.__playinfo__=(.*?)</script>', res)[0]
    json_data = json.loads(playinfo)
    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    video_url = json_data['data']['dash']['video'][0]['baseUrl']
    audio_content = requests.get(url=audio_url, headers=headers).content
    video_content = requests.get(url=video_url, headers=headers).content
    print('wait'.center(50, '-'))
    with open(title + '.mp3', mode='wb') as f:
        f.write(audio_content)
    with open(title + '.mp4', mode='wb') as f:
        f.write(video_content)
    command = f"ffmpeg -i {title}.mp4 -i {title}.mp3 -c:v copy -c:a aac -strict experimental {bv_id}.mp4"
    subprocess.run(command, shell=True)
    os.remove(f'{title}.mp3')
    os.remove(f'{title}.mp4')
    print(f'\033[1;36m{bv_id} already Done\033[0m')
    time.sleep(3)
