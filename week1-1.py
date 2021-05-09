"""
#計算總成績、平均

某一學生修國文、計算機概論、計算機程式設計三科，使用者輸入名字（一個char）、學號（int）、三科成績(int)。
(1) 計算學生總成績、平均。
(2) 印出名字、學號、總成績、平均。
Input
K
905067
100
100
100
Output
Name:K
ID:905067
Average:100
Total:300
"""
def getAverageScore(csi, pd, ch):
    average = (csi + pd + ch)//3
    return average

def getSumScore(csi, pd, ch):
    sum=(csi+pd+ch)
    return sum
 
def main():
    name = input()
    id = int(input())
    csi = int(input())
    pd = int(input())
    ch = int(input())
    averageScore = getAverageScore(csi, pd, ch)
    sumScore=getSumScore(csi, pd, ch)
    print("Name:%s" %name)
    print("ID:%d" %id)
    print("Average:%d" %averageScore)
    print("Total:%d" %sumScore)
    
main()

