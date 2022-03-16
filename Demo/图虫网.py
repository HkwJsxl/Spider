import requests
import os

# url = 'https://tuchong.com/tags/%E5%86%99%E7%9C%9F/'

# 创建文件
if not os.path.exists('img'):
    os.mkdir('img')

for page in range(1, 10):
    print(f'正在爬取第{page}页'.center(50, '-'))
    url = f'https://tuchong.com/rest/tags/%E5%86%99%E7%9C%9F/posts?page={page}&count=20&order=weekly&before_timestamp='
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers).json()
    for post in response['postList']:
        img_id = post['images'][0]['img_id']
        user_id = post['images'][0]['user_id']
        img_id_str = post['images'][0]['img_id_str']
        img_url = f'https://photo.tuchong.com/{user_id}/f/{img_id}.jpg'
        img_data = requests.get(url=img_url).content
        with open('img\\' + img_id_str + '.jpg', mode='wb') as f:
            f.write(img_data)
        print(f'{img_id}： 下载完成')
