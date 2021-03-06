"""
#猜數字

程式的使用者設定一個答案 X，四位數，0~9不重複。
程式的使用者輸入 4 位數字，以及這些 4 位數與答案 X 的相似程度。
程式必須根據相似程度資料，輸出使用者設定的答案 X。
相似程度的規則
(1) Yi 中有 1 位數字跟答案 X 一樣，且所在位置相同，例如千位對千位，或百位對百位，記為 1A。
若 2 位都有這情況，就是2A。
例如 X=1234，Y1=1856，兩者都有 1 ，位置都在千位，因此相似程度是 1A。
(2) Yi 中有 1 位數字跟答案 X 一樣，但所在位置不同，記為 1B。
若 2 位都有這情況，就是2B。
例如 X=1234，Y1=8561，兩者都有 1，但位置不同，所以是 1B。
(3) 以上兩條規則以 (1)優先，之後再考慮 (2)。
(4) 輸入至猜出答案為止
----------------------------------------------------------------------------------
輸入範例說明:
每一行輸入 4 位數字 Yi，以及相似程度 ?A?B。
假設使用者設定的答案是 4237
輸入
1968,0A0B 數字都沒有對，所以相似程度為 0A0B。
7052,0A2B 有 2 個數字對 (7, 2) ，但位置不對，相似程度為 0A2B。
2347,1A3B 有 1 個數字對且位置對 (7)， 3 個數字對 (2, 3, 4)，相似程度為1A3B。
3427,1A3B 有 1 個數字對且位置對 (7)， 3 個數字對 (3, 4, 2)，相似程度為1A3B。
2473,0A4B 4 個數字對，位置不對。
輸出範例說明:
4237 輸出使用者設定的答案
Sample Input
1968,0A0B
7052,0A2B
2347,1A3B
3427,1A3B
2473,0A4B
Sample Output
4237
"""
def compare(ans,gn):
    A,B,i = 0,0,0
    gn1=list(gn)
    digits = len(ans)
    copyans = list(ans)
    while i < digits-A:
        if copyans[i]==gn1[i]:
            A+=1                            
            gn1.remove(gn1[i])
            copyans.remove(copyans[i])
        else:
            i+=1
            
    digits = len(copyans)
    for i in range(digits):
        for j in range(digits):
            if copyans[i]==gn1[j]:
                B+=1
                break
    return A,B
    
    
def judge(a,guess,A1,B1):
    s=[]
    for i in range (len(a)):
        x,y=compare(a[i],tuple(guess))     
        if ( int(x)==int(A1) and int(y)==int(B1)):
            s.append(a[i])
    return s

def main():
    a=[(str(i%10),str((i//10)%10),str((i//100)%10),str((i//1000)%10))for i in range (10000)]
    x=0;j=0;i=0
    lol=len(a)
    for i in range (10):
        j=0
        while j < lol-x:
            if a[j].count(str(i))>1:
                a.remove(a[j])
                x+=1
            else:
                j+=1
    while True:
        hintnum=[]
        hint=input()
        for i in range (4) :
            hintnum.append(hint[i])
        if hint[5]=='4':
            for i in range (4):
                print(hint[i],end='')
        else:
            new_a=judge(a,hintnum,hint[5],hint[7])
            a=new_a
            if len(a)==1:
                for i in range (4):
                    print(a[0][i],end='')
                break
            
main()