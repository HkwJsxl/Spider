import parsel
import requests
import concurrent.futures.thread
import csv


class JueDuiLingYu(object):
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36', }

    def get_response(self, url):
        response = requests.get(url=url, headers=self.headers).text
        return response

    def parse_1(self, parse_html):
        main_html = parsel.Selector(parse_html)
        link_list = main_html.css('.post-info > h2 > a::attr("href")').getall()
        return link_list

    def parse_2(self, link_html):
        link_data = parsel.Selector(link_html)
        title = link_data.css('#primary-home > article > header > h1::text').get()
        img_url = link_data.css('#primary-home > article > div.entry-content > img::attr("src")').getall()
        if not img_url:
            img_url = link_data.css('#primary-home > article > div.entry-content > p > img::attr("src")').getall()
        data_dict = {
            '标题': title,
            '图片地址': img_url,
        }
        return data_dict

    def run(self, url):
        link_list = self.parse_1(self.get_response(url))
        f = open('绝对领域.csv', mode='a', encoding='utf-8-sig', newline='')
        csv_writer = csv.DictWriter(f, fieldnames=['标题',
                                                   '图片地址',
                                                   ])
        csv_writer.writeheader()
        for link in link_list:
            data_dicts = self.parse_2(self.get_response(link))
            csv_writer.writerow(data_dicts)
            print(data_dicts)


if __name__ == '__main__':
    jueduilingyu = JueDuiLingYu()
    with concurrent.futures.thread.ThreadPoolExecutor(max_workers=4) as pool:
        for page in range(1, 6):
            url = f'https://www.jdlingyu.com/tag/jk%e5%88%b6%e6%9c%8d/page/{page}'
            pool.submit(jueduilingyu.run, url)
