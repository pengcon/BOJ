money=int(input())
price_list=list(map(int,input().split()))
up_count=0
down_count=0

junhyun=0
j_money=money
sungmin=0
s_money=money

def junhyun_play(j_money,junhyun):
    for i in range(14):
        buy_count=(j_money//price_list[i])
        j_money=j_money-buy_count*price_list[i]
        junhyun+=buy_count
    return j_money,junhyun


def sungmin_play(s_money,sungmin):
    global up_count
    global down_count
    for i in range(1,14):
        
        if price_list[i-1]<price_list[i]:
            up_count=max(1,up_count+1)
            down_count=0
            
        elif price_list[i-1]>price_list[i]:
            down_count=max(1,down_count+1)
            up_count=0
            
        if up_count>=3 and sungmin>0:
            s_money=s_money+(sungmin*price_list[i])
            sungmin=0
            
        elif down_count>=3:
            buy_count=s_money//price_list[i]
            s_money=s_money-(buy_count*price_list[i])
            sungmin+=buy_count
    return s_money,sungmin

j_money,junhyun = junhyun_play(j_money,junhyun)
s_money,sungmin = sungmin_play(s_money,sungmin)

if j_money+(junhyun*price_list[-1])>s_money+(sungmin*price_list[-1]):
    print("BNP")
elif j_money+(junhyun*price_list[-1])<s_money+(sungmin*price_list[-1]):
    print("TIMING")
else:
    print("SAMESAME")