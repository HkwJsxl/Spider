import requests


def get_self(next_cursor):
    url = 'https://weibo.com/tv/api/component?page=%2Ftv%2Fsubbillboard%2F4418219805484551'  # 改
    headers = {
        'cookie': 'SINAGLOBAL=3681016557813.379.1641709685675; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhUshhm5xhVwj.KYpkEU5rP5JpX5KMhUgL.FoMEe0.cS0.EShz2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNeoe4SoM4eoBE; ALF=1674374660; SSOLoginState=1642838660; SCF=Am5tWrFRFjaV0FdzVn2sI81g876ytFtjO8On0nOn3yti9x7t1PLchqaJt1TvkZdQXbFjtLwj35FLHOI0b4nCN1c.; SUB=_2A25M78rUDeRhGeFM6FsX9yfOzz6IHXVvnLscrDV8PUNbmtAKLVbgkW9NQMYwNlJp0qaZZCAVZ1Dj_VS2hMw3zTJp; wvr=6; wb_view_log_7239679242=1536*8641.25; _s_tentry=login.sina.com.cn; UOR=,,www.google.com; Apache=8848911848505.355.1642838668765; ULV=1642838668834:4:4:1:8848911848505.355.1642838668765:1642144448493; webim_unReadCount=%7B%22time%22%3A1642838680970%2C%22dm_pub_total%22%3A3%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A15%2C%22msgbox%22%3A0%7D; TC-V-WEIBO-G0=35846f552801987f8c1e8f7cec0e2230; XSRF-TOKEN=9--ac4s6xzW1wIlspMRtBMRi; WBPSESS=bZXvfyafvVJNryZKScS0OcOCeQdFvfFSt6eOnyRUnJM7V_EuyvC2imXrS2xkpmCZsRs7qFbOMEdm2DfAlVy509NECKTAnyKImci1Z_ZvsKnmWxbJl1S1eE_ZL0u6XU0N',
        'referer': 'https://weibo.com/tv/subbillboard/4418219805484551?cid=4379160563414111',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'x-xsrf-token': '9--ac4s6xzW1wIlspMRtBMRi',
    }
    data = {
        'data': '{"Component_Billboard_Billboardlist":{"cid":"4418219805484551","count":20}}'  # 改
    }
    if next_cursor != 0:
        data = {
            'data': '{"Component_Billboard_Billboardlist":{"cid":"4418219805484551","next_cursor":' + str(  # 改
                next_cursor) + ',"count":20}}'
        }
    if next_cursor == -1:
        return 'over'
    response = requests.post(url=url, headers=headers, data=data).json()
    json_data = response['data']['Component_Billboard_Billboardlist']['list']
    for lst in json_data:
        media_id = lst['media_id']
        headers_1 = {
            'cookie': 'SINAGLOBAL=3681016557813.379.1641709685675; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhUshhm5xhVwj.KYpkEU5rP5JpX5KMhUgL.FoMEe0.cS0.EShz2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNeoe4SoM4eoBE; ALF=1674374660; SSOLoginState=1642838660; SCF=Am5tWrFRFjaV0FdzVn2sI81g876ytFtjO8On0nOn3yti9x7t1PLchqaJt1TvkZdQXbFjtLwj35FLHOI0b4nCN1c.; SUB=_2A25M78rUDeRhGeFM6FsX9yfOzz6IHXVvnLscrDV8PUNbmtAKLVbgkW9NQMYwNlJp0qaZZCAVZ1Dj_VS2hMw3zTJp; wvr=6; wb_view_log_7239679242=1536*8641.25; _s_tentry=login.sina.com.cn; UOR=,,www.google.com; Apache=8848911848505.355.1642838668765; ULV=1642838668834:4:4:1:8848911848505.355.1642838668765:1642144448493; webim_unReadCount=%7B%22time%22%3A1642838680970%2C%22dm_pub_total%22%3A3%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A15%2C%22msgbox%22%3A0%7D; TC-V-WEIBO-G0=35846f552801987f8c1e8f7cec0e2230; XSRF-TOKEN=9--ac4s6xzW1wIlspMRtBMRi; WBPSESS=bZXvfyafvVJNryZKScS0OcOCeQdFvfFSt6eOnyRUnJM7V_EuyvC2imXrS2xkpmCZsRs7qFbOMEdm2DfAlVy509NECKTAnyKImci1Z_ZvsKnmWxbJl1S1eE_ZL0u6XU0N',
            'referer': f'https://weibo.com/tv/show/1034:{media_id}?mid={media_id}',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'x-xsrf-token': '9--ac4s6xzW1wIlspMRtBMRi',
        }
        data_num = '{"Component_Play_Playinfo":{"oid":"1034:' + str(media_id) + '"}}'
        data_1 = {
            'data': data_num
        }
        url_1 = f'https://weibo.com/tv/api/component?page=/tv/show/1034:{media_id}'
        response_1 = requests.post(url=url, headers=headers_1, data=data_1).json()
        urls = response_1['data']['Component_Play_Playinfo']['urls']
        title = response_1['data']['Component_Play_Playinfo']['title']
        video_url = 'https:' + urls[list(urls.keys())[0]]
        print(title, video_url)
        # video_data = requests.get(url=video_url).content
        # with open(f'video//{title}.mp4', mode='wb') as f:
        #     f.write(video_data)
        # print('下载完成')
    next_cursor = response['data']['Component_Billboard_Billboardlist']['next_cursor']
    get_self(next_cursor)


get_self(0)
