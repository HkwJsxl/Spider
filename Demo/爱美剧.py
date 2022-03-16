import concurrent.futures.thread
import requests
import re


class AiMeiJu(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://www.imeiju.pro/js/player/rrm3u8.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36', }

    def get_request_mian(self, url, link):
        data = {
            'url': link,
            'f': 'ck_m3u8',
        }
        response = requests.get(url=url, headers=self.headers, params=data)
        return response

    def get_request(self, url):
        res = requests.get(url=url)
        return res

    def run(self, url):
        main_html = self.get_request(url)
        # 自动编解码
        main_html.encoding = main_html.apparent_encoding
        title = re.findall("var playn = '(.*?)'", main_html.text)[0]
        m3u8_url_list = re.findall('第(\d+)集\$(.*?).m3.*?m3u8', main_html.text)
        for num, link in m3u8_url_list:
            m3u8_hand = 'https://www.imeiju.pro/ckplayerx/m3u8.php'
            m3u8_html = self.get_request_mian(m3u8_hand, link + '.m3u8').text
            m3u8_url = re.findall("url: '(.*?)'", m3u8_html)[0]
            ts_html = self.get_request(m3u8_url).text
            ts_list = re.sub('#(.*)\n', '', ts_html).split('\n')[:-1]
            for ts in ts_list:
                ts_url = f'https://fangao.stboda.com/concat/20220301/d8335ce5a63941d78d2a94ff4c24176d/cloudv-transfer/{ts}'
                ts_data = self.get_request(ts_url).content
                with open(f'{title}' + num + '.mp4', mode='ab') as f:
                    f.write(ts_data)
                print(title, num, ts_url)


if __name__ == '__main__':
    aimeiju = AiMeiJu()
    url = 'https://www.imeiju.pro/Play/7982-0-0.html'
    with concurrent.futures.thread.ThreadPoolExecutor(max_workers=4) as fool:
        fool.submit(aimeiju.run, url)
