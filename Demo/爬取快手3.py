import requests
import re
import pprint
import json
import random

url = 'https://www.kuaishou.com/graphql'
headers = {
    'content-type': 'application/json',
    'Cookie': 'kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; did=web_fe83435bc913e109599de8b12ae3a04d; userId=157833072; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABRmYeML0OrdVZoJEGYseU95EmQyEQVJQRC_7MX9ilOA8YnCmrLW8IDwQ1f7iWtIlHaRc1OW0Zq0F4N5WbSMKCxVUncneQcGhxXD6FK02EJfj1x6qpm_RIymCdaOhpt_fFAKoEqPzS3oP7yIrvZwF68P_t5yMb0nZ_f8DkZtszOCuExqHF_BW04aosB2fxBYnllC2pI6UD-InlXOJmgsEPBBoSfVpfCMyKId3v5a5yUz8_gvvmIiBN6bJID8ZWdXnIVwjaaljT7vyVN2QTYr3SHojLEpWutygFMAE; kuaishou.server.web_ph=7e3426953f1972c3ff8e136eeef984b38b89',
    'Host': 'www.kuaishou.com',
    'Origin': 'https://www.kuaishou.com',
    'Referer': 'https://www.kuaishou.com/brilliant',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}


def get_page(pcursor):
    data = {
        'operationName': "hashTagDataQuery",
        'query': "fragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    id\n    duration\n    caption\n    likeCount\n    realLikeCount\n    coverUrl\n    photoUrl\n    coverUrls {\n      url\n      __typename\n    }\n    timestamp\n    expTag\n    animatedCoverUrl\n    distance\n    videoRatio\n    liked\n    stereoType\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  __typename\n}\n\nquery hashTagDataQuery($tagName: String, $pcursor: String, $fromPhotoId: String, $page: String, $webPageArea: String) {\n  hashTagData(tagName: $tagName, pcursor: $pcursor, fromPhotoId: $fromPhotoId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    pcursor\n    sessionId\n    webPageArea\n    feeds {\n      ...feedContent\n      __typename\n    }\n    __typename\n  }\n}\n",
        'variables': {'tagName': "防控疫情我们在一起", 'pcursor': "", 'page': "detail", 'webPageArea': "hashtagxxnull"},
    }
    if pcursor != 0:
        data = {
            'operationName': "hashTagDataQuery",
            'query': "fragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    id\n    duration\n    caption\n    likeCount\n    realLikeCount\n    coverUrl\n    photoUrl\n    coverUrls {\n      url\n      __typename\n    }\n    timestamp\n    expTag\n    animatedCoverUrl\n    distance\n    videoRatio\n    liked\n    stereoType\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  __typename\n}\n\nquery hashTagDataQuery($tagName: String, $pcursor: String, $fromPhotoId: String, $page: String, $webPageArea: String) {\n  hashTagData(tagName: $tagName, pcursor: $pcursor, fromPhotoId: $fromPhotoId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    pcursor\n    sessionId\n    webPageArea\n    feeds {\n      ...feedContent\n      __typename\n    }\n    __typename\n  }\n}\n",
            'variables': {'tagName': "防控疫情我们在一起", 'pcursor': pcursor, 'page': "detail", 'webPageArea': "hashtagxxnull"},
        }
    if pcursor == None:  # 最底 pcursor 为 no_more
        print('全部下载成功')
        return 0  # 退出
    
    data = json.dumps(data)
    response = requests.post(url=url, headers=headers, data=data)
    # pprint.pprint(response)
    data_json = response.json()
    feeds = data_json['data']['hashTagData']['feeds']
    pcursor = data_json['data']['hashTagData']['pcursor']
    page = 1

    for feed in feeds:
        caption = feed['photo']['caption']
        photoUrl = feed['photo']['photoUrl']
        # caption = re.sub(r'[/\:*?"<>|\n]', '', caption)
        # video_data = requests.get(url=photoUrl).content
        # with open(f'video2\\{caption}.mp4', mode='wb') as f:
        #     f.write(video_data)
        print(caption, photoUrl)
        print(f'第{page}个爬取成功')
        page += 1
    # print('本页已完成'.center(50, '-'))
    get_page(pcursor)


get_page(0)
