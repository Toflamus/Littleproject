
# dic = {"y":'y1','x':'x1'}
# it = dic.items()
# print(it)
# ls = list(dic.items())#这样只会输出key的
# print(ls[0])

# import jieba
# #jieba.add_word('卷帘大将')
# words = jieba.lcut('我是卷帘大将')
# print(words)
# #本测试说明这个加入的词如果比本来的词长会按照加入的词来

# tex = ['\n','12','我是']
# for i in range(3):
#     print(type(eval(tex[i])))#不能print会报错
#     print(type(tex[i]))

# tex = ['12']
# for i in range(1):
#     try:
#         print(type(eval(tex[i])))#这样可以print
#     except:
#         continue

# tex = ['\n','12']
# for i in range(2):
#     print(type(eval(tex[i])))#不能print会报错
#     print(type(tex[i]))


# tex = ['\n','12','我是']
# for i in range(3):
#     try:
#         print(type(eval(tex[i])))#这样可以print,卧槽完美
#     except:
#         continue

# print(type(28/2))