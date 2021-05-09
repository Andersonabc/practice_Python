"""
#一元二次方程式

一元二次方程式，aX^2 + bx + c = 0，輸入a, b, c, 求 方程式的兩個實/虛根。
T = sqrt(b*b-4*a*c)
第一個根， x1 = (-b+T)/(2*a)
第二個根， x2 = (-b-T)/(2*a)
#若為 C 語言，本題須 #include < math.h >
---------------
輸入說明：
第一個數 a
第二個數 b
第三個數 c
---------------
輸出說明：
當 T>=0
輸出x1, x2為實根，輸出到小數點第一位 print("%.1f" %x1);
當 T<0
輸出x1 , x2為虛根，輸出到小數點第一位
print("%.1f+%.1fi" %(x11, x12))
print("%.1f-%.1fi" %(x21, x22))
若x11或x21為0.0時，不須輸出正負號
測試案例(Test Case)資料：
Input：
1
-2
1
Output：
1.0
1.0
---------------
Input：
1
2
2
Output：
-1.0+1.0i
-1.0-1.0i
"""

from math import sqrt
def cal (a, b, c):
   
    if((b*b-4*a*c)>=0):
        T = sqrt(b*b-4*a*c)
        x1 = (-b+T)/(2*a)
        x2 = (-b-T)/(2*a)
        x11=x12=x21=x22=0
        i=1

    else:
        x11=-b/(2*a)
        x12=sqrt(-(b*b-4*a*c))/(2*a)
        x21=-b/(2*a)
        x22=sqrt(-(b*b-4*a*c))/(2*a)
        x1=x2=0
        i=0
        T=0
    return T, x1, x2, x11, x12, x21, x22, i
	
def output (T, x1, x2, x11, x12, x21, x22, i):
    if(i==1):
        print("%.1f" %x1)
        print("%.1f" %x2)
    else:
        print("%.1f+%.1fi" %(x11, x12))
        print("%.1f-%.1fi" %(x21, x22))
		
def main():
    a=int(input())
    b=int(input())
    c=int(input())
    I,J,Y,Q,W,E,R,Y=cal (a, b, c)
    output(I,J,Y,Q,W,E,R,Y)
	
main()