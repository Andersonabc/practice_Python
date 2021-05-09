"""
#數值運算

分別輸入 num1 num2 求出兩數的 Sum,Difference,Product,Quotient。
結果須輸出到小數點第二位
print("%.2f" %x1);
輸入:
25
2
輸出:
Difference:23.00
Sum:27.00
Quotient:12.50
Product:50.00
"""

import math
def cal(a,b):
    sum=a+b
    de=math.fabs(a-b)
    quo=a/b
    pro=a*b
    return sum,de,quo,pro 

def main():
    a=int(input())
    b=int(input())
    x1,x2,x3,x4=cal(a,b)
    print("Difference:%.2f" %x2)
    print("Sum:%.2f" %x1)
    print("Quotient:%.2f" %x3)
    print("Product:%.2f" %x4)
	
main()