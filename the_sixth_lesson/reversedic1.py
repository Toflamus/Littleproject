#字典翻转输出
# 描述
# 读入一个字典类型的字符串，反转其中键值对输出
# 即输入：key.value,输出value.key
# 输出格式输入错误
# 输出格式：字典





def reversedic(dic):
    copydic = dic
  #lsvalue = list(dic.values())
    #lskey = list(dic.keys())
    #lsvalue.reverse()
    #lskey.reverse()  
    redic = {}
    for key in dic:#字典只会取出key
        redic[dic[key]]  =key 
    return redic


dic = eval(input('please enter a dcitionary'))#后输入两个一样的key会使得后面覆盖前面
if (dic is dict):
    #print(len(set(dic.values())),len((dic.values())))
    if len(set(dic.values())) == len((dic.values())):
        dicn = reversedic(dic)
        print(dicn)
    #else:
        print("输入错误")
else:
    print("输入错误")
#print(dic)
