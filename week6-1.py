"""
#多重線段

請使用一個 while loop 和 function call
C 語言此題不使用陣列。
Python 此題不使用 List。
給定一些線段，求這些線段所覆蓋的長度，注意，重疊的部分只能算一次。
輸入說明 ：
第一列有一個正整數 n:
代表共有 n 組測試案例。
接下來每一組測試案例的第一列是一個整數 m
表示此測試案例有m個線段，
接著的m列每一列是一個線段的兩端點，
每一個端點是一個整數介於0~60000之間，
端點之間以一個空格區隔，線段個數不超過 5000。
-----------------------------
輸出說明 ：
針對每一組測試案例，輸出其覆蓋的長度，每組測試案例輸出一列。
不合法的輸入則輸出E
Input:
2 (共有2組次是案例)
2 (此組測試案例有2個線段)
0 1
2 3
3 (此組測試案例有3個線段)
0 20
10 30
40 50
Output:
2
40
-------------
Input:
3
3
10 111
150 3450
160 180
2
100 180
150 3333
1
150 150
Output:
3401
3233
0
--------------
Input:
1
2
150 320
160 190
Output:
170
"""

def test1(total):
    a=input()
    wire=a.split()
    for k in range(len(wire)):
        wire[k]=int(wire[k])
    for k in range(len(wire)):
        if wire[k]>=0 and wire[k]<=60000:
            yn=0
            
        else:
            yn=1
            break
    total.append(list(wire))
    return total,yn 

    
    
def test2(total):
    k=0
    total.sort(key=lambda x:x[0] )
    
    return total        
    
def cal (answer):
    a=0
    for i in range (len(answer)-1):
        if answer[i][1]>answer[i+1][1]:
            answer[i+1][0]=answer[i+1][1]=0
        elif answer[i][1]>answer[i+1][0]:
            answer[i+1][0]=answer[i][1]
        
    for j in range (len(answer)):
        a=a+answer[j][1]-answer[j][0]
    
    return a
    
def main ():
    
    sum=[]
    total=[]
    case=int(input())
    for i in range (case):
        yn=0
        total=[]
        line=int(input())
        if line <=5000 :
            
            for j in range(line):
                total,yn=test1(total)
                if yn==1 and j!=line-1:
                    for i in range(line-j-1):
                        total,yn=test1(total)
                        yn=1
                    break
                    
            if yn == 0:
                answer=test2(total) 
                sum.append(cal(answer))
            else :
                sum.append('E')
                
        else:
            print('E')


    for j in range (len(sum)):
       
        print(sum[j])



    
    
main()