from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time

f = open('商品.csv', mode='w', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '标题',
    '价格',
    '评论数目',
    '店铺名称',
    '详情页',
])
csv_writer.writeheader()
key = input('输入要搜索的关键字：')
driver = webdriver.Chrome()
driver.get('https://www.jd.com/?country=USA')
# print(driver.page_source)
driver.find_element_by_css_selector('#key').send_keys(key)
driver.find_element_by_css_selector('#key').send_keys(Keys.ENTER)
for page in range(1, 11):
    driver.implicitly_wait(10)
    lst = driver.find_elements_by_css_selector('#J_goodsList > ul > li')
    # print(lst)
    for li in lst:
        title = li.find_element_by_css_selector('.p-name.p-name-type-2 > a > em').text  # 标题
        href = li.find_element_by_css_selector('.p-name.p-name-type-2 a').get_attribute('href')  # 详情页
        price = li.find_element_by_css_selector('.p-price strong i').text  # 价格
        Comment_num = li.find_element_by_css_selector('.p-commit strong a').text  # 评论数目
        shop = li.find_element_by_css_selector('.p-shop span a').text  # 店铺名称
        info_dic = {
            '标题': title,
            '价格': price,
            '评论数目': Comment_num,
            '店铺名称': shop,
            '详情页': href,
        }
        print(info_dic)
        csv_writer.writerow(info_dic)
    print(f'第{page}页已完成'.center(50, '-'))
    driver.find_element_by_css_selector('.pn-next').click()
    time.sleep(1)
driver.quit()
