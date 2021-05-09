"""
#計算保齡球分數(無視規則-除了第十局)

小明到保齡球館打保齡球，一輪有十局，假設小明一到八局都拿零分，剩下最後兩局
每局有十瓶保齡球瓶，倒一瓶保齡瓶得一分，每一局最多為十分，
每一局可以打兩次，若在第十局打出strike，可以再多打一局，但當局只能打一次，試算出總得分
測試案例(Test Case)資料：
Input：
2
5
7
1
Output：
15
---------------
Input：
5
5
10
0
8
Output：
28
"""
def main ():
    a1=int(input())
    if(a1!=10):
        a2=int(input())
        b1=int(input())
    else:
        b1=int(input())
        a2=0
    if(b1==10):
        b2=0
        c1=int(input())
        if(c1!=10):
            c2=int(input())
        else:
            c2=0
    else:
        b2=int(input())
        c1=0
        c2=0
    total=a1+a2+b1+b2+c1+c2
    print(total)

main()