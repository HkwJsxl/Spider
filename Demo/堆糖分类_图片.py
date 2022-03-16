import requests


def send_request(url):
    response = requests.get(url=url, headers=headers)
    return response


def parse_data(json_data):
    object_list = json_data['data']['object_list']
    img_list = []
    for obj in object_list:
        img_url = obj['photo']['path']
        img_list.append(img_url)
    return img_list


def save_data(file_name, img_data):
    with open('img\\' + file_name, mode='wb') as f:
        f.write(img_data)
    print('\033[1;36m下载完成', file_name)


if __name__ == '__main__':
    for page in range(24, 300, 24):
        print('\033[1;31m正在爬取'.center(50, '-'))
        url = f'https://www.duitang.com/napi/blog/list/by_filter_id/?include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Csender%2Calbum%2Creply_count&filter_id=%E6%97%85%E8%A1%8C&start={page}'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        }
        json_data = send_request(url).json()
        img_list = parse_data(json_data)
        for img_url in img_list:
            file_name = img_url.split('/')[-1]
            img_data = send_request(url=img_url).content
            save_data(file_name, img_data)
    print('done')
