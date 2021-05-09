"""
#計算價格

A、B、C三本書價格及折扣表如下：
定價   1~10本 11~20本 21~30本 31本以上
A 380  原價   打9折   打8.5折 打8折
B 1200 原價   打9.5折 打8.5折 打8折
C 180  原價   打8.5折 打8折   打7折
有一顧客欲購買A：ｘ本、B：ｙ本、C：ｚ本（ｘ、ｙ、ｚ為使用者輸入），請計算需花費多少錢？
例如：
A購買6本 B購買12本 C購買30本
6*380+12*1200*0.95+30*180*0.8
=20280
輸入說明：
---------------
A書本數量，整數
B書本數量，整數
C書本數量，整數
輸出說明：
---------------
費用，整數
print("%d" %x);
測試案例(Test Case)資料：
Input：
6
12
30
Output：
20280
"""
def cal (a, b, c):
    if(a<=10):
        i=380*a
    elif(a>10 and a<=20):
        i=380*0.9*a
    elif(a>20 and a<=30):
        i=380*0.85*a
    else:
        i=380*0.8*a
        
    if(b<=10):
        j=1200*b
    elif(b>10 and b<=20):
        j=1200*0.95*b
    elif(b>20 and b<=30):
        j=1200*0.85*b
    else:
        j=1200*0.8*b
        
    if(c<=10):
        k=180*c
    elif(c>10 and c<=20):
        k=180*0.85*c
    elif(c>20 and c<=30):
        k=180*0.8*c
    else:
        k=180*0.7*c
    return i,j,k

        
def output(a, b, c):
    x=int(a+b+c)
    print("%d"  %x)
    
def main():
    a=int(input())
    b=int(input())
    c=int(input())
    a,b,c=cal (a, b, c)
    output(a, b, c)
    
main()