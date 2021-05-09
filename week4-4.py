"""
#計算電費

輸入月份、輸入前年所使用的度數及今年使用的度數，
依據月份是否為夏季電費做計算依據，並計算出電費，
若今年度有較前年成功節電，則每節一度電可省0.6元
每度(元) 夏季電價(7~9月) 非夏季電價
120度以下 2.10 2.10
121-330度 3.02 2.68
331-500度 4.39 3.61
501-700度 4.97 4.01
701度以上 5.63 4.50
輸入說明：
---------------
輸入月份
輸入前年使用度數
輸入今年使用度數
輸出說明：
---------------
輸出電費
測試案例(Test Case)資料：
Input：
7
505
525
Output：
2609.25
Input：
7
550
525
Output
2594.25
(以此題為例，較上年度節電25度，故計算方式為525*4.97-(550-525)*0.6)
"""

def calsum(a,b):
    if(a<=120):
        cost=a*2.1
    elif(a>120 and a<=330):
        cost=a*3.02
    elif(a>330 and a<=500):
        cost=a*4.39
    elif(a>500 and a<=700):
        cost=a*4.97
    else:
        cost=a*5.63
    cost=cost-0.6*b
    print("%.2f"%(cost))
        
def calnor(a,b):
    if(a<=120):
        cost=a*2.1
    elif(a>120 and a<=330):
        cost=a*2.68
    elif(a>330 and a<=500):
        cost=a*3.61
    elif(a>500 and a<=700):
        cost=a*4.01
    else:
        cost=a*4.5
    cost=cost-0.6*b
    print("%.2f" %(cost))
    

def main ():
    month=int(input())
    layr=float(input())
    thyr=float(input())
    if (thyr-layr)<0 :
        i=layr-thyr
    else:
        i=0
    if(month<=9 and month >=7):
        calsum(thyr,i)
    else:
        calnor(thyr,i)
        
main()