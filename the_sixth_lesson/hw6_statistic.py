import jieba
import math 
jieba.add_word('甲醇流量')
jieba.add_word('甲醇温度')
def aver(ls):
    j = 0
    for i in ls:
        j+=float(i)#这里报错ls中元素是字符串
    ave = j/len(ls)
    return ave

def med(ls):
    length = len(ls)
    #print(length)
    if length%2 == 0 :
        # med = (ls[length/2]+ls[length/2+1])/2#注意错误写法注意数组的从零开始里面会有减一
        med = (ls[int(length/2)]+ls[int(length/2-1)])/2#这里报错说我的indices必须是整数为什么我这个
    else :
        med = ls[(length-1)/2]
    return med

def dev(ls, ave):
    addsqu = 0
    for i in ls:
        addsqu += (float(i)-ave)**2#python中是两个**表示乘方
    de = math.sqrt(addsqu/(len(ls)))
    return de    

def maxof(ls):
    maxo = ls[0]
    for i in ls:
        if i>=maxo:
            maxo = i 
    return maxo

def minof(ls):
    mino = ls[0]
    for i in ls:
        if i <= mino:
            mino = i
    return mino


shuju = open('MTO.txt','r',encoding='utf-8').read()
words1 = list(jieba.lcut(shuju))
#print(words1)#输出发现这个包括所有的换行符号以及字段之类，并且都是字符串的格式
j = 0
num = []
#print(words1)
for i in range(len(words1)) :#提取其中的数字
    #print(words1[i])
    #num[j] = words1[i]#列表增加值要用函数蹦年这么直接搞
    try:
        if type(eval(words1[i])) is float: 
            num.append(float(words1[i]))#可以解决字符串报错问题
            j+=1
    except:
        continue
#print(num)
liuliang = num.copy()
del liuliang[0::2]
wendu = num.copy()
del wendu[1::2]
#print(wendu)
#print(liuliang)
print('甲醇流量的平均值',aver(liuliang))
print('甲醇流量的中位数',med(liuliang))
print('甲醇流量的标准差',dev(liuliang,aver(liuliang)))
print('甲醇流量的最大值',maxof(liuliang))
print('甲醇流量的最小值',minof(liuliang))
print('甲醇温度的平均值',aver(wendu))
print('甲醇温度的中位数',med(wendu))
print('甲醇温度的标准差',dev(wendu,aver(wendu)))
print('甲醇温度的最大值',maxof(wendu))
print('甲醇温度的最小值',minof(wendu))





