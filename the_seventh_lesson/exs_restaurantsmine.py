
from tkinter.simpledialog import askstring


fr = open("restaurantdata.txt",'rt',encoding='UTF-8')
fw = open("restaurantdataout.csv",'at',encoding='UTF-8')

keyset = set()

def collectkey(stri):#这个函数配合下面的for循环取出所有的key,另外别用tm的str作为变量名
    diction = eval(stri)#我在这里报错，断点调试说dictionary update sequence element #0 has length 1; 2 is required因为dict()的函数注释是新建一个字典，rnm退钱！！！！！！！！
    
    #list = diction.key()#这个地方报错dict没有性质key，你他妈认真点keys！！！
    list = diction.keys()
    setlist = set(list)
    global keyset
    keyset = keyset.union(setlist)
    return keyset

def buwan(j,lol):#这个函数补完列表的没有的餐馆returnu一个全新的totallist
    diction = eval(lol)
    global totalkey
    for caiguan in totalkey:
    
        diction[caiguan] = diction.get(caiguan,0)
    global totallist
    totallist[j].insert(1,str(diction))
    totallist[j].pop(2)#替换元素
    return totallist
    
def sortdic (j,lol):#这个函数给每个dic排个序
    diction = eval(lol)
    listofdic = list(diction.items())
    listofdic.sort(key = lambda x:x[0],reverse = False)
    strlistofdic = str(dict(listofdic))#这边竟然能直接把一个二元对变成字典，不难理解为什么上面会报错

    global totallist
    totallist[j].insert(1,strlistofdic)
    totallist[j].pop(2)#替换元素

   



totallist = []#这里创建一个包含列表的列表
cntline = 0  #数一下一共几行然后后面对于每一行来增加字典
for line in fr:#这里报错了一个说fr没有length为啥？？？？？？？fr的数据类型好像很奇怪
    linelist = line.replace("\n",'')
    complete_split = linelist.split("-")#完全split
    #print(complete_split)
    totallist.append(complete_split)#这里将split的字符串给加入进去。
    #目前正常，先在totallist是一个等差,但是我发现会把‘\n’之类的也放进去，那么如何处理这个\n就是一个问题，也就是如何按照多种方式split，可以先全replace正常了再split。运行成功
    #print(totallist)#经过修改后运行成功
    collectkey(complete_split[1])
    cntline+=1#调试半天，发现tm没有改变totallist，也不报错，后来发现根本没进下面的循环，你tm不改cntline值
#print(keyset)#print成功yeah，目前已经创建了一个涵盖所有餐馆的set
totalkey = list(keyset)#我惊了竟然可以直接转
for j in range(cntline):
    #for caiguan in totalkey: #菜馆
        #buwan(totallist[1])
    #totallist[2*i][caiguan] =  totallist[2*i].get(caiguan,0)
    #print(totallist)   #为啥没加进去，因为totallist第二个元素是字符串o，shit
    #buwan(j,totallist[2*j-1])#这个地方注意减一草又忘了从零开始但是问题不在这totallist是一个列表的列表
    buwan(j,totallist[j][1])#这里j不用-1
#print(totallist)#woc 我快哭出来了，卧槽终于调试成功了
#现在totallist是一个无序的东西，如何排序呢
#主要还是得重新写一下totallist把第二个先转换成列表然后再排序

for j in range(cntline):
    sortdic(j,totallist[j][1])

#print(totallist)运行成功，雷姆,现在totallist已经符合输出的格式了剩下的就是搞一个程序把那个点user和函数值搞到一个列表里面
totalkey.sort(key = None ,reverse= False)
fw.write('人名,'+str(totalkey)[1:-1]+'\n')

for j in range(cntline):
    alist = []
    #blist = eval(totallist[j][1]).values()
    #del blist[0:13]#dict_values' object does not support item deletion哎呦我真是服了列表不让删
    #只能切片了
    bstr = str(eval(totallist[j][1]).values())
    bstr = bstr[13:]#删除dict_values
    astr = totallist[j][0]+','+bstr#注意加括号，注意values，注意eval
    astr = astr[:-2]#删除)]
    #ok了兄弟们print(alist)#中间有个dict_values很烦
    fw.write(str(astr)+'\n')
fw.close()


