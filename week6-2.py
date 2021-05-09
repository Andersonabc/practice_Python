"""
#印多組圖形

輸入第一個整數，決定輸出圖形種類，
輸入第二個整數，決定輸出的行數。
..1
.121
12321
.121
..1
7531357
.53135
..313
...1
輸入說明：
每一組兩個數字，輸入-1結束所有輸入。
第一個正整數，1為菱形數字，2為三角形數字，其餘輸入均為不合法。
第二個正整數為行數 N， 第一種圖形合法輸入 N 為奇數，1<=N<=18，
第二種圖形合法輸入，1<=N<=5，其餘輸入均為不合法。
不合法輸入，則輸出 E。
輸出說明：
每個圖形之間需留空行
請參考範例輸出。
Sample Input1:
1 9
1 13
-1
Sample Output:
....1
...121
..12321
.1234321
123454321
.1234321
..12321
...121
....1
......1
.....121
....12321
...1234321
..123454321
.12345654321
1234567654321
.12345654321
..123454321
...1234321
....12321
.....121
......1
Sample Input2:
1 22
1 5
-1
Sample Output:
E
..1
.121
12321
.121
..1
Sample Input:
---------------
2 5
2 4
2 2
2 12
-1
Sample Output:
--------------
975313579
.7531357
..53135
...313
....1
7531357
.53135
..313
...1
313
.1
E
"""
def pic1 (a):
    b=a//2
    for i in range (b+1):
        for j in range(b-i-1,-1,-1):
            print('.',end='')
        for k in range(1,i+2,1):
            print(k,end='')
        for z in range(i,0,-1):
            print(z,end='')
        print('')       
    for i in range (b):
        for j in range (i+1):
            print('.',end='')
        for k in range (1,b-i+1):
            print(k,end='')
        for z in range (b-i-1,0,-1):
            print(z,end='')
        print('')
            

def pic2 (a):
    b=a*2
    for i in range (a):
        for k in range (i):
            print('.',end='')
        for j in range (2*a-1-2*i,0,-2):
            print(j,end='')
        for z in range (3,2*a-2*i,2):
            print(z,end='')
        print('')
        
def main():
    i=0
    A=[]
    num=input()
    while (num!='-1'):
        B=[num]
        A.extend(B)
        num=input()
        i+=1
        
    for i in range (len(A)):
        a=A[i].split()
        if a[0]=='1' :
            if (int(a[1])%2==1 and int(a[1])>=1 and int(a[1])<=18):
                pic1(int(a[1]))
            else:
                print('E')
        elif a[0]=='2':
            if (int(a[1])>=1 and int(a[1])<=5):
                pic2(int(a[1]))
            else:
                print('E')
        else:
            print('E')
        print('')
        
    
    
main()