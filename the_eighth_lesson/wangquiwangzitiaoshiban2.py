#定义常量
import random
import math

roundlimit = 6
roundsep = 5


def printIntro():
    print("This programme will do a simple simulation of a tennis match.")
    print('Simply input the probabilities of the service round of two players and the basic rules')
    print('the winner and detail data will be print out')


def get_input():#返回值已经处理好了
    name1 = input("please input the first player's name,we assume the first player serving first ")
    pro1 = float(input('the probabilities[0,1] of the service round of first player '))
    
    name2 = input("please input the second player's name ")
    pro2 = float(input('the probabilities[0,1] of the service round of second player '))
    try:
        assert pro1<=1,pro1>0 
        assert pro2<=1,pro2>0
    except:
        print('你的输入有问题不在0-1之间')
    setnum = input("how many set they played")
    rule = input('they use tiebreak or not?if yes input 1 if not input 0')                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    try:
        assert rule == '1' or '0'
    except:
        print('你的规则没有按照指示方法输入')
    return name1,float(pro1),name2,float(pro2),int(setnum),int(rule)

def semround(pro1,pro2):#普通对局#命令行调试出了问题只会出现
    score1,score2 = 0,0
    int(score1)
    int(score2)
    serving = True
    i = 0
    gameover = False
    while not gameover:
        if serving:
            if random.random()<float(pro1):
                score1 += 1
            else:
                serving = False
        else:
            if random.random()<float(pro2):
                score2 += 1
            else:
                serving = True
        i += 1
        if score1 ==4 or score2 == 4:
            if  abs(score1 - score2) > 1:
                gameover = True
        if score1>4 or score2>4:
            if abs(score1 - score2) == 2:
                gameover = True
    ratio = [0,0]
    ratio[0] = score1
    ratio[1] = score2
    return ratio


def tiebreak(pro1,pro2):#抢七决胜局
    score1,score2 = 0,0
    int(score1)
    int(score2)
    serving = True

    i = 0
    gameover = False
    while not gameover:
        if math.ceil(i/2)%2 != 0:
            serving = True
        else:
            serving = False 

        if serving:
            if random.random()<pro1:
                score1 += 1
        else:
            if random.random()<pro2:
                score1 += 1
        i += 1
        if score1 ==7 or score2 == 7:
            if  abs(score1 - score2) > 1:
                gameover = True
        if score1>6 or score2>6:
            if abs(score1 - score2) == 2:
                gameover = True
    ratio = [0,0]
    ratio[0] = score1
    ratio[1] = score2
    return ratio


def semoneset(pro1,pro2,rule):#一盘比赛
    bigroundsocre_ls = [0,0]
    roundscore_dic = {}
    ratio = []
    i=0#计数器
    while i<=9:#10局以内分胜负
        ratio = semround(pro1,pro2)#对于每一个非决胜局，都会返回一个比分列表
        roundscore_dic[i+1] = ratio
        if  ratio[0]>ratio[1]:
            bigroundsocre_ls[0] = bigroundsocre_ls[0] +1
        if  ratio[0]<ratio[1]:
            bigroundsocre_ls[1] = bigroundsocre_ls[1] +1
        if  bigroundsocre_ls[0] == roundlimit or bigroundsocre_ls[1] == roundlimit:
            return bigroundsocre_ls,roundscore_dic #单出口问题
        i += 1

    else:#没有在10局以内分胜负就是55平
        try:
            assert bigroundsocre_ls[0] == bigroundsocre_ls[1] and bigroundsocre_ls[0] == roundsep
        except:
            print("比分不是5：5，说明你的算法有问题")
        while i <= 11:#又进行两把比赛
            ratio = semround(pro1,pro2)
            roundscore_dic[i+1] = ratio
            if  ratio[0]>ratio[1]:
                bigroundsocre_ls[0] = bigroundsocre_ls[0] +1
            if  ratio[0]<ratio[1]:
                bigroundsocre_ls[1] = bigroundsocre_ls[1] +1
            i+=1
       #进行完两把比赛之后
        if abs(bigroundsocre_ls[0]-bigroundsocre_ls[1]) == 2:
            return bigroundsocre_ls,roundscore_dic
        elif abs(bigroundsocre_ls[0]-bigroundsocre_ls[1]) == 0:
            if rule:#决胜局采用tiebreak
                ratio = tiebreak(pro1,pro2)
                roundscore_dic[i+1] = ratio
                i += 1
            else:#决胜局不采用tiebreak
                while abs(bigroundsocre_ls[0]-bigroundsocre_ls[1]) <2:
                    ratio = semround(pro1,pro2)#决胜局独有函数
                    roundscore_dic[i+1] = ratio
                    if  ratio[0]>ratio[1]:
                        bigroundsocre_ls[0] = bigroundsocre_ls[0] +1
                    if  ratio[0]<ratio[1]:
                        bigroundsocre_ls[1] = bigroundsocre_ls[1] +1
                    i+=1
            return bigroundsocre_ls,roundscore_dic          
        else:
            print('你的算法在长短比分的时候有问题')    
                   

def semmatch(pro1,pro2,setnum,rule):#整局比赛
    bigsetscore_ls = [0,0]#大比分几盘比几盘
    setscore_dic = {}#每盘每局每回合
    for i in range(setnum):
        bigroundscore_ls = [0,0]#第一个是A第二个是b
        roundscore_dic = {}
        bigroundscore_ls,roundscore_dic = semoneset(pro1,pro2,rule)#预计这个函数return一个列表和字典，列表是每盘的比分，字典是每局每回合
        if bigroundscore_ls[0] > bigroundscore_ls[1]:
                bigsetscore_ls[0] = bigsetscore_ls[0] +1
        if bigroundscore_ls[0] < bigroundscore_ls[1]:
                bigsetscore_ls[1] = bigsetscore_ls[1] +1
        setscore_dic[i+1] = roundscore_dic
        if bigsetscore_ls[0] == math.ceil(setnum/2) or bigsetscore_ls[1] == math.ceil(setnum/2):
            break
    return bigsetscore_ls,setscore_dic


def printelegantly(bigscore_ls,
        setscore_dic):
    print("大比分（盘数）是{}:{}".format(bigscore_ls[0],bigscore_ls[1]))
    for i in range(bigscore_ls[1]+bigscore_ls[0]):
        maximunkey =  max(list(setscore_dic[i+1].keys()))
        for j in range(maximunkey):
            print("第{}盘第{}局的比分是{}:{}".format(i+1,j+1,setscore_dic[i+1][j+1][0],setscore_dic[i+1][j+1][1]))


def printoutput(name1,name2,bigscore_ls,setscore_dic):
    winner = True
    if bigscore_ls[0]<bigscore_ls[1]:
        winner = False
    if winner:
        print('The Winner is ',name1)
    else:
        print('The Winner is ',name2)
    printelegantly(bigscore_ls,setscore_dic)


def main():
    printIntro()
    name1,pro1,name2,pro2,setnum,rule = get_input()
    bigscore_ls = []
    setscore_dic = {}
    bigscore_ls,setscore_dic = semmatch(pro1,pro2,setnum,rule)
    printoutput(name1,name2,bigscore_ls,setscore_dic)
    return 0
main() 
