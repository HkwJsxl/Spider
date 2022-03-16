import requests
import json

url = 'https://www.ixigua.com/api/videov2/author/new_video_list?_signature=_02B4Z6wo00f01olCxcQAAIDCCUA.hKaAKVKJZsFAAMO97e&to_user_id=6839565013&offset=30&limit=30&maxBehotTime=1631970973&order=new&isHome=0'
headers = {
    'cookie': 'ttcid=69021344ff8d40458f21f27877dfe36130; MONITOR_WEB_ID=214220dd-be3c-4b04-a824-143713200a47; _tea_utm_cache_1300=undefined; support_webp=true; support_avif=true; __ac_nonce=061e13029006ccc592cf7; __ac_signature=_02B4Z6wo00f01uO13pQAAIDCY7ck1mvJzp7jkdoAANkZb1; theater=1; s_v_web_id=verify_47108680dea8be62a88bcf089666dba9; _tea_utm_cache_2018=undefined; MONITOR_DEVICE_ID=b6354682-768f-461d-8256-9fbe1f63a52c; passport_csrf_token_default=1472db6a7536b19114fb186004f2b9a2; passport_auth_status=dd6760d1675035a110cd0029a7ab07a6%2C; passport_auth_status_ss=dd6760d1675035a110cd0029a7ab07a6%2C; sid_guard=bdca92fe751b4d7a5f0e8ee727ea06f8%7C1642148034%7C5183999%7CTue%2C+15-Mar-2022+08%3A13%3A53+GMT; uid_tt=3ed666427c15ae0aedf4e669f3a52afe; uid_tt_ss=3ed666427c15ae0aedf4e669f3a52afe; sid_tt=bdca92fe751b4d7a5f0e8ee727ea06f8; sessionid=bdca92fe751b4d7a5f0e8ee727ea06f8; sessionid_ss=bdca92fe751b4d7a5f0e8ee727ea06f8; sid_ucp_v1=1.0.0-KGZhMjUzYTE3YWE5M2U1NmU3MzUwNzAwYTc0NTJmODFmZWVmNmE3YTEKFgjewqGY4Y12EMLhhI8GGOgNOAJA7AcaAmhsIiBiZGNhOTJmZTc1MWI0ZDdhNWYwZThlZTcyN2VhMDZmOA; ssid_ucp_v1=1.0.0-KGZhMjUzYTE3YWE5M2U1NmU3MzUwNzAwYTc0NTJmODFmZWVmNmE3YTEKFgjewqGY4Y12EMLhhI8GGOgNOAJA7AcaAmhsIiBiZGNhOTJmZTc1MWI0ZDdhNWYwZThlZTcyN2VhMDZmOA; passport_csrf_token=1472db6a7536b19114fb186004f2b9a2; ixigua-a-s=3; ttwid=1%7CEYYmEVfFq6Mv6JLp7_DsfIo8NtiF-sH4YztoA0vBaEI%7C1642149525%7Ce2a3d414b9fe2aea9a9607e55c1cb37638ea3393c9aa1cfa85790f98e483b878',
    'referer': 'https://www.ixigua.com/home/6839565013/?list_entrance=search',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}

response = requests.get(url=url, headers=headers).json()
# print(response)
videoList = response['data']['videoList']
for video in videoList:
    title = video['title']
    article_url = video['article_url']
    video_data = requests.get(url=article_url, headers=headers).content
    # print(title, article_url)
    with open(f'video2\\{title}.mp4', 'wb') as f:
        f.write(video_data)
    f.close()
    print(f'{title}---爬取成功')
print('over')
