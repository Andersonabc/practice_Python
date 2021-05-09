"""
#有限狀態機

一個有限狀態機(Finite state machine, FSM) 從起始狀態(start)開始運作，
包含一組橢圓形表示的狀態(State)和一組箭頭表示的轉換(Transition)連接兩個狀態，且接受輸入字元資料。
請參考圖片作答，來源網址 : https://imgur.com/a/H0Uya
寫一個function模擬FSM運作流程，識別C語言正確的識別字(Identifier)與非負整數(Number)。
每項資料項目以一或多的空白結束，以句點（.）結束。
需偵測不合法(Invalid)的輸入。
FSM Transition Symbol
Digit(1) 0, 1, .., 9
Period (2) .
Blank(3) 空白
Letter(4) A,.., Z, a, .., z
Letter(5) A,.., Z, a, .., z
Digit(6) 0, 1, .., 9
Underscore(7) _
Blank(8) 空白
Digit(9) 0, 1, .., 9
Blank(10) 空白
Others1(11) 非空白、非Digit、非Letter、非底線
Blank(12) 空白
Others2(13) 非空白、非Digit
Others3(14) 非空白
Input:
rate R2D2 48 2 time 555666 .
Output:
rate - Identifier
R2D2 - Identifier
48 - Number
2 - Number
time - Identifier
555666 - Number
---------------------------------------------------
Input: 4132 6rte r_yg t#ee 6677 .
Output:
4132 - Number
6rte - Invalid
r_yg - Identifier
t#ee - Invalid
6677 - Number
"""

def build_invalid (a,x):
    if x==len(a):
        print('%s - Invalid' %a)
    else:
        if a[x]!=' ':
            x+=1
            build_invalid (a,x)
        else:
            print('Error4')
def buid_id(a,x):
    if x==len(a):
        print('%s - Identifier' %a)
    else:
        if a[x].isdigit()==True or a[x].isalpha()==True or a[x]=='_':
            x+=1
            buid_id(a,x)
        elif a[x]!='_' and a[x].isdigit()==False and a[x].isalpha()==False and a[x]!=' ':
            x+=1
            build_invalid(a,x)
        else:
            print('Error3')    
def build_num(a,x):
    if x == len(a):
        print('%s - Number' %a)
    else:
        if a[x].isdigit()==True:
            x+=1
            build_num(a,x)
        elif a[x]!=' 'and a[x].isdigit()==False:
            x+=1
            build_invalid(a,x)
        else:
            print('Error2')
def start(a):
    x=0
    if a[x].isdigit()==True:
        x+=1
        build_num(a,x)
    elif a[x].isalpha()==True:
        x+=1
        buid_id(a,x)
    elif a[x]==' ':
        x+=1
        start(a,x)
    else:
        print('Error1')

def main():
    a=list(map(str,input().split()))
    for i in range(len(a)):
        if a[i]!='.':
            start(a[i])
        else:
            break
main()