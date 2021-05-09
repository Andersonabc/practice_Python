def change(s,i,j,n,int_factor):
    for str_ans in range(1,5-n):
     if(j-str_ans>=0):
      if(s[i][j-str_ans]=='1'):
       int_factor=int_factor+1
    return int_factor
def test(s):
    str_ans=''
    ans_sheet=[]
    for i in range(10):
     for j in range(10):
      int_factor=0
      if(s[i][j]=='0'):
       for n in range(4):
        if(j+n+1<10):
         if(s[i][j+n+1]=='1'):
          int_factor=int_factor+1
         else:
          int_factor=change(s,i,j,n,int_factor)
          break
        else:
          int_factor=change(s,i,j,n,int_factor)
          break
      if(int_factor==4):
       str_ans=str(i)+' '+str(j)
       ans_sheet.append(str_ans)
    return s,ans_sheet
def check5 (ans,data,x,y):
    for i in range(5):
        if data[i] == 0 and data.count(0) == 1 :
            ans.append([x-i,y+i])
            #print('check5')
    return ans 
def test1(s,ans_sheet):
    s1=[]
    s2=[]
    for j in range(10):
     int_factor=''
     for i in range(10):
      int_factor=int_factor+s[i][j]
     s1.append(int_factor)
    s1,c1=test(s1)
    for i in range(len(c1)):
     c1[i]=c1[i][::-1]
    ans_sheet.extend(c1)
    for j in range(10):
     str_ans=''
     for i in range(10):
      str_ans=str_ans+s1[i][j]
     s2.append(str_ans)
    return s2,ans_sheet
def check6 (ans,data,x,y):
    for i in range(5):
        if data[i] == 0 and data.count(0) == 1 :
            ans.append([x-i,y+i])
            #print('check6')
def test2(s,ans_sheet):
    s1=[]
    for j in range(10):
     int_factor=''
     for i in range(9,-1,-1):
      int_factor=int_factor+s[i][j]
     s1.append(int_factor)
    c1=test3(s1)
    for i in range(len(c1)):
     c1[i]=c1[i][::-1]
     int_factor=list(c1[i])
     int_factor[0]=str(9-int(c1[i][0]))
     c1[i]=''.join(int_factor)
    ans_sheet.extend(c1)
    return ans_sheet
def test3(s):
    str_ans=''
    ans_sheet=[]
    for i in range(10):
     for j in range(10):
      int_factor=0
      if(s[i][j]=='0'):
       for n in range(4):
        if(j+n+1<10 and i+n+1<10):
         if(s[i+n+1][j+n+1]=='1'):
          int_factor=int_factor+1
         else:
          int_factor=lalala(s,i,j,n,int_factor)
          break
        else:
          int_factor=lalala(s,i,j,n,int_factor)
          break
      if(int_factor==4):
       str_ans=str(i)+' '+str(j)
       ans_sheet.append(str_ans)
    return ans_sheet
def lalala(s,i,j,n,int_factor):
    for str_ans in range(1,5-n):
     if(i-str_ans>=0 and j-str_ans>=0):
      if(s[i-str_ans][j-str_ans]=='1'):
       int_factor=int_factor+1
    return int_factor
def check4(ans,data,x,y):
    for i in range(5):
        if data[i] == 0 and data.count(0) == 1 :
            ans.append([x+i,y+i])
            #print('check4')
    return ans  
def main():
    s=[]
    for i in range(10):
     int_factor=input()
     str_ans=int_factor.replace(' ','')
     s.append(str_ans) 
    s,ans_sheet=test(s)
    s,ans_sheet=test1(s,ans_sheet)
    c2=test3(s)
    c2=test2(s,c2)
    ans_sheet.extend(c2)
    c1=list(set(ans_sheet))
    c1.sort()
    print('')
    for i in range(len(c1)):
     print(c1[i])
main()