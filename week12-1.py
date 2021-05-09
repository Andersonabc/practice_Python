"""
#撲克牌

撲克牌四種花色分別是黑桃、紅心、磚塊、梅花，定義 S, H, D, C。
牌面數字2~13，A為 14，共有52張牌。
花色大小：黑桃>紅心>方塊>梅花。
編碼規則為數字+花色，例如 10S 表黑桃 10、7D 表磚塊 7，12C 表梅花 Q。
撲克牌遊戲把單一張牌命名為單張，沒有任何花色牌型，編號 0。
兩張數字一樣的命名為 Pair，編號 1。
2 組 pair 的牌稱為 Two pair，編號 2。
三張一樣的稱為 Three of a Kind，編號 3。
數字連續的5張牌稱為 Straight，包括 13 ,14, 2, 3, 4，編號 4。
Three of a Kind 加一個 Pair 稱為 Full House，編號 5。
四張一樣稱為 Four Of A Kind，編號 6。
數字連續的5張且花色一樣稱為 Straight Flush，編號 7。
輸入5張撲克牌，判斷哪一類型的牌形編號(0~7)。
輸入說明 ：
第一列輸入為5個編碼分別由空格分開，表示5張撲克牌。
輸出說明 ：
輸出為一個0~7的整數，代表牌型編號。
Input:
-------------------------
9D 8C 8S 8H 9S
Output:
------------------------
5
"""

def check(data,suit):
    newdata=[]
    con=[data.count(num) for num in data]
    for i in data:
        if i > 10 :
            newdata.append(i)
        else:
            newdata.append(i+13)   
    newdata.sort()
    data.sort()
    if suit[0]==suit[1]==suit[2]==suit[3]==suit[4] :
        if newdata[0]+4==newdata[1]+3==newdata[2]+2==newdata[3]+1==newdata[4] or data[0]+4==data[1]+3==data[2]+2==data[3]+1==data[4]:
            print('7')       
            return 0
    if con.count(2)==4:
        print('2')
    elif con.count(2)==2:
        if con.count(3)==3:
            print('5')
            return 0
        print('1')
    elif con.count(3)==3:
        print('3')        
    elif con.count(4)==4:
        print('6')
    elif newdata[0]+4==newdata[1]+3==newdata[2]+2==newdata[3]+1==newdata[4] or data[0]+4==data[1]+3==data[2]+2==data[3]+1==data[4]:
        print('4')
    else:
        print('0')
    
def main():
    data=list(input().split())
    data2=sorted([int(num.replace(num[-1],'')) for num in data ])
    suit=[num[-1] for num in data]
    check(data2,suit)
    
main()
    
