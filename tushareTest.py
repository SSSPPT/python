import tushare as ts
ts.set_token('94dcbb0c07130fa3555018f3a832f753385f041d1174886a405ec81a')
pro = ts.pro_api()
df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
print(df)
