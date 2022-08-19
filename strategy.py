import util
import requests
import json
def is_pass(data):
    if(len(data)<60):
        return -1
    vra1 =util.get_wr(a=data,b=6,excursion=0)
    vra2 =util.get_wr(a=data,b=10,excursion=0)
    vrb1 = util.get_wr(a=data, b=6, excursion=1)
    vrb2 = util.get_wr(a=data, b=10, excursion=1)
    vrc1 = util.get_wr(a=data, b=6, excursion=2)
    vrc2 = util.get_wr(a=data, b=10, excursion=2)
    if((vra1 < 20 or vra2 <20) and (vrb1 > 20 and vrb2 >20) and (vrc1 > 20 or vrc2 >20)):
        avg1 = util.get_avg(data=data, b=60, excursion=0)
        avg2 = util.get_avg(data=data, b=60, excursion=1)
        return 1 if avg1 > avg2 else 0
    return -1

def is_gt_hundred(code):
    code = code[0:-3]
    c = 'SH' if code.startswith('6') else 'SZ'
    url = 'https://stock.xueqiu.com/v5/stock/quote.json?symbol='+ c + code + '&extend=detail'
    hdr = {
        'authority': 'stock.xueqiu.com',
        'method': 'GET',
        'path': '/v5/stock/quote.json?symbol=SZ002340&extend=detail',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'xq_a_token=28ed0fb1c0734b3e85f9e93b8478033dbc11c856; xqat=28ed0fb1c0734b3e85f9e93b8478033dbc11c856; xq_r_token=bf8193ec3b71dee51579211fc4994d03f17c64ac; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY2MzExMzIyMSwiY3RtIjoxNjYwNzM1NTg1NTM5LCJjaWQiOiJkOWQwbjRBWnVwIn0.Y35DxdvMYYh3qWu9d-YVVn4IHnQEYhZHdCFRFRuBiEjweCHI02eArL9yBJSBhjpT-esmItcxLA7c3eogRJ4HHfdLtzHYywLk3QVC6tiKMhcHqSBtOXjiXiQQ2B6vc8G2pKRRvsNIFn4HxG6d9Mkbb7eKkdw05dU8dsU_D_sYYDgNiFBVdL5NDgAHa24n-f_tOJSepPA3PZrRBHxiYqBny05XEoJw9i2N2cqrK0BZ0TObefmXB2RyiVfrdBLqJEIItGc674FNG-xHYu8C_xbdiIyAwm0wCMeBHEz4j3CiwlxnRFNx6pq6Dzq88stfz7-Wyj0OrRYXR6h0H0DM3N4c_Q; u=391660735643644; Hm_lvt_1db88642e346389874251b5a1eded6e3=1660735645; device_id=fdaa8483136c5be67b231cf75c2e1bf4; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1660735667',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    }  # 这里根据我们的目标网页填写相应的header，冒号直接原样保留
    dts = {}  # 这里根据我们的页面需要和请求类型发送data
    res = requests.get(url=url, headers=hdr)
    m = json.loads(res.text)
    c = m['data']['quote']['current'];t = m['data']['quote']['total_shares']
    tt = c * t
    b = tt >10000000000
    if(b):
        print(code,'--',round(tt/100000000,2))
    return b