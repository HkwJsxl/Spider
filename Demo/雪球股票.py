import requests
import csv

with open('雪球股票.csv', 'w', encoding='utf-8-sig', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['股票代码', '股票名称', '当前价', '涨跌额', '涨跌幅', '年初至今', '成交量', '成交额', '换手率', '市盈率(TTM)', '股息率', '市值'])
for page in range(1, 101):
    print(f'正在打印第{page}页'.center(50, '-'))
    url = f'https://xueqiu.com/service/v5/stock/screener/quote/list?page={page}&size=30&order=desc&orderby=percent&order_by=percent&market=US&type=us&_=1647409102757'
    headers = {
        'Cookie': 'device_id=fc679d5783b907140de7764060aabbbe; acw_sc__v2=62316d5f472722f4a8617a9801bc4911677e12cd; s=cv11xxty3c; remember=1; xq_a_token=f4cd247f19b8b75fc47da7144729b5073d2f582b; xqat=f4cd247f19b8b75fc47da7144729b5073d2f582b; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjUyNTI1NzYxMjksImlzcyI6InVjIiwiZXhwIjoxNjQ5OTk4NDc2LCJjdG0iOjE2NDc0MDY0NzY3NTAsImNpZCI6ImQ5ZDBuNEFadXAifQ.UonyZX1WlQEcwPxSasL9XQkrjYff7uzXP4CYJAM3R0eXAMCpvOPF4G25VT5k8T2oV9ONFDRIfXirV858nfqNHJsjEB0mWQZTnIH-Mbmv3t6rIj_-NggYf2Zvy3S3kHzwxdgDmAd0hIFMCrf_g79qnP1paBnFOvydayUAKnyQpgOb793CTGGtHuqDzUZP9I86wp6lQ26OmcGt8lxBQ_Itwi4FgfCMf74G2Wjc_gE68wMOc_bvsG8cReg4HgWfD4GMAeoNDg4kO-I6lQ-bZYjOtE1TePV7kmKZ358U_8Lq_55zdgejz1pfNszYi511In3Q9OWnmpr4HET_6-oMYoA0kg; xq_r_token=3ae607b89b9b1c5016b7a01c2f4e8e0158d5f40f; xq_is_login=1; u=5252576129; snbim_minify=true; bid=88cd59dae612499ef86cc7e1340dcac9_l0t3b27q; acw_tc=2760827116474087781968245e14418bbd619efb0b07634b43ad737856a6eb',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    response = requests.get(url, headers=headers).json()
    for lists in response['data']['list']:
        symbol = lists['symbol']
        name = lists['name']
        current = lists['current']
        chg = lists['chg']
        percent = str(lists['percent']) + '%'
        current_year_percent = str(lists['current_year_percent']) + '%'
        volume = lists['volume']
        amount = lists['amount']
        turnover_rate = lists['turnover_rate']
        pe_ttm = lists['pe_ttm']
        dividend_yield = lists['dividend_yield']
        market_capital = lists['market_capital']
        print(symbol, name, current, chg, percent, current_year_percent, volume, amount, turnover_rate, pe_ttm,
              dividend_yield, market_capital)
        with open('雪球股票.csv', 'a', encoding='utf-8-sig', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(
                [symbol, name, current, chg, percent, current_year_percent, volume, amount, turnover_rate, pe_ttm,
                 dividend_yield, market_capital])
