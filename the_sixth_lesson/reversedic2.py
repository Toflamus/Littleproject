s = input("输入字典")
try:
    d= eval(s)
    e= {}
    assert type(d) == type(e)#assertTrue无事发生False则直接报错
    for k in d:
        e[d[k]]=k
        print(e)
except:
    print("输入错误")

    