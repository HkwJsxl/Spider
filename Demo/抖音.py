import requests
import re
from selenium import webdriver
import time


def drop_down():
    for x in range(1, 50, 2):
        time.sleep(0.5)
        j = x / 9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)
        

driver = webdriver.Chrome()
driver.get('https://www.douyin.com/user/MS4wLjABAAAAJqTyV9DKLyl-0JoeAU1BiZW2PWyfBX17JyeXK1YmE-w')
drop_down()
driver.implicitly_wait(10)
lst = driver.find_elements_by_css_selector('.ECMy_Zdt')
for li in lst:
    href = li.find_element_by_css_selector('a').get_attribute('href')
    title = li.find_element_by_css_selector('img').get_attribute('alt')
    # url = 'https://www.douyin.com/video/7067102667620764932'
    headers = {
        'cookie': 'douyin.com; ttcid=c160638113c04e659358b9c4c056d21419; ttwid=1%7CcYI5JJKscIiLCwfVqWndjShDSvygmqHz9wdGzQdR47Y%7C1639612589%7C8452d668769dd4a76a51d2000b4cbb924132f19da177840d0b9b27d06ccc947b; MONITOR_DEVICE_ID=d07908c9-175c-462e-b62a-12dcf870448e; MONITOR_WEB_ID=e4c51b1f-004a-4456-88b3-f2cdef2ed3ec; MONITOR_WEB_ID=214220dd-be3c-4b04-a824-143713200a47; n_mh=k4a5qyPQcOO7npBInQOrH7MtydsD9Ufh8wwDI3kXmV8; d_ticket=467d1aba05d98396698627ad85e76e2edb09b; _tea_utm_cache_6383=undefined; douyin.com; AB_LOGIN_GUIDE_TIMESTAMP=1645618381647; passport_csrf_token_default=61930460f0a08ba0621c3d27b2eee7e0; passport_csrf_token=61930460f0a08ba0621c3d27b2eee7e0; _tea_utm_cache_1300=undefined; s_v_web_id=verify_kzzip362_u6vkvati_1uln_4ghl_BSaw_309nBe5kPKAl; sso_uid_tt=c02b57a9358986de4e88c82e491b7199; sso_uid_tt_ss=c02b57a9358986de4e88c82e491b7199; toutiao_sso_user=b8f5d374e865d3b959288b3130e170e4; toutiao_sso_user_ss=b8f5d374e865d3b959288b3130e170e4; sid_ucp_sso_v1=1.0.0-KDRkZGVhZjdhZGIxM2Y2ODQxMTE4Y2I3NzY1OThmYzY0NmIyM2FkZTUKHQjwo-D4lAMQx8rYkAYY7zEgDDDhh8PgBTgGQPQHGgJsZiIgYjhmNWQzNzRlODY1ZDNiOTU5Mjg4YjMxMzBlMTcwZTQ; ssid_ucp_sso_v1=1.0.0-KDRkZGVhZjdhZGIxM2Y2ODQxMTE4Y2I3NzY1OThmYzY0NmIyM2FkZTUKHQjwo-D4lAMQx8rYkAYY7zEgDDDhh8PgBTgGQPQHGgJsZiIgYjhmNWQzNzRlODY1ZDNiOTU5Mjg4YjMxMzBlMTcwZTQ; passport_auth_status=23454b0e26b05ff7a749938f4eec8705%2C; passport_auth_status_ss=23454b0e26b05ff7a749938f4eec8705%2C; sid_guard=353e5c62b1e64a344e147ba7fd908e50%7C1645618505%7C5183998%7CSun%2C+24-Apr-2022+12%3A15%3A03+GMT; uid_tt=40da9a81a53682d9dd54ba39e2c61e80; uid_tt_ss=40da9a81a53682d9dd54ba39e2c61e80; sid_tt=353e5c62b1e64a344e147ba7fd908e50; sessionid=353e5c62b1e64a344e147ba7fd908e50; sessionid_ss=353e5c62b1e64a344e147ba7fd908e50; sid_ucp_v1=1.0.0-KDU2MWZkOGZlZjYzNjRlMjg4Y2RkZTVlY2ViYzZmODQzODc5ZTRiMGIKFwjwo-D4lAMQycrYkAYY7zEgDDgGQPQHGgJsZiIgMzUzZTVjNjJiMWU2NGEzNDRlMTQ3YmE3ZmQ5MDhlNTA; ssid_ucp_v1=1.0.0-KDU2MWZkOGZlZjYzNjRlMjg4Y2RkZTVlY2ViYzZmODQzODc5ZTRiMGIKFwjwo-D4lAMQycrYkAYY7zEgDDgGQPQHGgJsZiIgMzUzZTVjNjJiMWU2NGEzNDRlMTQ3YmE3ZmQ5MDhlNTA; odin_tt=7e109d3cfa41c0a81c084e5c4f00666316b8e0abcbc4c7b8fe06246afa8c72268801e91b73f2dbc8c1595e78ba1f64b75d192744a2563cc432a38f68e11ad3fd; __ac_nonce=06216254a0033651f2776; __ac_signature=_02B4Z6wo00f01jEAtbgAAIDCsQJP-XUUBkoxJLEAAO5kzYtPRmQqrSwluHPMWf3OUBOVLdHN-9CX2cWQvTL2HDApZyTMPQPRzBfdw2Fh6Hk-DfPUF8BwW1KIO5kCEiFf0mafyDT1N49bV3hIbd; FOLLOW_LIVE_POINT_INFO=MS4wLjABAAAAguZ-OiYCFtnBBDcnjgnkkSUk54Sahi-1ovk6WU_zoDI%2F1645632000000%2F0%2F1645618509199%2F0; msToken=oGXEskKMATKtLd44szv7QO5_jVXAhfVko1KVMFauQK-GICrWpg0_WM5j-j3iQG6Up7hewWYzXT6lVIe6CDGmlwS_9eaCksgNNeUYak4OVelQPvZZnZ5SQSLQZ2U=; tt_scid=6FRp0aIrCX9nx4He5STu3ZjF6SRWF9P0f8wksrlCoUan3JOx2kvy7Vh5qw8B8z.562f2; IS_HIDE_THEME_CHANGE=1; THEME_STAY_TIME=299574; pwa_guide_count=3; home_can_add_dy_2_desktop=1; msToken=XOhrEKIJOi8jK77NBWPdzz3yfCEOTTJAs7WU1mp3AcYv3-eQllrfa8P7-7tsKCHoKJg-Ozp3qs2lKe9aaiZw-Nmcj1WSDITsDDWtW4fPWLE_L3inWfZvHN_vbA==',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    }
    res = requests.get(url=href, headers=headers).text
    # title = re.findall('<title data-react-helmet="true">(.*?)</title>', res)[0]
    title = re.sub('r[\|/":*?<>]', '', title)
    video_url = re.findall('src(.*?)vr%3D%', res)[0]
    video_url = requests.utils.unquote(video_url).replace('":"', 'https:')  # 解码
    # video_url = requests.utils.quote('美女')  # 编码
    print(video_url)
    video_content = requests.get(url=video_url, headers=headers).content
    # with open('video\\' + title + '.mp4', mode='wb') as f:
    #     f.write(video_content)
driver.quit()
