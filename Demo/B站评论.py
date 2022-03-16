import pprint
import requests
import pandas as pd


def save_data(comments_dict):
    df = pd.DataFrame(comments_dict)
    df.to_csv('reply.csv', mode='w', encoding='utf-8-sig', )
    print(f'\033[1;35m{df}\033[1;31m')
    print('"over"'.center(50, '-'))


if __name__ == '__main__':

    # https://www.cnblogs.com/phyger/p/14026663.html # 思路和流程
    header = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0",
              "Cookie": "_uuid=17D39D2A-A21E-8043-92AD-B1B6F2AF4EC320579infoc; b_nut=1636032226; buvid3=06201A74-4D4D-4BFD-B069-FED89C254CB9148826infoc; buvid_fp=06201A74-4D4D-4BFD-B069-FED89C254CB9148826infoc; buvid_fp_plain=06201A74-4D4D-4BFD-B069-FED89C254CB9148826infoc; SESSDATA=ba30c108%2C1651584260%2C8b69f%2Ab1; bili_jct=bde1afe7475a50bf6dc17fafafa2f303; DedeUserID=506963849; DedeUserID__ckMd5=6bbdace67271ad46; sid=jwmr0br2; blackside_state=1; rpdid=|(JYl)kkk)mR0J'uYJY|JJu~u; LIVE_BUVID=AUTO5616362112472401; PVID=1; video_page_version=v_old_home; i-wanna-go-back=-1; b_ut=5; fingerprint3=39df0467a8ac842fbec247cd80b4a3a2; fingerprint=12d37e45743125341a6784d0c9a199c4; fingerprint_s=0a74d2020f65156ad539465b08013659; CURRENT_QUALITY=120; CURRENT_BLACKGAP=0; bp_video_offset_506963849=632514752809009200; innersign=1; CURRENT_FNVAL=4048",
              }
    comments = []
    # pn是页码；sort控制排序顺序，1按时间排序，2按热度排序；oid代码视频编号
    # original_url = "https://api.bilibili.com/x/v2/reply?jsonp=jsonp&type=1&oid=752687794&sort=2&pn="
    # plat是页码
    original_url = "https://api.bilibili.com/x/v2/reply/main?jsonp=jsonp&next=1&type=1&oid=752687794&plat="

    for page in range(1, 21):  # 页码这里就简单处理了
        url = original_url + str(page)
        try:
            html = requests.get(url, headers=header)
            data = html.json()
            # pprint.pprint(data)
            if data['data']['replies']:
                for i in data['data']['replies']:
                    comments.append(i['content']['message'])
                print(url)
            if page == 20:
                comments_dict = {'comments': comments}
                save_data(comments_dict)
        except Exception as err:
            print(err)
