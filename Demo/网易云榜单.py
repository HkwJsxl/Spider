# http://music.163.com/song/media/outer/url?id=
# 网易：https://music.163.com/#/song?id=25906124
# ＱＱ：https://y.qq.com/n/yqq/song/002B2EAA3brD5b.html
# 酷狗：http://www.kugou.com/song/#hash=08228af3cb404e8a4e7e9871bf543ff6
# 酷我：https://www.kuwo.cn/play_detail/175264544/
# 千千：https://music.taihe.com/song/266069
# 一听：https://www.1ting.com/player/b6/player_357838.html
# 咪咕：https://music.migu.cn/v3/music/song/477803
# 荔枝：https://www.lizhi.fm/1947925/2498707770886461446
# 蜻蜓：https://www.qingting.fm/channels/158696/programs/5266259
# 喜马拉雅：https://www.ximalaya.com/51701370/sound/24755731
# 5sing原创：http://5sing.kugou.com/yc/3082899.html
# 5sing翻唱：http://5sing.kugou.com/fc/14369766.html
import requests
import re

url = 'https://music.163.com/discover/toplist?id=3778678'
headers = {
    'cookie': '_iuqxldmzr_=32; _ntes_nnid=e0f94449c668badebbabe0f940d233f4,1642064895840; _ntes_nuid=e0f94449c668badebbabe0f940d233f4; NMTID=00OQIeM-qTM9K3eWEYNo9k7oiDGlAsAAAF-UrHWvw; WNMCID=nnpxdw.1642064896673.01.0; WEVNSM=1.0.0; WM_TID=Y5ghnkxkFpNFARUBBAc%2FpgBgpjvRGpPM; WM_NI=Ywce4fvJ%2FGJHpyxgKWhghVmr%2Fllp8Y1cLDrwdoI8Hut8vnSZjTrhcmN67smr6jtcwtdi%2FVbaR%2F4BY3uFw9PF3AfYSg9GtJtjiiADDZPe3Kvmz4xXqgsc6WCV3c%2BRWJ%2FvYVE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed7aa21f8bab8b9b450ed8e8ea7c15b978b9bbbf17f95bd828bb345f1eefcb9e22af0fea7c3b92a9ba9ad86b76eb696e1a8c944b4a7b888ca5dacb9a8b7f07aedb4a491bb53f3bd84a5f17da8b187d9cb7fb8e8ba8fd252aa8cbe89e2678eeaf994f07af6b6bc84f680a8b7e1b7e16b92f1fca3dc39b79ab9dad34ef19faabad26dfb99bcabf762abb78fa5c75294bbfdacf567baecb8b9f46db1bdfab8c25ef1bde5b3d642edaa97b7c837e2a3; JSESSIONID-WYYY=c0HnkPmb8iZxoNDWX9f9ijsQcY4dAoY12YQd1kqM6f4MCnoW2igUJoYpgJcvJ%5CnFsMtvavHbbBxVD5IZiM3CAncb7QDrinKfF5%2Bl%2Bbel8NV90Jd8xSw%5CcYoDryZhYV4bs96oTrbvtGtkoXaoEP6aZzoDRPFFCjtl88Z7NjqktJjG5iZ0%3A1642073702629',
    'referer': 'https://music.163.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
data_html = requests.get(url=url, headers=headers).text
# <li><a href="/song?id=1901371647">孤勇者</a></li>
# <li><a href="/song?id=488249475">哪里都是你</a></li>
# <li><a href="/song?id=1891469546">删了吧</a></li>
data_music = re.findall('<li><a href="/song\?id=(.*?)">(.*?)</a></li>', data_html)
i = 1
for data in data_music:
    id_ = data[0]
    name = data[1]
    add = requests.get(url=f'https://music.163.com/song/media/outer/url?id={id_}').content
    # print(id, name, add)
    with open(f'music\\{name}.mp3', mode='wb') as f:
        f.write(add)
    print(f'{i}---{name}---下载成功')
    i += 1
print('over')
