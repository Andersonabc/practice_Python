"""
#判斷何種三角形

當三個邊長能構成三角形時，再判斷該三角形是否為正三角形，若否，則判斷是否為等腰三角形：
1. 不能成為三角形：任兩邊和不大於第三邊，或任一邊長不大於0。
2. 正三角形：三個邊相等。
3. 等腰三角形：任兩邊相等，平方和大於第三邊的平方。
4. 一般三角形：非正三角形與等腰三角形。
此題必須寫一個運算的function
int getTriangle(int a, int b, int c);
輸入說明：
---------------
輸入三個整數邊長
輸出說明：
---------------
1. 不能成為三角形：輸出 not triangle。
2. 正三角形：輸出 equilateral triangle。
3. 等腰三角形：輸出 isosceles triangle。
4. 一般三角形：輸出 triangle。
測試案例(Test Case)資料：
Input：
4 1 1
Output：
not triangle
---------------
Input：
3 3 3
Output：
equilateral triangle
---------------
Input：
3 2 3
Output：
isosceles triangle
---------------
Input：
7 8 9
Output：
triangle
"""
def getTriangle(a,b,c):
    if (a<=0 or b<=0 or c<=0 or (a+b)<=c or (b+c)<=a or (c+a)<=b):
        return 1
    elif (a==b==c):
        return 2
    elif ((a==b or b==c or a==c) and ((a*a)+(c*c))>(b*b) and ((a*a)+(b*b))>(c*c) and ((c*c)+(b*b))>(a*a)):
        return 3
    else:
        return 4
		
def output (a):
    if a==1:
        print("not triangle")
    elif a==2:
        print("equilateral triangle")
    elif a==3:
        print("isosceles triangle")
    else:
        print("triangle")
		
def main():
    x1=input()
    y=str.split(x1)
    a=getTriangle(int(y[0]),int(y[1]),int(y[2]))
    output(a)
	
main()