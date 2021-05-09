"""
#猜數列

小明的家庭作業裏有很多數列填空練習。
填空練習的要求是：已知數列的前四項，填出第五項。
因為已經知道這些數列只可能是等差或等比數列，他決定寫一個程式來完成這些練
輸入說明:
第一行是數列的數目t（1 <= t <= 20）。
以下每行均包含四個整數，表示數列的前四項。
輸出說明:
對輸入的每個數列，輸出它的前五項。
不合法的輸入則輸出E。
input :
2
1 2 3 4
32 16 8 4
output:
1 2 3 4 5
32 16 8 4 2
"""
def cal(x1,x2,x3,x4):
    if (x1/x2==x2/x3):
        a=x2/x1
        print('%d %d %d %d %d' %(x1,x2,x3,x4,x4*a))
    elif ((x1+x3)/2==x2):
        a=x2-x1
        print('%d %d %d %d %d' %(x1,x2,x3,x4,x4+a))
    else:
        print('E')
    
 
def main():
    times=int(input())
    list1 = []
    if (times>=1 and times<=20): 
        for i in range (times):
            list1.append(list(map(int,input().split())))
    else:
        print('E')
        
        
    for j in range (times):
        cal(list1[j][0],list1[j][1],list1[j][2],list1[j][3])
    print(list1)
    
    
main()