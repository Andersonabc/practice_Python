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
def output(Alist,Blist):
    for i in range(len(Alist)):
        print('%dA%dB'%(Alist[i],Blist[i]))

def compare(ans,gn,Alist,Blist):
    A,B,i = 0,0,0
    digits = len(ans)
    copyans = list(ans)
    while i < digits-A:
        if copyans[i]==gn[i]:
            A+=1                            
            gn.remove(gn[i])
            copyans.remove(copyans[i])
        else:
            i+=1
    digits = len(copyans)
    for i in range(digits):
        for j in range(digits):
            if copyans[i]==gn[j]:
                B+=1
            break
    Alist.append(A)
    Blist.append(B)

def main():
    answer = input().split()
    guessnum = [0]
    n = 0
    Alist,Blist = [],[]
    while True:
        guessnum = input().split()     
        print(guessnum)
        if guessnum[0] == '-1':
            guessnum.remove('-1')
            break
        n += 1
        compare(answer,guessnum,Alist,Blist)
        print(guessnum)
       
    output(Alist,Blist)		

main()