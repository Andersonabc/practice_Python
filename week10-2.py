"""
#旋轉抽抽樂

小明有個N*M(１≦N≦10,1≦M≦10) 的抽抽樂矩陣, 裡面放著1~9號等獎項,
小明在走樓梯的時候不小心手滑讓抽抽樂滾走，
抽抽樂有三種滾動方式:向右轉90度,向左轉90度,向右轉180度,
請幫助小明找出目前的獎項排列。
輸入說明:
3 3 (矩陣大小為3*3)(數字間有空格)
123 (輸入矩陣內的獎項)(數字之間沒有空格)(數字可重複)
321
456
12321322 (滾動方式 1=:向右轉90度 ,2=向左轉90度, 3=向右轉180度)
輸出說明:
輸出旋轉後的矩陣。(數字間沒有空格)
不合法的輸入則輸出E。
------------測資--------------
input:
3 4
1234
3216
1397
12321233
output:
131
322
913
764
--------------------------------
input
1 10
123456789
3321
output:
E
--------------------------------
input
1 10
1234567893
123321313
output:
1
2
3
4
5
6
7
8
9
3
"""
def f1 (da):
    for i in range (len(da)):
        print(da[i])
def f2(da,x):
    for i in range(x):
        for j in range (len(da)-1,-1,-1):
            print(da[j][i],end='')
        print('')
def f3(da,x):
    a=''
    for i in range(len(da)-1,-1,-1):
        for j in range (x-1,-1,-1):
            print(da[i][j],end='')
        print('')
def f4(da,x):    
    for i in range(x-1,-1,-1):
        for j in range (len(da)):
            print(da[j][i],end='')
        print('')    
def main():
    ww=0;rr=0
    data=[]
    lon=list(map(int,input().split()))
    if len(lon)>2 or lon[0]<1 or lon[0]>10 or lon[1]<1 or lon[1]>10 :
        ww=1
    for i in range (lon[0]):
        data.append(input())    
    rotation=input()  

    for i in range (len(data)) :                  
        if len(data[i])!=lon[1]:
            ww=1
    if ww==1:
        print('E')
    elif ww==0:
        for i in range (len(rotation)):
            if rotation[i]=='1':
                rr+=90
            elif rotation[i]=='2':
                rr+=270
            elif rotation[i]=='3':
                rr+=180
        rr=rr%360
        if rr==0:
            f1(data)
        elif rr==90:
            f2(data,lon[1])
        elif rr==180:
            f3(data,lon[1])
        else:
            f4(data,lon[1])
    
main()