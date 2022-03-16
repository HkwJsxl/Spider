import requests
import re
import pprint
import json
import random

url = 'https://www.kuaishou.com/graphql'
headers = {
    'content-type': 'application/json',
    'Cookie': 'kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; did=web_fe83435bc913e109599de8b12ae3a04d; userId=157833072; ktrace-context=1|MS43NjQ1ODM2OTgyODY2OTgyLjcxMjUxMzgzLjE2NDE5MDM5OTM3MzUuMjAyMjcyMzA=|MS43NjQ1ODM2OTgyODY2OTgyLjI0MzQ2NzIyLjE2NDE5MDM5OTM3MzUuMjAyMjcyMzE=|0|graphql-server|webservice|false|NA; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABsJQFgcZUPy2AGXkg8nc_rOmDPZCVMDOhm7lYIitPGGcxfb5T2L67r4U5_yX4FpMZpYZyBXDDENUR021TAkLJh0IsWqUBOJ4VnGrYnAF3o7Y0YlL9QsiTsNevlWOfFwpUGNfBWGacy9II-N_bj-Q4MWIWS0tscRelvyDL7d-Kjh4OszxhqKuigP0-bYmvAeBivKo8zGrKLOKiPu6tUEmhUhoSTdCMiCqspRXB3AhuFugv61B-IiCI8Si1C8ByOKUdmhl5IL6j9Fo7qPWjo2pN7xVnUoKliSgFMAE; kuaishou.server.web_ph=1feff23b54478a78c689ba150c44d180e5f7',
    'Host': 'www.kuaishou.com',
    'Origin': 'https://www.kuaishou.com',
    'Referer': 'https://www.kuaishou.com/profile/3xauthkq46ftgkg',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}
data = {
    'operationName': "visionProfilePhotoList",
    'query': "query visionProfilePhotoList($pcursor: String, $userId: String, $page: String, $webPageArea: String) {\n  visionProfilePhotoList(pcursor: $pcursor, userId: $userId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      type\n      author {\n        id\n        name\n        following\n        headerUrl\n        headerUrls {\n          cdn\n          url\n          __typename\n        }\n        __typename\n      }\n      tags {\n        type\n        name\n        __typename\n      }\n      photo {\n        id\n        duration\n        caption\n        likeCount\n        realLikeCount\n        coverUrl\n        coverUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrl\n        liked\n        timestamp\n        expTag\n        animatedCoverUrl\n        stereoType\n        videoRatio\n        profileUserTopPhoto\n        __typename\n      }\n      canAddComment\n      currentPcursor\n      llsid\n      status\n      __typename\n    }\n    hostName\n    pcursor\n    __typename\n  }\n}\n",
    'variables': {'userId': "3xauthkq46ftgkg", 'pcursor': "", 'page': "profile"},
}
proxies = [
    {'http': 'http://127.0.0.1:7890'},
    {'https': 'http://127.0.0.1:7890'},
]
proxies = random.choice(proxies)

# 字典类型转换为json字符串类型
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data, proxies=proxies)
# pprint.pprint(response.json())
data_json = response.json()
feeds = data_json['data']['visionProfilePhotoList']['feeds']
for feed in feeds:
    caption = feed['photo']['caption']
    photoUrl = feed['photo']['photoUrl']
    video_data = requests.get(url=photoUrl).content
    new_caption = re.sub(r'[/\:*?"<>|\n]', '', caption)
    with open(f'video1\\{new_caption}.mp4', mode='wb') as f:
        f.write(video_data)
    print('爬取成功')
print('over')
