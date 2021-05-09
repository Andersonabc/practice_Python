"""
#保齡球

小明到保齡球館打保齡球，一次十局。若一到八局都零分，剩下最後兩局。
保齡球打球規則為:
(1) 每一局有十瓶保齡球瓶。
(2) 若某局第一球沒有全部打倒十瓶保齡球瓶，可再打第二球。
(3) 若某局第一球打倒全部十瓶保齡球瓶，此局只打一球。
(4) 若第十局打倒全部十瓶保齡球瓶，此局可以打三球。
保齡球每一局計分規則為:
(1) 兩球打倒保齡球瓶少於十瓶，每一瓶得一分。
例如兩球打倒 7 瓶、2瓶，計為 7 2。
此局分數計為 7+2 = 9。
(2) 第一球打倒保齡球瓶少於十瓶，第二球將剩餘球瓶均打倒 (spare)，
每一瓶得一分，並加計後面一球打倒瓶數。
例如兩球打倒 7 瓶、3 瓶，下一球打倒 5 瓶，計為 7 3。
若此局為第十局，計為 7 3 5。
此局分數為 7 + 3 + 5。
(3) 第一球打倒保齡球瓶等於十瓶，不用打第二球 (strike)。
每一瓶得一分，並加計後面兩球打倒的瓶數。
例如本局第一球打打倒 10 瓶，後面兩球打倒 5、0 瓶，本局計為 10。
若此局為第十局，計為 10 5 0。
此局分數為 10 + 5 + 0。
例如本局打倒 10 瓶，後面兩球打倒 10、10 瓶，計為 10。
若此局為第十局，計為 10 10 10。
此局分數為 10 + 10 + 10。
試算出總得分
測試案例(Test Case)資料：
Input：
2 5
7 1
Output：
15
---------------
Input：
5 5
10 8 0
Output：
38
---------------
Input：
10
10 8 2
Output：
48
---------------
Input：
8 2
7 3 8
Output：
35
"""

def check(x):
    if int(x[0])==10:
        return 1
    elif int(x[0])+int(x[1])==10:
        return 2
    else:
        return 0
        
def hey (ck2,ans,lisrd10):
    if ck2==0:
        for j in range(len(lisrd10)):
            ans+=int(lisrd10[j])
        print(ans)
    if ck2==1:
        for j in range(len(lisrd10)):
            ans+=int(lisrd10[j])  
        print(ans)
    if ck2==2:
        for j in range(len(lisrd10)-1):
            ans+=int(lisrd10[j])   
        print(ans)
def main():
    rd9=input()
    lisrd9=rd9.split()
    rd10=input()
    lisrd10=rd10.split()
    ck1=check(lisrd9)
    ck2=check(lisrd10)
    ans=0
    for i in range(len(lisrd9)):
        ans+=int(lisrd9[i]) 
    if ck1==0:   
        hey(ck2,ans,lisrd10)
    if ck1==1:
        if ck2==1:
            ans=ans+int(lisrd10[0])+int(lisrd10[2])
            hey(ck2,ans,lisrd10)
        else:
            ans=ans+int(lisrd10[0])+int(lisrd10[1])
            hey(ck2,ans,lisrd10)
    if ck1==2:
        ans=ans+int(lisrd10[0])
        hey(ck2,ans,lisrd10)


main()