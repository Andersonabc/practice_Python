"""
#線段計算

請算出a,b,c三條線在X軸上所涵蓋的長度(不含重複線段)
例如:a(x1,x2)表示a線段為X軸上點x1到點x2的線
輸入說明:
---------------
-1 (a的x1座標為 -1)
1 (a的x2座標為 1)
0 (b的x1座標為 0)
2 (b的x2座標為 2)
1 (c的x1座標為 1)
3 (c的x2座標為 3)
https://i.imgur.com/3RWOXvp.png
輸出說明:
---------------
4
"""
import math
def cal (a1,a2,b1,b2,c1,c2):
    if(b1<a2 and c1>b2):
        lo=abs(b2-a1+c2-c1)
    elif(b1>a2 and c1<b2):
        lo=abs(a2-a1+c2-b1)
    elif(b1>a2 and c1>b2):
        lo=a2+b2+c2-a1-b1-c1
    else:
        i=max(a1,a2,b1,b2,c1,c2)
        j=min(a1,a2,b1,b2,c1,c2)
        lo=abs(i-j)
    return lo


def main():
    a1=int(input())
    a2=int(input())
    b1=int(input())
    b2=int(input())
    c1=int(input())
    c2=int(input())
    diff=cal (a1,a2,b1,b2,c1,c2)
    print(diff)
    
main()