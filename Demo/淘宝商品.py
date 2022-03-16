import random
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

f = open('商品.csv', mode='w', encoding='utf-8-sig', newline='')
csv_driver = csv.DictWriter(f, fieldnames=['标题', '价格', '销售数量', '店名', '地址', '链接'])
csv_driver.writeheader()

driver = webdriver.Chrome()
# 跳过滑块验证
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                       {'source': '''Object.defineProperty(navigator, 'webdriver', {get:()=>false})'''})
driver.get('https://www.taobao.com/')
driver.implicitly_wait(5)
driver.find_element(by=By.CSS_SELECTOR, value='#q').send_keys('巴黎世家丝袜')
driver.find_element(by=By.CSS_SELECTOR, value='#J_TSearchForm > div.search-button > button').click()
driver.implicitly_wait(5)
driver.find_element(by=By.CSS_SELECTOR, value='#fm-login-id').send_keys('18533538210')
driver.find_element(by=By.CSS_SELECTOR, value='#fm-login-password').send_keys('20020224.')
time.sleep(random.randint(3, 5))
driver.find_element(by=By.CSS_SELECTOR, value='#login-form > div.fm-btn > button').click()
driver.implicitly_wait(5)


def get_content():
    time.sleep(random.randint(3, 5))
    comment = driver.find_elements(by=By.CSS_SELECTOR, value='#mainsrp-itemlist > div > div > div:nth-child(1) > div')
    for value in comment:
        title = value.find_element(by=By.CSS_SELECTOR, value='.pic a img').get_attribute('alt')
        shop = value.find_element(by=By.CSS_SELECTOR, value='.shop > a > span:nth-child(2)').text
        address = value.find_element(by=By.CSS_SELECTOR, value='.row.row-3.g-clearfix .location').text
        price = value.find_element(by=By.CSS_SELECTOR, value='.price.g_price.g_price-highlight strong').text
        num = value.find_element(by=By.CSS_SELECTOR, value='.row.row-1.g-clearfix .deal-cnt').text
        href = value.find_element(by=By.CSS_SELECTOR, value=
        '.ctx-box.J_MouseEneterLeave.J_IconMoreNew > .row.row-2.title a').get_attribute('href')
        data_dict = {
            '标题': title,
            '价格': price,
            '销售数量': num,
            '店名': shop,
            '地址': address,
            '链接': href,
        }
        csv_driver.writerow(data_dict)
        print(data_dict)
    driver.find_element(by=By.CSS_SELECTOR, value='.items .J_Ajax.num.icon-tag').click()


for page in range(1, 11):
    print(f'正在爬取第{page}页'.center(50, '-'))
    get_content()
    time.sleep(random.randint(3, 5))

driver.quit()
