import pprint

# 1.发送请求
import requests  # pip install requests
import re  # 内置模块
import json  # 内置模块
import csv  # 内置模块
import time
import parsel

# 打开文件
f = open('招聘.csv', mode='w', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['标题', '公司名', '薪资', '福利待遇', '招聘信息'])
# 写入表头
csv_writer.writeheader()

# for 循环 遍历
for page in range(1, 21):
    time.sleep(1)
    # format()  字符串格式化的方法
    print(f'==========================现在正在爬取第{page}页的招聘信息============================')
    # 要爬取的url地址
    url = f'https://search.51job.com/list/010000%252C020000%252C030200%252C040000,000000,0000,00,9,99,python,2,{page}.html'
    # 请求头
    headers = {
        'Cookie': '_uab_collina=164577710210472950591185; guid=6271b56c2b111cfd69dbc8db995767ce; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60010000%2C020000%2C030200%2C040000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60010000%2C020000%2C030200%2C040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; acw_tc=76b20ff016457788958933024e557eec658be0cf3ecce91471228c86495fbc; acw_sc__v2=621897cf6f243e630ff9fdb66a022f1407763df3; _ujz=MjA0NzYzMzc2MA%3D%3D; ps=needv%3D0; slife=lowbrowser%3Dnot%26%7C%26lastlogindate%3D20220225%26%7C%26securetime%3DAz8EMVIwVDUAZQ43WmhcN1FnAT4%253D; track=registertype%3D1; 51job=cuid%3D204763376%26%7C%26cusername%3DJ%252BLVOIcCZOgvJeNl14Ep1IYv5S3q5dj2v1senI6THSY%253D%26%7C%26cpassword%3D%26%7C%26cname%3DLMkgCyw6KfW%252FPLIJkfpMqg%253D%253D%26%7C%26cemail%3D%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0q%252FS57ImgqWc%26%7C%26cconfirmkey%3D%25241%2524L7k7r9OT%2524mTWbBmldkDwP9S.mfE2%252FN.%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D0%26%7C%26cnamekey%3D%25241%252442isDzbn%2524Q0lb0CETMBpzNUGmtejKV0%26%7C%26to%3De348df1dddab45183b4c80ec39f2299062189871%26%7C%26; privacy=1645779177; ssxmod_itna2=YqGx9DgDnD2DBDIgxlf=OKPAK0=Cnqw9DnnGwKikE8ttDlxxrDj+436KhKudid3AawuNY4Ernv280l=BY+sNL2GGnwoODZ8==VnRlMrKie5KQ6x8Ql4=wN6N4qZGzUM=p9Cg2Nu5=QcWw4iQikC7mTfrqqhYPxYmIQE=i1Zrgp1lbi/ApYkbwTQ8a+z9TEQ8BT+FaC+Sa=/Ah=+Ee61K8i=6fxS1Pi/+d0roljM+cXNhhOxMow=gCGhfjeXeMTzOk=iY6F5ken9GmcE=3gzs/BqSLFNxuTSKq=Z98iCQ/jrbWir4uj=SLMrK8ePSgoLBUgoX/ZqqAPGZD4D=to+I1Xtoiqgm7ZICYpb1N+1+i2GY2KvirMopWbiEQLtEbvWf8YR7gG2cEH9dApABgwYoLG1rnPd0rtCrefmwpgK97eNgPyADgPIvfiv=cGWqvRYsZNsPe6epXbeSgcU4wkSUHlcAY02EF4I4DQI87fGAxeQiXjdkDB99dbIqzX2VnDeYRs6xtQGhfbzdg+V55WGsc+e+Whr+10dyIpxI2Wajvv5eD08DiQLjwtnq4QGmRG4nKRmBNcAakDtDoLOD=YD=; ssxmod_itna=YqGx9DgDnD2DBDIgxlf=OKPAK0=Cnqw9DnnGw2PDs+TDSxGKidDqxBnmj+qho2GK4tBA37oriQA4p4F8bf+qwIeWcw2GoDU4i8DCqbFjTDem=D5xGoDPxDeDADYoXDAqiOD7qDd6vs5VkDYPDEnKDaxDbDiWkvxGCDeKD0xqHDQKDucI+CgA1Fb5e3RDq6xG1740H8m3x6oEfjbDs333ERQD5DBbxSRDxeALqtlnGfCKDXhQDvhv1ZgppS4vsg=Ao==G4TnuoTAxdbB04emn9=Q45qA6KE7Gx+Qmxq1rZQ0=DiZMZtQx44D=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    # 模拟浏览器发送请求
    response = requests.get(url=url, headers=headers)
    selector = parsel.Selector(response.text)
    # print(response.text)

    # 对数据进行解析 提取自己想要数据内容
    html_data = re.findall('window.__SEARCH_RESULT__ = (.*?)</script>', response.text)[0]
    # print(html_data)
    # 字符串转字典 json数据
    # json_data = json.loads(html_data)
    # pprint.pprint(json_data)
    json_data = json.loads(html_data)['engine_jds']
    # pprint.pprint(json_data)
    # 遍历 列表里面每一个元素 分别取值
    for index in json_data:
        # 根据字典取值的方式,根据的一个键取它的值
        title = index['job_name']  # 标题
        company_name = index['company_name']  # 公司名
        money = index['providesalary_text']  # 薪资
        jobwelf = index['jobwelf']  # 福利待遇
        job_info = '|'.join(index['attribute_text'])  # 招聘信息
        # 用一个字典的数据容器 把这些存起来
        dit = {
            '标题': title,
            '公司名': company_name,
            '薪资': money,
            '福利待遇': jobwelf,
            '招聘信息': job_info,
        }
        # 保存数据
        csv_writer.writerow(dit)
        print(title, company_name, money, jobwelf, job_info)
    # exit()
