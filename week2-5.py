"""
#最佳資費選擇

輸入每月網內、網外、市話、通話時間(秒)及網內、網外簡訊則數，求最佳資費。
費率如下表：
資費類型 183型 383型 983型
月租費 183元 383元 983元
優惠內容 月 租 費 可 抵 等 額 通 信 費
語音費率 網內 0.08 0.07 0.06
(元/秒) 網外 0.139 0.130 0.108
市話 0.135 0.121 0.101
(元/秒)
簡訊費率 網內 1.128 1.128 1.128
(元/則) 網外 1.483 1.483 1.483
---------------
輸入說明：
---------------
網內語音(秒)，整數
網外語音(秒)，整數
市話 (秒)，整數
網內簡訊數，整數
網外簡訊數，整數
輸出說明：
---------------
費用，整數
最佳資費類型，(183, 383, 983)
測試案例(Test Case)資料：
Input：
120
150
20
10
5
Output：
183
183
---------------
Input：
3000
4000
200
5
5
Output：
767
383
"""
def cal (a, b, c, d, e):
    i=0.08*a + 0.139*b + 0.135*c + 1.128*d + 1.483*e
    j=0.07*a + 0.130*b + 0.121*c + 1.128*d + 1.483*e
    k=0.06*a + 0.108*b + 0.101*c + 1.128*d + 1.483*e
    if (i<183):
       i=183
    if (j<383):
       j=383
    if (k<983):
       k=983
    
    return i, j, k
    
def com (x, y, z) :
    if (x<y and x<z):
        return 1
    elif (y<x and y<z):
        return 2
    elif (z<x and z<y):
        return 3
    else :
        return 4
        
        
def output (y,ii,jj,kk):
    if (y==1):
        print("%d" %ii)
        print("183")
    elif (y==2):
        print("%d" %jj)
        print("383")
    elif (y==3):
        print("%d" %kk)
        print("983")
    else :
        print("有相同資費方案")
    



def main():
    a1=int(input())
    a2=int(input())
    a3=int(input())
    a4=int(input())
    a5=int(input())
    b1,b2,b3=cal (a1, a2, a3, a4, a5)
    t=com (b1,b2,b3)
    output (t,b1,b2,b3)
    
main()