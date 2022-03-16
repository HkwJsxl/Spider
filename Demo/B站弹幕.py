import requests
from bs4 import BeautifulSoup
import pandas as pd

# https://blog.csdn.net/qq_36330643/article/details/81288903  # 思路和流程
# 主要抓取数据包 heartbeat

if __name__ == '__main__':
    headers = {
        'cookie': "_uuid=17D39D2A-A21E-8043-92AD-B1B6F2AF4EC320579infoc; buvid3=06201A74-4D4D-4BFD-B069-FED89C254CB9148826infoc; buvid_fp=06201A74-4D4D-4BFD-B069-FED89C254CB9148826infoc; buvid_fp_plain=06201A74-4D4D-4BFD-B069-FED89C254CB9148826infoc; SESSDATA=ba30c108%2C1651584260%2C8b69f%2Ab1; bili_jct=bde1afe7475a50bf6dc17fafafa2f303; DedeUserID=506963849; DedeUserID__ckMd5=6bbdace67271ad46; sid=jwmr0br2; blackside_state=1; rpdid=|(JYl)kkk)mR0J'uYJY|JJu~u; LIVE_BUVID=AUTO5616362112472401; PVID=1; video_page_version=v_old_home; i-wanna-go-back=-1; b_ut=5; fingerprint3=39df0467a8ac842fbec247cd80b4a3a2; fingerprint=12d37e45743125341a6784d0c9a199c4; fingerprint_s=0a74d2020f65156ad539465b08013659; CURRENT_QUALITY=120; CURRENT_BLACKGAP=0; bp_video_offset_506963849=632514752809009200; innersign=1; CURRENT_FNVAL=4048",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    # 两种url都可
    url = 'https://comment.bilibili.com/174997516.xml'
    # # url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=174997516'

    req = requests.get(url, headers=headers)
    html = req.content
    html_doc = str(html, 'utf-8')  # 修改成utf-8

    # 解析
    soup = BeautifulSoup(html_doc, "lxml")
    results = soup.find_all('d')
    contents = [x.text for x in results]
    # print(contents)

    # 保存结果
    table_dict = {"contents": contents}
    df = pd.DataFrame(table_dict)
    df.to_csv("danmu.csv", mode='w', encoding='utf-8-sig')
    print(f'\033[1;36m{df}\033[1;31m')

    print('"over"'.center(50, '-'))
