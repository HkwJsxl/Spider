import requests
import re
import pprint
import json
import random

url = 'https://www.kuaishou.com/graphql'
headers = {
    'content-type': 'application/json',
    'Cookie': 'kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; did=web_fe83435bc913e109599de8b12ae3a04d; userId=157833072; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABfjccvWpDHxk1Go3divpumZXbwfwLh46sLUzgJtjyl2NQWPl-63w7957WyuPwel4ivMwkwKtPW0h-2FA5Mkz9z-q45ibn-FRJgXxcRR9tdhhfmhtzM2m-fc0URHHPZxUoxptugopcmHeM9MXbt7uIoudmvROSG5KERhnQa9XxDd9e0-Bs-o66gtwuA0Ci-w0YHzdlcPjyU5z14VNVLz_e8hoSsmhEcimAl3NtJGybSc8y6sdlIiAI2xQEOGb8qU9MlTy8ro3kBW3I8R6A18ZgbbczlFkMoCgFMAE; kuaishou.server.web_ph=57421674dcb7e7af191242b8cb6ff0aac512',
    'Host': 'www.kuaishou.com',
    'Origin': 'https://www.kuaishou.com',
    'Referer': 'https://www.kuaishou.com/profile/3xv78fxycm35nn4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}


def get_page(pcursor):
    data = {
        'operationName': "visionProfilePhotoList",
        'query': "query visionProfilePhotoList($pcursor: String, $userId: String, $page: String, $webPageArea: String) {\n  visionProfilePhotoList(pcursor: $pcursor, userId: $userId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      type\n      author {\n        id\n        name\n        following\n        headerUrl\n        headerUrls {\n          cdn\n          url\n          __typename\n        }\n        __typename\n      }\n      tags {\n        type\n        name\n        __typename\n      }\n      photo {\n        id\n        duration\n        caption\n        likeCount\n        realLikeCount\n        coverUrl\n        coverUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrl\n        liked\n        timestamp\n        expTag\n        animatedCoverUrl\n        stereoType\n        videoRatio\n        profileUserTopPhoto\n        __typename\n      }\n      canAddComment\n      currentPcursor\n      llsid\n      status\n      __typename\n    }\n    hostName\n    pcursor\n    __typename\n  }\n}\n",
        'variables': {'userId': "3xv78fxycm35nn4", 'pcursor': '', 'page': "profile"}
    }
    if pcursor != 0:
        data = {
            'operationName': "visionProfilePhotoList",
            'query': "query visionProfilePhotoList($pcursor: String, $userId: String, $page: String, $webPageArea: String) {\n  visionProfilePhotoList(pcursor: $pcursor, userId: $userId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      type\n      author {\n        id\n        name\n        following\n        headerUrl\n        headerUrls {\n          cdn\n          url\n          __typename\n        }\n        __typename\n      }\n      tags {\n        type\n        name\n        __typename\n      }\n      photo {\n        id\n        duration\n        caption\n        likeCount\n        realLikeCount\n        coverUrl\n        coverUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrl\n        liked\n        timestamp\n        expTag\n        animatedCoverUrl\n        stereoType\n        videoRatio\n        profileUserTopPhoto\n        __typename\n      }\n      canAddComment\n      currentPcursor\n      llsid\n      status\n      __typename\n    }\n    hostName\n    pcursor\n    __typename\n  }\n}\n",
            'variables': {'userId': "3xv78fxycm35nn4", 'pcursor': pcursor, 'page': "profile"}
        }
    if pcursor == 'no_more':  # 最底 pcursor 为 no_more
        print('全部下载成功')
        return 0  # 退出
    proxies = [
        {'http': 'http://127.0.0.1:7890'},
        {'http': 'http://64.227.41.59:443'},
        {'http': 'http://112.5.37.33:777'},
        {'https': 'http://127.0.0.1:7890'},
    ]
    proxies = random.choice(proxies)
    data = json.dumps(data)
    response = requests.post(url=url, headers=headers, data=data, proxies=proxies)
    # pprint.pprint(response)
    data_json = response.json()
    feeds = data_json['data']['visionProfilePhotoList']['feeds']
    pcursor = data_json['data']['visionProfilePhotoList']['pcursor']
    page = 1

    for feed in feeds:
        print(f'正在爬取第{page}个短视频'.center(50, '-'))
        caption = feed['photo']['caption']
        photoUrl = feed['photo']['photoUrl']
        caption = re.sub(r'[/\:*?"<>|\n]', '', caption)
        video_data = requests.get(url=photoUrl).content
        with open(f'video2\\{caption}.mp4', mode='wb') as f:
            f.write(video_data)
        # print('爬取成功')
        # print(caption, photoUrl)
        # print(photoUrl)
        print(f'第{page}个爬取成功')
        page += 1
    print('本页已完成'.center(50, '-'))
    get_page(pcursor)


get_page(0)
