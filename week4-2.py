  
"""
#印圖形

請使用 while loop或for loop，
請使用 function。
第一個輸入意義為選擇三種圖形:
1 三角形方尖方面向右邊
2 三角形方尖方面向左邊
3 菱形
第二個輸入意義為畫幾行
(奇數，範圍為 3,5,7,9,....,21)
input
1 (第一種圖形，三角形尖方面向右邊)
9 (共 9 行)
--------------------------
output
*
**
***
****
*****
****
***
**
*
---------------------------
input
2 (第二種圖形，三角形尖方面向左邊)
5 (共 5 行)
---------------------------
output
..*
.**
***
.**
..*
--------------------------
input
3 (第三種圖形: 菱形 )
3 (共 3 行數)
輸出
.*
***
.*
"""
def right(b):
    a=b//2
    for i in range (1,a+2):
        for j in range (0,i,1):
            print("*",end='')
        print('')
    for i in range (a):
        for j in range (a-i,0,-1):
            print("*",end='')
        print('')
            
def left(b):
    b=b//2
    for i in range (b+1):
        for j in range (b-i):
            print(".",end='')
        for k in range (i+1):
            print("*",end='')
        print('')
    for i in range (b):
        for j in range (i+1):
            print(".",end='')
        for k in range (b-i):
            print("*",end='')
        print('')
            
def mid (b):
    b=b//2
    for i in range (b+1):
        for j in range (b-i):
            print(".",end='')
        for k in range (1+2*i):
            print("*",end='')
        print('')
    for i in range (b):
        for j in range (i+1):
            print(".",end='')
        for k in range (2*b-(2*i+1)):
            print ("*",end='')
        print('')

def main ():
    a=input()
    b=int(input())
    if(a=="1"):
        right(b)
    elif(a=="2"):
        left(b)
    elif(a=="3"):
        mid(b)
    else:
        print("error")
            

        
main()