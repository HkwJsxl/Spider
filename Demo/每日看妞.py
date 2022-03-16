import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

'''
chromeOptions = webdriver.ChromeOptions()
#  设置代理
chromeOptions.add_argument("--proxy-server=http://182.18.83.42:6666")
browser = webdriver.Chrome(chrome_options = chromeOptions)

'''
# https://www.ixigua.com/home/6839565013/?list_entrance=search
url = 'https://www.ixigua.com/embed?group_id=7028605499276788238'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}

# 新建一个浏览器
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url=url)
# 延迟等待
driver.implicitly_wait(10)

info = driver.find_element_by_xpath('//xg-definition/ul/li[1]')
video_url = 'https:' + info.get_attribute('url')

video_data = requests.get(url=video_url, headers=headers).content
with open('video\\每日看妞.mp4', 'wb') as f:
    f.write(video_data)
f.close()
