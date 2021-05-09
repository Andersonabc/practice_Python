"""
#請檢查輸入的三門課程是否衝堂。

依序輸入
課程編號 (4位數字)、
上課小時數 (1-2小時)、
上課時間 (依小時數輸入上課時間, 星期1-5, 第1-8節)。
輸入任何錯誤，輸出-1。
輸入說明：
---------------
1002 (第一門課課程編號)
2 (2 小時)
33 (星期 3 第 3 節課)
59 (星期 5 第 9 節課)
1003 (第二門課課程編號)
2 (2 小時)
11 (星期 1 第 1 節課)
33 (星期 3 第 3 節課)
3003 (第三門課課程編號)
2 (2 小時)
11 (星期 1 第 1 節課)
33 (星期 3 第 3 節課)
(上課時間輸入順序為星期 1~5，第 1 節 ~ 第 8 節)
(課程編號輸入順序為編號大小)
輸出說明：
---------------
1002,1003,33
1002,3003,33
1003,3003,11
1003,3003,33
輸出 課程編號,課程編號,衝突時間
若沒有衝突則輸出 correct
若有錯誤輸入則輸出 -1
(每次列出兩個衝突課程編號，一個衝突時間，所有倆倆課程衝突均要列出)
(衝突輸出順序，課程 1-2, 1-3, 2-3, 第 1 節 ~ 第 2 節)
測試案例(Test Case)資料：
Input：
1001
2
12
13
1002
2
13
21
1003
2
21
25
Output：
1001,1002,13
1002,1003,21
---------------
Input：
1001
1
21
1002
2
32
33
1003
2
45
46
Output：
correct
---------------
Input：
101
3
99
1002
2
32
33
1003
2
45
46
Output：
-1
"""

def main():
    cc=1
    
    a1=int(input())
    x=input()
    if(x=="1"):
        a3=int(input())
        if(a3>=11 and a3<=58):
            a=[a1,a3]
        else:
            cc=0
    elif(x=="2"):
        a3=int(input())
        a4=int(input())
        if(a3>=11 and a3<=58 and a4>=11 and a4<=58):
            a=[a1,a3,a4]
        else:
            cc=0
    else:
        a3=int(input())
        cc=0
 
    b1=int(input())
    y=input()
    if(y=="1"):
        b3=int(input())
        if(b3>=11 and b3<=58):
            b=[b1,b3]
        else:
            cc=0
    elif(y=="2"):
        b3=int(input())
        b4=int(input())
        if(b3>=11 and b3<=58 and b4>=11 and b4<=58):
            b=[b1,b3,b4]
        else:
            cc=0
    else:
        b3=int(input())
        cc=0

    c1=int(input())
    z=input()
    if(z=="1"):
        c3=int(input())
        if(c3>=11 and c3<=58):
            c=[c1,c3]
        else:
            cc=0
    elif(z=="2"):
        c3=int(input())
        c4=int(input())
        if(c3>=11 and c3<=58 and c4>=11 and c4<=58):
            c=[c1,c3,c4]
        else:
            cc=0
    else:
        c3=int(input())
        cc=0
    
    Cor=1
    if(cc==1): 
        
            for i in range (len(a)):
                for j in range (len(b)):
                    if (a[i]==b[j] and a[0]>=b[0]):
                        print("%d,%d,%d" %(b[0],a[0],a[i]))
                        Cor=0
                    elif(a[i]==b[j] and a[0]<b[0]):
                        print("%d,%d,%d" %(a[0],b[0],a[i]))
                        Cor=0
            for i in range (len(a)):
                for j in range (len(c)):
                    if (a[i]==c[j] and a[0]>=c[0]):
                        print("%d,%d,%d" %(c[0],a[0],a[i]))
                        Cor=0
                    elif(a[i]==c[j] and a[0]<c[0]):
                        print("%d,%d,%d" %(a[0],c[0],a[i]))
                        Cor=0            
            for i in range (len(b)):
                for j in range (len(c)):
                    if (b[i]==c[j] and b[0]>=c[0]):
                        print("%d,%d,%d" %(c[0],b[0],b[i]))
                        Cor=0
                    elif(b[i]==c[j] and b[0]<c[0]):
                        print("%d,%d,%d" %(b[0],c[0],b[i]))
                        Cor=0
                
            
            if (Cor!=0):
                print("correct")
    else:
        print("-1")
    
    
    
     

main()
