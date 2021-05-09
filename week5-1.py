"""
#階層與質因數

求階層(N!)值總和，0< N < 1000
輸入說明:
輸入一個整數N
------------------
輸出說明:
依序每一行輸出小於 N 的質因數，以及其階層值，以逗號隔開。
最後一行是所有階層值總和。
輸入錯誤，包括小數點、負數、字元或其他不合法的輸入，
輸出 E。
------------------
input :
10
output:
2,2
5,120
122
-----------------
input :
12
output:
2,2
3,6
8
-----------------
input :
30
output:
2,2
3,6
5,120
128
-----------------
input :
-1
output:
E
------------------
input
10.2
output:
E
------------------
input
a.2
output:
E
------------------
input
11.a2
output:
E
"""

import math

def multiplyinverse(mx,nx,my,ny,matrixX,matrixY):
    if(nx!=my):
        print("undefined")
    else:
        result=[[0 for i in range(mx)] for j in range(ny)]
        for i in range(0,mx,1):
            for j in range(0,ny,1):
                for k in range(0,my,1):
                    result[i][j]+=intorfloat(matrixX[i][k])*intorfloat(matrixY[k][j])
        if(len(result)!=len(result[0])):
            print("undefined")
        else:
            newresult=[[0 for i in range(len(result))] for j in range(len(result))]
            for i in range(len(result)):         #反矩陣轉換
                for j in range(len(result)):
                    if(i!=j):
                        newresult[i][j]=-1*result[i][j]
                    else:
                        newresult[j][i]=result[i][j]
            temp=newresult[0][0]
            newresult[0][0]=newresult[1][1]
            newresult[1][1]=temp
            print("F-1=")
            for i in range(len(result)):   #output F-1
                print("[",end="")
                for j in range(len(result)):
                    newresult[i][j]=intorfloat(newresult[i][j]/(result[0][0]*result[1][1]-result[1][0]*result[0][1]))
                    print(newresult[i][j],end=" ")
                print("]")
            print("F*F-1=")
            Multiply(2,2,2,2,result,newresult)   #F*F-1
            print("F*F-1 equals to I")
    print()
def intorfloat(num):   #判斷資料型態並轉換
    if(isinstance(num,int)):
        return int(num)
    elif(isinstance(num,float)):
        if(int(num)==float(num)):
            return int(num)
        else:
            return float(num)
    else:
        for i in range(len(num)):
            if(num[i]=='.'):
                return float(num)
        return int(num)
def Multiply(mx,nx,my,ny,matrixX,matrixY):   #乘法
    if(nx!=my):
        print("undefined")
    else:
        result=[[0 for i in range(mx)] for j in range(ny)]
        for i in range(0,mx,1):
            for j in range(0,ny,1):
                for k in range(0,my,1):
                    result[i][j]+=intorfloat(matrixX[i][k])*intorfloat(matrixY[k][j])
        for i in range(0,mx,1):
            print("[",end="")
            for j in range(0,ny,1):
                print(intorfloat(result[i][j]),end=" ")
            print("]")
    print()
def Transpose(m,n,matrix=[]):   #轉置
    transmatrix=[]
    for i in range(n):
        for j in range(m):
            print(matrix[j][i],end=" ")
        print()
    print()
    """for i in range(0,len(transmatrix)):
        for j in range(len(transmatrix[i])):
            print(transmatrix[i][j],end=" ")
        print()
    print()"""
    
def Aminus2C(ma,na,mc,nc,matrixA=[],matrixC=[]):
    if(ma!=mc or na!=nc):
        print("undefined")
    else:
        result=[[0 for i in range(ma)] for j in range(na)]
        for i in range(ma):
            print("[",end="")
            for j in range(na):
                print(intorfloat(matrixA[i][j])-2*intorfloat(matrixC[i][j]),end=" ")
            print("]")
    print()
  
def AplusB(ma,na,mb,nb,matrixA=[],matrixB=[]):
    if(ma!=mb or na!=nb):
        print("undefined")
    else:
        for i in range(ma):
            print("[",end="")
            for j in range(na):
                print(intorfloat(matrixA[i][j])+intorfloat(matrixB[i][j]),end=" ")
            print("]")
    print()

def check(matrix=[]):     #判斷是否有pi or log
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j][0]=='l'):   #log運算
                print(matrix[i][j][-1])
                matrix[i][j]=float(math.log10(int(matrix[i][j][-1]))) #取出數字  
            elif(matrix[i][j][0]=='p'):  #pi運算
                matrix[i][j]=float(math.pi)

def main():
    matrixA=[['1','2'],['-3','-4'],['5','6']];
    matrixB=[['1','-2','-3'],['-4','5','6']];
    matrixC=[['2','-1'],['pi','log2'],['-2','6']];
    check(matrixA)  #檢查有無pi or log
    check(matrixB)  #檢查有無pi or log
    check(matrixC)  #檢查有無pi or log
    print("(a)")
    print("A+B=")
    AplusB(3,2,2,3,matrixA,matrixB)
    print("A-2C")
    Aminus2C(3,2,3,2,matrixA,matrixC)
    print("A^T=")
    Transpose(3,2,matrixA)
    print("(b)")
    print("E=")
    Multiply(3,2,2,3,matrixA,matrixB)
    print("F=")
    Multiply(2,3,3,2,matrixB,matrixA)
    print("G=")
    Multiply(3,2,3,2,matrixA,matrixC)
    print("(c)")
    multiplyinverse(2,3,3,2,matrixB,matrixA)
main()