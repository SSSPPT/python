import tushare as ts
import util
import strategy
ts.set_token('94dcbb0c07130fa3555018f3a832f753385f041d1174886a405ec81a')
pro = ts.pro_api()
df = pro.daily(ts_code='002342.SZ', start_date='20220502', end_date='20220818')
aa = list(df['trade_date'])
bb = list(df['open'])
cc = list(df['high'])
dd = list(df['low'])
datas = list(reversed(list(df['trade_date'])))
opens = list(reversed(list(df['open'])))
highs = list(reversed(list(df['high'])))
lows = list(reversed(list(df['low'])))
closes = list(reversed(list(df['close'])))
qk = 68.55
qd = 58.85
for i in range(len(datas)):
    kdj = {'k':None,'d':None,'j':None}
    data = datas[i]
    try:
        datasss = datas[i-8:i+1]
        c9 = closes[i-8:i+1]
        h9 = highs[i-8:i+1]
        l9 = lows[i-8:i+1]
        if((len(c9)<9)):
            print(data, '-', kdj['k'], '-', kdj['d'], '-', kdj['j'])
            continue
        kdj = util.get_kdj(c9,h9,l9,qk,qd);
        qk = kdj['k']; qd = kdj['d'];
    except TypeError:
        1+1
    print(data,'-',kdj['k'],'-',kdj['d'],'-',kdj['j'])


kdj = util.get_kdj(c9,h9,l9,qk,qd);







