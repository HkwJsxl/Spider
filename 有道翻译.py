import requests
import hashlib
import time

time_stamp = int(time.time() * 1000)  # 时间戳
key_word = input('要翻译的内容： ')

parse = "fanyideskweb" + key_word + str(time_stamp) + "Ygy_4c=r#e#4EX^NUGUc5"
sign = hashlib.md5(parse.encode('utf-8')).hexdigest()

url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=768727101@10.108.160.105; OUTFOX_SEARCH_USER_ID_NCOO=2054013353.125816; JSESSIONID=aaaNMCJWbF6hYbQYhoA9x; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcKUovbnsSlw8INioA9x; DICT_SESS=v2|pEvQ_ft1pWYfPLTynH6uRzfkfpuPLpK0wyP4YlhLpBRYl0MTS0L6yR6uk4PBkfzY06unHkGP4pZ0PzhLqyn4YM0l5nLzWPMJB0; DICT_LOGIN=1||1646487588375; ___rl__test__cookies=1646487604683',
    'Host': 'fanyi.youdao.com',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
data = {
    'i': key_word,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': time_stamp,
    'sign': sign,
    'lts': time_stamp,
    'bv': '56d33e2aec4ec073ebedbf996d0cba4f',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}
response = requests.post(url=url, headers=headers, data=data).json()
result = response['translateResult'][0][0]['tgt']
print(f'翻译后的内容为: \033[1;33m{result}')
