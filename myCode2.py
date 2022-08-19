import tushare as ts
import strategy
ts.set_token('94dcbb0c07130fa3555018f3a832f753385f041d1174886a405ec81a')
pro = ts.pro_api()

cods = pro.stock_basic(list_status='L')
col = list(cods['ts_code'])
first = []
second = []
for i in range( len(col)):
    code  = col[i]
    print(i,"-",code)
    # total_mv = pro.bak_daily(ts_code=code, trade_date='20220816')['total_mv'][0]
    # if(total_mv<100):
    #     continue
    if(code.startswith('688')):
        continue
    df = pro.weekly(ts_code=code, start_date='20210401', end_date='20220818')
    passs = strategy.is_pass(df);
    if(passs == 0 ):
        second.append(code)
    elif(passs == 1 ):
        print('--------------------------------------',code)
        if strategy.is_gt_hundred(code):
            first.append(code)

print(len(second))
print(second)
print(len(first))
print(first)


