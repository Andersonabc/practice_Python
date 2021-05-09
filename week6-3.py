"""
#密碼鎖1A2B

四位數字密碼鎖，忘記密碼最多嘗試10^4=10000次解鎖。
若知道嘗試的密碼的錯務資訊，解鎖速度就可增快。
請寫程式判斷猜測數字跟正確答案的正確位置與個數資訊。
輸入說明:
------------------------------------------------
第一行有四個介於0-9之間的數字，代表正確密碼。
第二行後，每行有四個介於0-9之間的數字，代表一組猜測密碼。
最後輸入-1 結束。
輸出說明
------------------------------------------------
每組猜測密碼，跟正確密碼比對規則
(1) 計算數字值正確，且在正確位子的個數 m，記為 mA。
(2) 計算數字值正確，但不在正確位子的個數 n，記為 nB。
(3) 若出現重複數字，每個數字比對一次，先比對規則(1)，若否再比對規則(2)。
如 5543、5255，第一個 5 數字正確，記為1A、第二個 5 數字正確記為1B。
輸出 mAnB。
Sample Input:
---------------
1 2 3 4
1 1 4 5
1 2 4 3
1 1 4 4
4 3 2 1
-1
Sample Output:
--------------
1A1B
2A2B
2A0B
0A4B
Sample Input:
---------------
1 1 1 5
1 1 1 1
0 9 2 8
1 5 2 3
1 1 5 1
-1
Sample Output:
--------------
3A0B
0A0B
1A1B
2A2B
"""
def compare (List,Guess):
    a=b=c=k=0
    d=4
    List1=list(List)
    Guess=Guess.split()
    for j in range (len(Guess)):
        Guess[j]=int(Guess[j])
        
    while k < d :

        if List1[k]==Guess[k]:
            a+=1
            Guess.remove(Guess[k])
            List1.remove(List1[k])
            d-=1
            k=k
        else:
            k+=1
            d=d
            
            
    for i in range (len(Guess)):
        for z in range (len(List1)):
            if (Guess[i] == List1[z] and i!=z ):
                b+=1
                if Guess.count(Guess[i])>1:
                    c+=1
    if c>0:
        c=c-1   
    b=b-c

    print('%dA%dB' %(a,b))

def inv (LI):
    for i in range (len(LI)):
        LI[i]=int(LI[i])
    return LI
    
def main ():
    x=input()
    Ans=x.split()
    for i in range (len(Ans)):
        Ans[i]=int(Ans[i])
    i=0
    A=[]
    B=[]
    Gue=input()
    while (Gue!='-1'):
        B=[Gue]
        A.extend(B)
        Gue=input()
        i+=1
    
    for j in range (i):
        compare(tuple(Ans),A[j])
main()