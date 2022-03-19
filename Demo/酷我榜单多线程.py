import requests
import concurrent.futures.thread


class KuWoYinYue(object):
    def __init__(self):
        self.headers = {
            'Cookie': 'uname3=%u3164%u3164%uD83C%uDDED.; t3kwid=574311085; userid=574311085; websid=1771276606; pic3="https://thirdwx.qlogo.cn/mmopen/vi_32/7C10RLAxBpkqaMJKUxXs0iacHB2msut3zjuYcuvDzMg6S5QZo2KmnLx0hl0ug1sEjy183dhYyibgWqlPSZdkeQOw/132"; t3=weixin; kw_token=3ISGGFEI4YL',
            'csrf': '3ISGGFEI4YL',
            'Host': 'www.kuwo.cn',
            'Referer': 'http://www.kuwo.cn/rankList',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
        }

    def get_request(self, url):
        response = requests.get(url, headers=self.headers)
        return response

    def prase_data(self, res_data):
        for musicList in res_data:
            artist = musicList['artist']
            music_id = musicList['name']
            album = musicList['album']
            rid = musicList['rid']
            print([artist, music_id, album, rid])
            playurl = f'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={rid}'
            res = self.get_request(playurl).json()
            if res['code'] == 200:
                video_url = res['data']['url']
                if video_url:
                    try:
                        video_data = requests.get(video_url, timeout=5).content
                        with open('video\\' + music_id + '-' + artist + '.mp3', 'wb') as f:
                            f.write(video_data)
                        print('success')
                    except Exception as error:
                        print(error)
            else:
                print('unsuccess')

    def run(self, url):
        self.prase_data(self.get_request(url).json()['data']['musicList'])


if __name__ == '__main__':

    kuwo = KuWoYinYue()
    with concurrent.futures.thread.ThreadPoolExecutor(max_workers=4) as tool:
        for page in range(1, 6):
            print(f'正在爬取第{page}页'.center(50, '-'))
            url = f'http://www.kuwo.cn/api/www/bang/bang/musicList?bangId=93&pn={page}&rn=30&httpsStatus=1&reqId=a2d2b0d0-a728-11ec-b352-3511a48e394c'
            tool.submit(kuwo.run, url)
