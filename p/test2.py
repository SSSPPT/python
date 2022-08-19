from hyper.contrib import HTTP20Adapter  # 帮助解析http2.0的帮手
import requests
import json
import ast

url = 'https://stock.xueqiu.com/v5/stock/quote.json?symbol=SZ002340&extend=detail'
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
res = requests.get(url=url,headers=hdr)
print(res.text)
j = json.loads(res.text)
aa=j.get('data')
bb=aa.get('quote')
print(j['data']['quote']['current'])
print(j['data']['quote']['total_shares'])
# sessions = requests.session()			# 实例化一个可以定制的requests.session类
# sessions.mount(url, HTTP20Adapter())	# 指定对http2.0中':'header的解码
# res = sessions.post(url, headers=hdr, data=dts)  # 接下来与原有requests的使用方式一致，不再报错
# print(res)