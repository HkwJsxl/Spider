from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time


def drop_down():
    for x in range(1, 10, 2):
        time.sleep(0.5)
        j = x / 9
        # document.documentElement.scrollTop  # 指定滚动条的位置
        # document.documentElement.scrollTop  # 获取浏览器页面的最大高度
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
# print(driver.page_source)
driver.find_element_by_css_selector('#keywords').send_keys(key)
driver.find_element_by_css_selector('#keywords').send_keys(Keys.ENTER)
# driver.implicitly_wait(10)  # 隐式等待

for page in range(1, 11):
    driver.implicitly_wait(10)
    drop_down()
    lst = driver.find_elements_by_css_selector('#productlist li')
    # print(lst)
    for li_text in lst:
        # print(li_text)
        name = li_text.find_element_by_css_selector('.rowtitle a').text  # 名称
        price = li_text.find_element_by_css_selector('.brprice span').text  # 价格
        viewpay = li_text.find_element_by_css_selector('.brprice .viewpay').text  # 商品满意度
        shop = li_text.find_element_by_css_selector('.shop a').text  # 店铺名称
        address = li_text.find_element_by_css_selector('.radd').get_attribute('title')  # 地址
        info_page = li_text.find_element_by_css_selector('.rowtitle a').get_attribute('href')  # 详情页
        # print(name, price, viewpay, shop, address, info_page)
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
    driver.find_element_by_css_selector('.next').click()
    time.sleep(1)

driver.quit()
