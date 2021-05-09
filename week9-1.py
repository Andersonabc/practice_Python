"""
#方程式計算

寫一個 function 輸入 XY 座標系統的兩個座標 (x1, y1), (x2, y2)；
輸出兩個座標經過的 XY 方程式 y=mx+b;
m=(y1-y2)/(x1-x2)
b=(x2y1-x1y2)/(x2-x1)
void f1_m(int x1, int y1, int x2, int y2, double m, double b);
寫一個 function 輸入 XY 座標系統的兩個座標 (x1, y1), (x2, y2)；
輸出兩個座標經過的 XY 方程式 y=m1/m2x+b1/b2;
m1=(y1-y2), m2=(x1-x2),
b1=(x2y1-x1y2), b2=(x2-x1),
void f2(int x1, int y1, int x2, int y2, int m1, int m2, int b1, int b2);
-------------
輸入說明:
XY的兩個座標 x1, y1, x2, y2，均為整數。
輸出說明:
(1) y=mx+b,
m, b 計算至小數第二位。
(2) y=mx+b
m, b 以分數表達，分數不需要化簡。
=>方程式有可能沒有 x 項，或沒有 y 項。
=>沒有 x 項則 y=b，沒有 y 項則 x = -b/m。
=>若m,b為整數，則使用整數表達。
不合法的輸入則輸出Error!
-------------
輸入範例:
3 4 -3 0
輸出範例:
y=0.67x+2
y=4/6x+2
-------------
輸入範例:
3.3 4 -3 0
輸出範例:
Error!
-------------
輸入範例:
1 0 0 1
輸出範例:
y=-x+1
y=-x+1
"""
def f1(x1,y1,x2,y2):    
    a=0
    if x1==x2:
        m=0
        b=0
    else:
        m=(y1-y2)/(x1-x2) 
        b=(x2*y1-x1*y2)/(x2-x1)         
    if x1==x2:
        print('x=%d' %x1)
    elif y1==y2:
        print('y=%d' %y1)
    elif m.is_integer() == True and b.is_integer() == True:
        if abs(m)==1 and b!=0:
            if m==-1:
                print('y=-x+%d' %b)
            else:
                print('y=x+%d' %b)           
        elif m!=1 and b!=0:
            if b>0:
                print('y=%dx+%d' %(m,b))
            else:
                print('y=%dx-%d' %(m,abs(b)))
        elif abs(m)==1 and b==0:
            if m ==1:            
                print('y=x')
            else:
                print('y=-x')
        elif m!=1 and b==0:
            print('y=%dx' %m)
        else:
            print('Error!')
    elif m.is_integer() == False and b.is_integer() == True:
        if b==0:
            print('y=%.2fx' %m)
        else:
            if b>0:
                print('y=%.2fx+%d' %(m,b))
            else:
                print('y=%.2fx-%d' %(m,abs(b)))
    elif m.is_integer() == True and b.is_integer() == False:
        if m==1:
            print('y=x+%.2f' %b)
        elif m==-1:
            print('y=-x+%.2f' %b)
        else:
            if b>0:
                print('y=%dx+%.2f' %(m,b))
            else:
                print('y=%dx-%.2f' %(m,abs(b)))
    elif m.is_integer() == False and b.is_integer() == False:
        if b>0:
            print('y=%.2fx+%.2f' %(m,b)) 
        else:
            print('y=%.2fx-%.2f' %(m,abs(b)))
        
def f2(x1,y1,x2,y2,m1,m2,b1,b2):
    if x1==x2:
        print('x=%d' %x1)
    elif y1==y2:
        print('y=%d' %y1)
    elif (m1/m2)<0 :   
        if (m1/m2)==-1:
            if ((b1/b2).is_integer()==True and (b1/b2)>0 ):
                print('y=-x+%d' %abs(b1/b2))
            elif ((b1/b2).is_integer()==True and (b1/b2)<0 ):
                print('y=-x-%d' %abs(b1/b2))
            else:
                if (b1/b2)<0 :
                    if (b1/b2)==-1 :
                        print('y=-x-1' %(abs(m1),abs(m2)))
                    else:
                        print('y=-x-%d/%d' %(abs(b1),abs(b2)))
                elif (b1/b2)>0:
                    if (b1/b2)==1:
                        print('y=-x+1')
                    else:
                        print('y=-x+%d/%d' %(abs(b1),abs(b2)))
                elif b1==0:
                    print('y=-x')    
    
        elif (m1/m2).is_integer()==True and (m1/m2)!=-1:
            if ((b1/b2).is_integer()==True and (b1/b2)>0 ):
                print('y=-%dx+%d' %(abs(m1/m2),abs(b1/b2)))
            elif ((b1/b2).is_integer()==True and (b1/b2)<0 ):
                print('y=-%dx-%d' %(abs(m1/m2),abs(b1/b2)))
            else:
                if (b1/b2)<0 :
                    if (b1/b2)==-1 :
                        print('y=-%dx-1' %(abs(m1/m2)))
                    else:
                        print('y=-%dx-%d/%d' %(abs(m1/m2),abs(b1),abs(b2)))
                elif (b1/b2)>0:
                    if (b1/b2)==1:
                        print('y=-%dx+1' %(abs(m1/m2)))
                    else:
                        print('y=-%dx+%d/%d' %(abs(m1/m2),abs(b1),abs(b2)))
                elif b1==0:
                    print('y=-%dx' %(abs(m1/m2)))  
                  
        else:
            if ((b1/b2).is_integer()==True and (b1/b2)>0 ):
                print('y=-%d/%dx+%d' %(abs(m1),abs(m2),abs(b1/b2)))
            elif ((b1/b2).is_integer()==True and (b1/b2)<0 ):
                print('y=-%d/%dx-%d' %(abs(m1),abs(m2),abs(b1/b2)))
            else:
                if (b1/b2)<0 :
                    if (b1/b2)==-1 :
                        print('y=-%d/%dx-1' %(abs(m1),abs(m2)))
                    else:
                        print('y=-%d/%dx-%d/%d' %(m1,m2,abs(b1),abs(b2)))
                elif (b1/b2)>0:
                    if (b1/b2)==1:
                        print('y=-%d/%dx+1' %(abs(m1),abs(m2)))
                    else:
                        print('y=-%d/%dx+%d/%d' %(abs(m1),abs(m2),abs(b1),abs(b2)))
                elif b1==0:
                    print('y=-%d/%dx' %(abs(m1),abs(m2)))           
    elif (m1/m2)>0  :    
        if (m1/m2)==1:
            if ((b1/b2).is_integer()==True and (b1/b2)>0 ):
                print('y=x+%d' %abs(b1/b2))
            elif ((b1/b2).is_integer()==True and (b1/b2)<0 ):
                print('y=x-%d' %abs(b1/b2))
            else:
                if (b1/b2)<0 :
                    if (b1/b2)==-1 :
                        print('y=x-1' %(abs(m1),abs(m2)))
                    else:
                        print('y=x-%d/%d' %(abs(b1),abs(b2)))
                elif (b1/b2)>0:
                    if (b1/b2)==1:
                        print('y=x+1')
                    else:
                        print('y=x+%d/%d' %(abs(b1),abs(b2)))
                elif b1==0:
                    print('y=x')                    
        elif (m1/m2).is_integer()==True :
            if ((b1/b2).is_integer()==True and (b1/b2)>0 ):
                print('y=%dx+%d' %(abs(m1/m2),abs(b1/b2)))
            elif ((b1/b2).is_integer()==True and (b1/b2)<0 ):
                print('y=%dx-%d' %(abs(m1/m2),abs(b1/b2)))
            else:
                if (b1/b2)<0 :
                    if (b1/b2)==-1 :
                        print('y=%dx-1' %(abs(m1/m2)))
                    else:
                        print('y=%dx-%d/%d' %(abs(m1/m2),abs(b1),abs(b2)))
                elif (b1/b2)>0:
                    if (b1/b2)==1:
                        print('y=%dx+1' %(abs(m1/m2)))
                    else:
                        print('y=%dx+%d/%d' %(abs(m1/m2),abs(b1),abs(b2)))
                elif b1==0:
                    print('y=%dx' %(abs(m1/m2)))        
        else:
            if ((b1/b2).is_integer()==True and (b1/b2)>0 ):
                print('y=%d/%dx+%d' %(abs(m1),abs(m2),abs(b1/b2)))
            elif ((b1/b2).is_integer()==True and (b1/b2)<0 ):
                print('y=%d/%dx-%d' %(abs(m1),abs(m2),abs(b1/b2)))
            else:
                if (b1/b2)<0 :
                    if (b1/b2)==-1 :
                        print('y=%d/%dx-1' %(abs(m1),abs(m2)))
                    else:
                        print('y=%d/%dx-%d/%d' %(abs(m1),abs(m2),abs(b1),abs(b2)))
                elif (b1/b2)>0:
                    if (b1/b2)==1:
                        print('y=%d/%dx+1' %(abs(m1),abs(m2)))
                    else:
                        print('y=%d/%dx+%d/%d' %(abs(m1),abs(m2),abs(b1),abs(b2)))
                elif b1==0:
                    print('y=%d/%dx' %(abs(m1),abs(m2)))    
    else:
        print('132123123')        
def main():
    try:
        inin=list(map(int,input().split()))
        if not len(inin)==4:
            print('Error!')
        else:
            #m=(inin[1]-inin[3])/(inin[0]-inin[2])
            #b=(inin[2]*inin[1]-inin[0]*inin[3])/(inin[2]-inin[0])
            m1=inin[1]-inin[3]
            m2=inin[0]-inin[2]
            b1=inin[2]*inin[1]-inin[0]*inin[3]
            b2=inin[2]-inin[0]
            f1(inin[0],inin[1],inin[2],inin[3])
            f2(inin[0],inin[1],inin[2],inin[3],int(m1),int(m2),int(b1),int(b2))
    except TypeError:
        print('Error!')
    except ValueError:
        print('Error!')
main()
