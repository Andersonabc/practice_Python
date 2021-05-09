"""
#十進制轉換

(若為 C 語言，請使用一個 loop 和 function call)
給予一個十進位整數，請撰寫一程式可以將此十進位整數轉換為指定的進制的整數。
輸入說明:
輸入分為兩部份，包括指定的進制數
(2 ~ 16)
與十進位整數(0 ~ 1000000000)
輸出說明:
經轉換後的新進位制的整數( y )
不合法的輸入則輸出E
input:
16 1234
output:
4D2
----------------------
Input:
8 56456456
Output:
327272410
-----------------------
Input:
11 17489465
Output:
9966104
-----------------------
Input:
4 17489
Output:
10101101
"""
def cal(a,b):
    list = ['A', 'B', 'C', 'D', 'E', 'F']
    str_tran=""
    while a>=b:
        x=a%b
        if(x>=10):
            str_tran=str(str_tran)+list[x%10]
        else:
            str_tran=str(str_tran)+str(x)
        a=a//b
    str_tran=str(str_tran)+str(a)
    return str_tran
    
def output(ans):
    return ans[::-1]

    
def main():
    x=input()
    y=str.split(x)
    if(int(y[0])<2 or int(y[0])>16 or int(y[1])<0 or int(y[1])>1000000000):
        print('E')
    else:
        ans=cal(int(y[1]),int(y[0]))
    
    ans=output(ans)
    print(ans)
    
main()