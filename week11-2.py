"""
#數獨

在9格寬×9格高的大九宮格中有9個3格寬×3格高的小九宮格
，每一列與每一行的數字均須包含 1～9，不能缺少，也不
能重複。每一小九宮格(3*3的九宮格)的數字均須包含 1～
9，不能缺少，也不能重複。
輸入一組測試資料為9x9的矩陣,判斷九宮格數字是不是一個
數獨的正解。
輸入說明 ：
輸入九列數據，每一列輸入為9個整數分別由空格分開。
輸出說明 ：
輸出Yes or No代表九宮格數字是不是一個數獨的正解。
----------------------
輸入範例
1 2 3 4 5 6 7 8 9
2 3 4 5 6 7 8 9 1
3 4 5 6 7 8 9 1 2
4 5 6 7 8 9 1 2 3
5 6 7 8 9 1 2 3 4
6 7 8 9 1 2 3 4 5
7 8 9 1 2 3 4 5 6
8 9 1 2 3 4 5 6 7
9 1 2 3 4 5 6 7 8
輸出範例
No
----------------------
輸入範例
1 9 3 2 6 5 4 7 8
7 8 2 3 1 4 9 5 6
4 5 6 9 7 8 1 3 2
2 3 4 8 5 1 6 9 7
9 6 5 4 3 7 2 8 1
8 7 1 6 9 2 3 4 5
3 1 9 5 8 6 7 2 4
5 2 7 1 4 3 8 6 9
6 4 8 7 2 9 5 1 3
輸出範例
Yes
"""
def build_mini(x,i,j):
    z=[]
    for w in range (i,i+3,1):
        for y in range (j,j+3,1):
            z.append(x[w][y])
    return z

def build_row(x,i):
    z=[]
    for j in range(9):
        z.append(x[j][i])
    print(z)
    return z
    
def check(x,yn):
    for i in range (9):
        for j in range (1,10):
            if x[i].count(str(j))!=1 :
                yn=0
    return yn

def main():
    yn=1
    x=[]
    x2=[]
    x3=[]
    for i in range (9):
        x.append(list(input().split()))      
    for i in range (0,7,3):
        for j in range (0,7,3):
            z=build_mini(x,i,j)
            x3.append(z)
    for i in range (9):
        q=build_row(x,i)
        x2.append(q)
    if check(x,yn)==1 and check(x2,yn)==1 and check(x3,yn)==1:
        print('Yes')   
    else:
        print('No')  
                
main()