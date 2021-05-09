"""
#五子棋

檢查10*10五子棋可以構成5個連為一線的位置。
1表示有放棋子，0表示沒有放旗子。
----------------------------------
輸入說明
輸入10*10的資料
-----------------------------
輸出說明
可構成5個連為一線的位置。例如
0 0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 1 1 1 1
0 0 0 0 1 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 1 1 1 1 0 0 0 0
0 0 0 1 0 0 0 0 0 0
可以增加5個連為一線，以下圖表示。
0 0 0 0 0 0 x 0 1 0
0 0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 x 1 1 1 1
0 0 0 0 1 0 1 0 0 0
0 0 0 x 0 0 x 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 x 1 1 1 1 x 0 0 0
0 0 0 1 0 0 0 0 0 0
其位置為
0 6
3 5
5 3
5 6
8 1
8 6
---------------------
SampleInput:
0 0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 1 1 1 1
0 0 0 0 1 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 1 1 1 1 0 0 0 0
0 0 0 1 0 0 0 0 0 0
Sample Output:
0 6
3 5
5 3
5 6
8 1
"""
def check(ans,data,x,y):
    for i in range (5):
        if data[i] == 0 and data.count(0) == 1 :
            ans.append([y,x+i])
            #print('check')
    return ans
def check2(ans,data,x,y):
    for i in range (5):
        if data[i] == 0 and data.count(0) == 1 :
            ans.append([x+i,y])
            #print('check2')
    return ans    
def check3(ans,data,x,y):
    for i in range(5):
        if data[i] == 0 and data.count(0) == 1 :
            ans.append([y+i,x+i])
            #print('check3')
    return ans
def check4(ans,data,x,y):
    for i in range(5):
        if data[i] == 0 and data.count(0) == 1 :
            ans.append([x+i,y+i])
            #print('check4')
    return ans
    
def check5 (ans,data,x,y):
    for i in range(5):
        if data[i] == 0 and data.count(0) == 1 :
            ans.append([x-i,y+i])
            #print('check5')
    return ans   
def check6 (ans,data,x,y):
    for i in range(5):
        if data[i] == 0 and data.count(0) == 1 :
            ans.append([x-i,y+i])
            #print('check6')
    return ans
    
def column (x,i):
    a=[]
    for j in range (10):
        x1=[]
        for k in range (i,i+5,1):
            x1.append(int(x[j][k]))        
        a=check(a,x1,i,j)     
    return a    
def row (x,i):
    a=[]
    for j in range (10):
        x1=[]
        for k in range (i,i+5,1):
            x1.append(int(x[k][j]))        
        a=check2(a,x1,i,j)     
    return a    
def slash(x,i):
    a=[];aans=[]
    for j in range (6-i):
        x1=[]
        for k in range (5):
            x1.append(int(x[j+k+i][j+k]))        
        a=check3(a,x1,j,j+i)
    return a
def slash2(x,i):
    a=[]
    for j in range (6-i):
        x1=[]
        for k in range (5):
            x1.append(int(x[j+k][j+k+i]))
        a=check4(a,x1,j,j+i)
    return a
 
def slash3(x,i):    
    a=[]
    for j in range (i,6):
        x1=[]
        for k in range (5):
            x1.append(int(x[9-j-k][i+k]))
        a=check5(a,x1,9-j,i)
    return a        
def slash4(x,i):
    a=[]
    for j in range (i):
        x1=[]
        for k in range(5):
            x1.append(int(x[9-j-k][i+k]))
        a=check6(a,x1,9-j,i)
    return a       
def main():
    x=[];aans=[];ans=[];a=0
    for i in range (10):
        x.append(list(input().split()))       
    for i in range (6):
        ans.extend(slash3(x,i))
        ans.extend(column(x,i))
        ans.extend(row(x,i))
        ans.extend(slash(x,i))
    for i in range (1,6):
        ans.extend(slash2(x,i))
        ans.extend(slash4(x,i)) 
    k=len(ans) 
    while a<=k:
        for i in range (a+1,len(ans)-1):
            if ans[a][0]==ans[i][0] and ans[a][1]==ans[i][1]:
                k=len(ans)
                del ans[a]
                a=0
                
        a+=1
    ans.sort()
    print('')
    for i in range (len(ans)):
        print('%d %d'%(ans[i][0],ans[i][1]))
main()