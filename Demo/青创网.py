from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time


def drop_down():
    for x in range(1, 10, 2):
        time.sleep(0.5)
        j = x / 9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


f = open('1.csv', mode='w', encoding='utf-8_sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '名称',
    '价格',
    '商品满意度',
    '店铺名称',
    '地址',
    '详情页',
])
csv_writer.writeheader()
key = input('输入要搜索的关键字：')
driver = webdriver.Chrome()
driver.get('https://www.17qcc.com/?ReturnUrl=%2F')
driver.find_element(by=By.CSS_SELECTOR, value='#keywords').send_keys(key)
driver.find_element(By.CSS_SELECTOR, value='#keywords').send_keys(Keys.ENTER)

for page in range(1, 11):
    driver.implicitly_wait(10)
    drop_down()
    lst = driver.find_elements(By.CSS_SELECTOR, value='#productlist li')
    for li_text in lst:
        name = li_text.find_element(By.CSS_SELECTOR, value='.rowtitle a').text  # 名称
        price = li_text.find_element(By.CSS_SELECTOR, value='.brprice span').text  # 价格
        viewpay = li_text.find_element(By.CSS_SELECTOR, value='.brprice .viewpay').text  # 商品满意度
        shop = li_text.find_element(By.CSS_SELECTOR, value='.shop a').text  # 店铺名称
        address = li_text.find_element(By.CSS_SELECTOR, value='.radd').get_attribute('title')  # 地址
        info_page = li_text.find_element(By.CSS_SELECTOR, value='.rowtitle a').get_attribute('href')  # 详情页
        lst_dic = {
            '名称': name,
            '价格': price,
            '商品满意度': viewpay,
            '店铺名称': shop,
            '地址': address,
            '详情页': info_page,
        }
        print(lst_dic)
        csv_writer.writerow(lst_dic)
    print(f'第{page}页已完成'.center(50, '-'))
    page += 1
    driver.find_element(By.CSS_SELECTOR, value='.next').click()
    time.sleep(1)

driver.quit()
