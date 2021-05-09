 """
#橋牌

撲克牌四種花色分別是黑桃、紅心、磚塊、梅花，定義 A~D。
撲克牌數字1~13，與四種花色共有52張牌。
編碼規則為數字+花色，例如 1A 表示黑桃 A、7C 表示磚塊 7，13D 表示梅花 K。
花色大小：黑桃>紅心>方塊>梅花
數字大小：2最小，A最大
輸入說明:
共有P1、P2、P3、P4
P1、P3一組，P2、P4一組
1. 每人先發13張牌
2. 先叫牌，由P1開始叫牌，叫到成局(決定王牌花色)為止，最多叫到3墩
3. 成局後出牌，由成局人的下一位(順時針)開始出牌，
所有人出完牌後開始比牌，此回合比牌最高者獲得一墩，
且成為下一輪出牌者，共玩三輪。
輸出說明:
由P1~P4依序輸出墩數，輸出獲勝組玩家。
錯誤狀況
1.叫牌未依照規則，則輸出ERROR
2.出牌時，第一位出牌的人決定花色，若是沒有同花色才能出別的花色，
若違反則輸出ERROR 。
3.出牌時出自己沒有的牌
Input :
2A 12B 1B 13D 11A 8A 10A 3D 1D 4D 10D 12A 3B
8B 1A 1C 13C 4A 9A 7B 7C 8C 12C 9D 12D 13B
10B 5C 5D 2D 4B 5B 9B 3C 9C 10C 7D 11D 8D
3A 2B 5A 2C 7A 6B 11B 4C 11C 6A 6C 6D 13A
1A //P1開始叫牌(順時針)
2D
2B
pass
pass
3C
pass
pass
pass //成局 王牌花色為C(磚塊)，成局人為P2，叫牌階段結束
10B 2B 12B 8B //P3(成局人下一位)出牌，所以出牌順序是P3 P4 P1 P2
11A 1A 5C 5A //P1(獲勝者)出牌，所以出牌順序是 P1 P2 P3 P4
5D 6D 3D 12D //P3(獲勝者)出牌，所以出牌順序是 P3 P4 P1 P2
說明:
第一局 10B 2B 12B 8B 大小順序為 2B <8B < 10B < 12B，此局P1獲勝，P1獲得一墩
第二局 11A 1A 5C 5A 大小順序為 5A < 11A < 1A <5C，此局P3獲勝，P3獲得一墩
第三局 5D 6D 3D 12D 大小順序為 3D < 5D < 6D < 12D，12D(王牌花色)最大，
此局P2獲勝，P2獲得一墩。
output :
1
1
1
0
P1 P3 //P2成局人隊伍墩數不足於3墩，所以另一隊(P1 P3)獲勝
---------------------------------------
input:
2A 12B 1C 13D 11A 8A 10A 6C 10C 4D 10D 13A 13C
8B 2B 7A 11C 4A 9A 7B 7C 5C 12C 9D 12D 13B
10B 8C 5D 6A 4B 5B 9B 5A 3C 9C 1D 7D 12A
3A 3B 2C 1A 6B 11B 4C 1B 2D 11D 3D 6D 8D
1C
1A
2D
2B
pass
pass
pass //P4贏 花色B(紅心)
8A 4A 12A 1A //P1 P2 P3 P4
2C 1C 5C 5A // P4 P1 P2 P3，P3手中還有花色Ｃ牌，違反出牌原則
2A 9A 12A 3A
output:
ERROR
--------------------------------------------
input:
2A 12B 1C 13D 11A 8A 10A 6C 10C 4D 10D 13A 13C
8B 2B 7A 11C 4A 9A 7B 7C 5C 12C 9D 12D 13B
10B 8C 5D 6A 4B 5B 9B 5A 3C 9C 1D 7D 12A
3A 3B 2C 1A 6B 11B 4C 1B 2D 11D 3D 6D 8D
1C
1A
2D
2B
2C //違反
pass
pass
pass
8A 4A 12A 1A
2C 1C 5C 5A
2A 9A 12A 3A
output:
ERROR
"""
def game(score_1,score_2,score_3,score_4,firstplayer,Cards_Player1,Cards_Player2,Cards_Player3,Cards_Player4,round,error,king):
    temporary=[]
    suits_Player1=[card[-1]for card in Cards_Player1]
    suits_Player2=[card[-1]for card in Cards_Player2]
    suits_Player3=[card[-1]for card in Cards_Player3]
    suits_Player4=[card[-1]for card in Cards_Player4] 

    gamecard=['','','','']    
    if firstplayer == 1 :
        gamecard[0]=round[0]
        gamecard[1]=round[1]
        gamecard[2]=round[2]
        gamecard[3]=round[3]
    elif firstplayer == 2 :
        gamecard[1]=round[0]
        gamecard[2]=round[1]
        gamecard[3]=round[2]
        gamecard[0]=round[3]         
    elif firstplayer == 3 :
        gamecard[2]=round[0]
        gamecard[3]=round[1]
        gamecard[0]=round[2]
        gamecard[1]=round[3]         
    elif firstplayer == 4 :
        gamecard[3]=round[0]
        gamecard[0]=round[1]
        gamecard[1]=round[2]
        gamecard[2]=round[3]
         

    #print(Cards_Player1)
    #print(Cards_Player2)
    #print(Cards_Player3)
    #print(Cards_Player4)

    for i in range (4):
        if gamecard[i] == '14A':
            temporary.append('1A')
        elif gamecard[i] == '14B':
            temporary.append('1B')
        elif gamecard[i] == '14C':
            temporary.append('1C')
        elif gamecard[i] == '14D':
            temporary.append('1D')
        else:
            temporary.append(gamecard[i])
            
        
    #for i in range (4):
    #    print(temporary[i])
    gamecard_suit=[mm[-1] for mm in gamecard]
    gamecard_num=[mm.replace(mm[-1],'')for mm in gamecard]
    #print(gamecard_suit,gamecard_num)
    
    #print(gamecard_num)
    #print(gamecard_suit)
    biggest_suit=gamecard_suit[0]
    biggest=int(gamecard_num[0])
    #print(biggest)
    #print(biggest_suit)
    #print(error)

        #print('NO1')
        #for i in range (4):
         #   print(gamecard_suit[i])
        #print(suits_Player1)
        #print(suits_Player2)
        #print(suits_Player3)
        #print(suits_Player4)        
    if (not temporary[0] in Cards_Player1 or not temporary[1] in Cards_Player2 or not temporary[2] in Cards_Player3 or not temporary[3] in Cards_Player4):
        error=1
        #print('NO2')
        #for i in range (4):
         #   print(gamecard[i])
        #print(Cards_Player1)
        #print(Cards_Player2)
        #print(Cards_Player3)
        #print(Cards_Player4)
        return score_1,score_2,score_3,score_4,firstplayer,Cards_Player1,Cards_Player2,Cards_Player3,Cards_Player4,error
    #if (gamecard_suit[0]==gamecard_suit[1]==gamecard_suit[2]==gamecard_suit[3]):
    for i in range (3):
        if  biggest_suit!=king[-1] and gamecard_suit[i+1]==king[-1]:
            biggest=int(gamecard_num[i+1])
            biggest_suit=gamecard_suit[i+1]
        elif biggest_suit!=king[-1] and gamecard_suit[i+1]!=king[-1]:
            if gamecard_suit[i+1] == biggest_suit:
                if int(gamecard_num[i+1])>biggest :
                    biggest=int(gamecard_num[i+1])
                    biggest_suit=gamecard_suit[i+1]
            elif gamecard_suit[i+1]!=biggest_suit:
                biggest=biggest
        elif biggest_suit == king[-1] and gamecard_suit[i+1]!=king[-1]:
            biggest=biggest
        elif biggest_suit == king[-1] and gamecard_suit[i+1]== king[-1]:
            if int(gamecard_num[i+1])>biggest :
                biggest=int(gamecard_num[i+1])
                biggest_suit=gamecard_suit[i+1]
        #print(biggest)
        #print(biggest_suit)
            
    winner=gamecard.index(str(biggest)+str(biggest_suit))
    firstplayer=winner+1
    #print(firstplayer)
    if winner == 0:
        score_1+=1
    elif winner==1:
        score_2+=1
    elif winner==2:
        score_3+=1
    elif winner ==3:
        score_4+=1
    else:
        error=1 
        return 0
        
    Cards_Player1.remove(temporary[0])
    Cards_Player2.remove(temporary[1])
    Cards_Player3.remove(temporary[2])
    Cards_Player4.remove(temporary[3])    
    return score_1,score_2,score_3,score_4,firstplayer,Cards_Player1,Cards_Player2,Cards_Player3,Cards_Player4,error
    
def main():
    turn=0
    winnerrr=''
    daddy=0
    score_1=0
    score_2=0
    score_3=0
    score_4=0
    players=[]
    playboard=[]
    error=0
    for i in range(4):
        players.append(list(input().split()))
    Cards_Player1=players[0]
    Cards_Player2=players[1]
    Cards_Player3=players[2]
    Cards_Player4=players[3]
    round=0
    firstplayer=1
    king=''
    while round < 3 :
        desideking=input()
        desidekingnum=desideking[0]
        turn+=1
        if firstplayer == 5:
            firstplayer=1
        if desideking == 'pass':
            round+=1
        elif king=='':
            king=desideking
        else:
            round=0
            if king!='' :
                kingnum=king[0]
                if kingnum > desidekingnum :
                    error=1
                elif kingnum == desidekingnum and king[-1]=='A' and (desideking[-1]=='A' or desideking[-1]=='B' or desideking[-1]=='C' or desideking[-1]=='D'):
                    error=1
                elif kingnum == desidekingnum and king[-1]=='B' and (desideking[-1]=='B' or desideking[-1]=='C' or desideking[-1]=='D'):
                    error=1
                elif kingnum == desidekingnum and king[-1]=='C' and (desideking[-1]=='C' or desideking[-1]=='D'):
                    error=1
                elif kingnum == desidekingnum and king[-1]=='D' and desideking[-1]=='D':
                    error=1
                else :
                    king=desideking
        
        firstplayer+=1
    if firstplayer == 5:
        firstplayer=1
    daddy=firstplayer
    firstplayer+=1
    if firstplayer == 5:
        firstplayer=1    
    #print(king)
    for i in range (3):
        playboard.append(list(input().split()))
    for i in range(3):
        for j in range(4):
            if playboard[i][j]=='1A':
                playboard[i][j]='14A'
            elif playboard[i][j]=='1B':
                playboard[i][j]='14B'
            elif playboard[i][j]=='1C':
                playboard[i][j]='14C'
            elif playboard[i][j]=='1D':
                playboard[i][j]='14D'
    round_1=playboard[0]
    round_2=playboard[1]
    round_3=playboard[2]
    if error != 1 or turn>12:
        score_1,score_2,score_3,score_4,firstplayer,Cards_Player1,Cards_Player2,Cards_Player3,Cards_Player4,error=game(score_1,score_2,score_3,score_4,firstplayer,Cards_Player1,Cards_Player2,Cards_Player3,Cards_Player4,round_1,error,king)
    if error != 1 or turn>12:
        score_1,score_2,score_3,score_4,firstplayer,Cards_Player1,Cards_Player2,Cards_Player3,Cards_Player4,error=game(score_1,score_2,score_3,score_4,firstplayer,Cards_Player1,Cards_Player2,Cards_Player3,Cards_Player4,round_2,error,king)
    if error !=1 or turn>12:
        score_1,score_2,score_3,score_4,firstplayer,Cards_Player1,Cards_Player2,Cards_Player3,Cards_Player4,error=game(score_1,score_2,score_3,score_4,firstplayer,Cards_Player1,Cards_Player2,Cards_Player3,Cards_Player4,round_3,error,king)
        
    if((daddy==2 or daddy==4) and int(king[0])<=(score_2+score_4)):
        winnerrr='P2 P4'
    elif((daddy==1 or daddy==3) and int(king[0])<=(score_1+score_3)):
        winnerrr='P1 P3'
    elif((daddy==2 or daddy==4) and int(king[0])> (score_2+score_4)):
        winnerrr='P1 P3'
    elif((daddy==1 or daddy==3) and int(king[0])> (score_1+score_3)):
        winnerrr='P2 P4'

    
    if error ==1 or turn>12:
        print('ERROR')
    else :
        print(score_1)
        print(score_2)
        print(score_3)
        print(score_4)
        print(winnerrr)

main()