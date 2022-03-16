# url = 'https://www.kanxiaojiejie.com/'

import requests
import parsel


def get_response(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36', }
    response = requests.get(url=url, headers=headers)
    return response


def parse_data_1(html_data):
    selector = parsel.Selector(html_data)
    href = selector.css('.entry-top .entry-thumbnail::attr("href")').getall()
    return href


def parse_data_2(html_data):
    selector = parsel.Selector(html_data)
    href = selector.css('.entry.themeform > p > img::attr("src")').getall()
    return href


def save_img(img_url_list):
    for img_href in img_url_list:
        img_url = parse_data_2(get_response(img_href).text)[0]
        title = img_url.split('/')[-1]
        img_data = get_response(img_url).content
        with open('img\\' + title, mode='wb') as f:
            f.write(img_data)
        print(f'{title} already done')


if __name__ == '__main__':
    for page in range(1, 4):
        print(f'\033[1;33m正在爬取{page}页内容\033[0m'.center(50, '-'))
        url = f'https://www.kanxiaojiejie.com/page/{page}'
        img_href_list = parse_data_1(get_response(url).text)
        save_img(img_href_list)
