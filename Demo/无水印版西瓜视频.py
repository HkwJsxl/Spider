import pprint

import requests  # 发送网络请求 第三方
import re  # 提取数据内容
import base64  # 内置 不需要你额外安装
import subprocess
import os

url = 'https://www.ixigua.com/6995198185928917517'
headers = {
    'cookie': 'MONITOR_WEB_ID=c27b9f4a-4917-4256-be93-e948308467e3; passport_csrf_token_default=953dd0d49c23abe66533828fa8ed0f8b; passport_csrf_token=953dd0d49c23abe66533828fa8ed0f8b; uid_tt=93c867fb443fdd4f7ba75c2b24678bd0; uid_tt_ss=93c867fb443fdd4f7ba75c2b24678bd0; sid_tt=db0c9d4ab90ee7a872404a7b1c7ca70d; sessionid=db0c9d4ab90ee7a872404a7b1c7ca70d; sessionid_ss=db0c9d4ab90ee7a872404a7b1c7ca70d; sid_ucp_v1=1.0.0-KDdmMDYwNTM3Y2MyODg0Yzk0NTU4MjI0ZjFmMWY4YmYyYTZiMDY3NWIKDgjo5IrYFxDmnYCPBhgYGgJobCIgZGIwYzlkNGFiOTBlZTdhODcyNDA0YTdiMWM3Y2E3MGQ; ssid_ucp_v1=1.0.0-KDdmMDYwNTM3Y2MyODg0Yzk0NTU4MjI0ZjFmMWY4YmYyYTZiMDY3NWIKDgjo5IrYFxDmnYCPBhgYGgJobCIgZGIwYzlkNGFiOTBlZTdhODcyNDA0YTdiMWM3Y2E3MGQ; sid_guard=db0c9d4ab90ee7a872404a7b1c7ca70d%7C1642073830%7C3024000%7CThu%2C+17-Feb-2022+11%3A37%3A10+GMT; ttcid=0cbb8baca16443e8b2320dfcb0ebd3ab24; ixigua-a-s=1; BD_REF=1; support_webp=true; support_avif=true; __gads=ID=b750d35ceb3b300e-22f59bfba5d0002a:T=1645008733:RT=1645008733:S=ALNI_MZSPYii3eywVYfjuGdExhE-Dw3tLw; _tea_utm_cache_1300=undefined; __ac_signature=_02B4Z6wo00f01cBYT5AAAIDAo1KP-yGh3ynAfEsAABIcb5; ttwid=1%7Cbki1kBY9AbTODWRF62oQmAFNNd1E9JpOrWrMnRcIdwY%7C1645013401%7C37584981fca703c40f60dfc56b20420d417a7ec3ae7b7f96d0bf581a309da711; __ac_nonce=0620cecf80023f1d97fa9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
# 1. 发送请求
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
# <Response [200]>: 访问成功
# 2. 获取数据
data_html = response.text
# 3. 解析数据
# 视频链接
title = re.findall('<title data-react-helmet="true">(.*?)</title>', data_html)[0]
title = title.replace(' ', '')
main_url_list = re.findall('main_url":"(.*?)","backup_url_1"', data_html)
# pprint.pprint(main_url_list)
audio_url = ''
video_url = ''
for main_url in main_url_list[:-1]:
    main_url = base64.b64decode(main_url)
    try:
        audio_url = main_url.decode()
    except:
        video_url = str(main_url).replace(r'.\xd3M\x85', '?')[2: -1]
print(video_url)
print(audio_url)
# 4. 保存数据
video_data = requests.get(video_url).content
with open(f'data/{title}.mp4', mode='wb') as f:
    f.write(video_data)
audio_data = requests.get(audio_url).content
with open(f'data/{title}.mp3', mode='wb') as f:
    f.write(audio_data)
cmd = r'ffmpeg -i ' + 'data/' + title + '.mp4 -i ' + 'data/' + title + '.mp3 -acodec copy -vcodec copy ' + "data/" + title + 'out.mp4'
subprocess.run(cmd, shell=True)
os.remove(f'data/{title}.mp3')
os.remove(f'data/{title}.mp4')
print('over')
