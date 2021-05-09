"""
#分數四則計算

(若為 C 語言此題不使用陣列，必須使用指標)
此題自訂 add function，計算兩個分數相加。
function input
--------------------
n1: 第一個數的分子
d1: 第一個數的分母
n2: 第二個數的分子
d2: 第二個數的分母
function output
------------------------------
numerator: 相加結果的分子
deniminator: 相加結果的分母
此題自訂multiply function 定義，計算兩個分數相乘。
function input
--------------------
n1: 第一個數的分子
d1: 第一個數的分母
n2: 第二個數的分子
d2: 第二個數的分母
function output
------------------------------
numerator: 相乘結果的分子
deniminator: 相乘結果的分母
--------------------
輸入說明:
----------------------------
輸入二行，每一行代表一個分數
----------------
輸出說明:
---------------------------
輸出分數相加結果
輸出分數相減結果
輸出分數相乘結果
輸出分數相除結果
若有輸入分數的分母或分子為0，則輸出ERROR。
若分數大於1，則分數部分要加括號，如一又六分之一輸出為1(1/6)
若為負數，負號在最前面。
若輸出為0，則顯示0
輸出的結果必須化簡為最簡分數
----------------
Sample input:
----------------
1/2
2/3
----------------
Sample output:
----------------
1(1/6)
-1/6
1/3
3/4
----------------
Sample input:
----------------
0/2
2/3
----------------
Sample output:
----------------
ERROR
ERROR
ERROR
ERROR
"""

def a(m,n):
    while (m!=0 and n!=0):
        if m>n:
            m=m%n
        else:
            n=n%m
            
    if m==0:
        return n
    elif n==0:
        return m
    else:
        return 0

def output(son,mom,stt):
    if son > mom :
        ans=son//mom
        son=son%mom   
        if son!=0:
            print('%s%d(%d/%d)' %(stt,ans,son,mom))
        else:
            print('%s%d' %(stt,ans))
    elif son==mom:
        print('%s%d' %(stt,son//mom))
    elif son<mom:
        if son!=0:
            print('%s%d/%d' %(stt,son,mom))
        else:
            print('0')

def min(x,y):
    stt=''
    if (int(x[0])/int(x[1])-int(y[0])/int(y[1]))<0:
        stt='-'    
    mom=abs(int(x[1])*int(y[1]))
    son=abs(int(x[0])*int(y[1])-int(y[0])*int(x[1]))
    qq=a(son,mom)
    if qq !=0 :
        son/=qq
        mom/=qq
    output(son,mom,stt)
            
        
def ad (x,y):
    stt=''
    if (int(x[0])/int(x[1])+int(y[0])/int(y[1]))<0:
        stt='-'
    mom=abs(int(x[1])*int(y[1]))
    son=abs(int(x[0])*int(y[1])+int(y[0])*int(x[1]))
    qq=a(abs(son),mom)
    if qq !=0 :
        son/=qq
        mom/=qq
    output(son,mom,stt)
        
def mult (x,y):
    stt=''
    if (int(x[0])/int(x[1])*int(y[0])/int(y[1]))<0:
        stt='-'
    son=abs(int(x[0])*int(y[0]))
    mom=abs(int(x[1])*int(y[1]))
    qq=a(abs(son),mom)
    if qq !=0 :
        son/=qq
        mom/=qq
    output(son,mom,stt)
def divi (x,y):
    stt=''
    if (int(x[0])/int(x[1])*int(y[0])/int(y[1]))<0:
        stt='-'
    son=abs(int(x[0])*int(y[1]))
    mom=abs(int(x[1])*int(y[0]))
    qq=a(abs(son),mom)
    if qq !=0 :
        son/=qq
        mom/=qq
    output(son,mom,stt)

def main():
    a=input()
    a1=a.split('/')
    b=input()
    b1=b.split('/')
    
    if a1[0]=='0' or a1[1]=='0' or b1[0]=='0' or b1[1]=='0':
        for i in range (4):
            print('ERROR')
    else:
        ad(a1,b1)
        min(a1,b1)
        mult(a1,b1)
        divi(a1,b1)
    
main()
    