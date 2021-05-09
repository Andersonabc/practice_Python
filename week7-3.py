"""
#找出正整數之加法表達方式

所有的正整數都可以以連續的正整數相加的和來表達。
例如: 9有3種表達方式
2+3+4
4+5
9
給一個正整數N(N>0)，請計算出N有多少種以連續的正整數相加的和來表達的方式。
輸入說明:
輸入一個正整數N (N>0)
輸出說明:
輸出有哪幾種相加方式。
輸出順序由小到大。
不合法的輸入則輸出E。
"""
def main ():
    try:
        i=1
        a=int(input())
        if a>0:
            while i <=a :
                x=0
                list1=[]
                for j in range (i,a+1,1):
                    x+=j
                    if x < a:
                        list1.append(str(j))
                    elif x==a:
                        list1.append(str(j))
                        i+=1
                        print('+'.join(list1))
                        break
                    else:
                        i+=1
                        break
        else:
            print('E')
    except ValueError:
        print('E')               
main()                