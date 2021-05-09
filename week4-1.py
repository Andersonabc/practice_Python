"""
#停車費計算

假設某個停車場的費率是停車2小時以內，每半小時30元，未滿半小時部分不計費。
超過2小時，但未滿4小時，每半小時40元，未滿半小時以半小時計費。
超過4小時以上的部份，每半小時60元，未滿半小時以半小時計費。
請撰寫程式計算輸入數筆資料，共需繳交的停車費。
本程式不考慮隔夜情況。
輸入說明：
---------------
輸入3組時間，每組分別為開始與離開時間，24小時制。
若輸入格式錯誤，則輸出error
輸出說明：
---------------
輸出總停車費。
測試案例(Test Case)資料：
Input：
8:00
9:15
13:45
16:50
6:20
10:50
Output：
60
240
340
Input：
00:01
25:00
00:11
23:66
-01:00
12:34
Output：
error
error
error
"""
def comp(a1,err):
    if(err==0):
        if(a1<=120):
            cost=0+((a1)//30)*30
            
        elif(a1>120 and a1<=240):
        
            cost=((a1-120)//30)*40+120
            if((a1%30)!=0):
                cost=cost+40
        else:
            cost=((a1-240)//30)*60+280
            if((a1%30)!=0):
                cost=cost+60
        print(cost)
    else:
            print('error')
    
    
def main():
    err=0
    a1=input()
    aa1=a1.split(':')
    
    a2=input()
    aa2=a2.split(':')
    
    b1=input()
    bb1=b1.split(':')
    
    b2=input()
    bb2=b2.split(':')
    
    c1=input()
    cc1=c1.split(':')
    
    c2=input()
    cc2=c2.split(':')
    
    x1=[aa1[0],aa2[0],bb1[0],bb2[0],cc1[0],cc2[0]]
    y1=[aa1[1],aa2[1],bb1[1],bb2[1],cc1[1],cc2[1]]
    for i in range (3):
        if (int(x1[i])<0 or int(x1[i])>=24 ):
            err=1
        if(int(y1[i])<0 or int(y1[i])>=60 ):
            err=1
    an1=(int(aa2[0])*60+int(aa2[1]))-(int(aa1[0])*60+int(aa1[1]))
    an2=(int(bb2[0])*60+int(bb2[1]))-(int(bb1[0])*60+int(bb1[1]))
    an3=(int(cc2[0])*60+int(cc2[1]))-(int(cc1[0])*60+int(cc1[1]))
    if (an1<=0 or an2<=0 or an3<=0):
        err=1
        
    cost1=comp(an1,err)
    cost2=comp(an2,err)
    cost3=comp(an3,err)
 
main()