import requests


def send_url(url):
    response = requests.get(url=url, headers=headers)
    return response


def parse_data(json_data):
    object_list = json_data['data']['object_list']
    url_list = []
    for obj in object_list:
        img_url = obj['photo']['path']
        url_list.append(img_url)
    return url_list


def save_data(file_name, img_url):
    with open('img\\' + file_name, mode='wb') as f:
        f.write(img_url)
    print('\033[1;36m下载完成', file_name)


if __name__ == '__main__':
    for page in range(24, 100, 24):
        print('\033[1;31m正在爬取'.center(50, '-'))
        url = f'https://www.duitang.com/napi/blogv2/list/by_search/?kw=%E7%BE%8E%E5%A5%B3&after_id={page}'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        }
        json_data = send_url(url).json()
        url_list = parse_data(json_data)
        for img_name in url_list:
            img_data = send_url(img_name).content
            img_name = img_name.split('/')[-1]
            save_data(img_name, img_data)
    print('done')
