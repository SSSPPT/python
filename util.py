
#e.getHigh().subtract(e.getNow()).divide(e.getHigh().subtract(e.getLow()),4,BigDecimal.ROUND_HALF_UP).multiply(BigDecimal.valueOf(100)).doubleValue();
def get_avg(data,b,excursion):
    a = list(data['close'])
    n = a[0+excursion:b+excursion]
    f = round(sum(n) / b, 2)
    return f

def get_wr(a,b,excursion):
    close,high,low = 0,0,0
    if(len(a)<b):
        return None
    for i in range(b):
        if(i==0):
            i = excursion + i;b = b + excursion
        col = a.iloc[i]
        c,h,l = col['close'],col['high'],col['low']
        if(c==None):
            b=b+1
        if i == 0+excursion:
            close = c;low = l
        high = h if h > high else high
        low = l if l < low else low
    return round((high-close)/(high-low)*100,2)


def get_kdj(c,h,l,qk,qd):
    close = c[8]
    hig = max(h)
    low = min(l)
    print(close)
    rsv = (close-low)/(hig-low)*100
    k = round(2 / 3 * qk + 1 / 3 * rsv,2)
    d = round(2 / 3 * qd + 1 / 3 * k,2)
    j = round(3*k-2*d,2)
    return {'k':k,'d':d,'j':j}







