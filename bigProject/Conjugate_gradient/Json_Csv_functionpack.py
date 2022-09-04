
#调用官方库
from array import array

import matplotlib
import matplotlib.pyplot as plt
# matplotlib.rcParams['font.family'] = 'SimHei'
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
import numpy as np


def writejson(pendtowrite_dic,filenpath_str):
    #这个函数可以通过读取写入的一行的信息以及文件名来写入json格式的文件
    #这里传入的列表或者字典应该是类似{k:[x0,x1,x2...r]}的
    #这里我采取相对路径否则换个电脑可能会出错
    fileobject = open(filenpath_str,'at',encoding='UTF-8')
    fileobject.writelines(str(pendtowrite_dic)+'\n')
    fileobject.close()
    return 0


def read_json_print_table(filepath_str):
    #这个函数可以行读取json中的内容转换成并输出成表格的一行
    # 读入的数据有类似"[k,[x0,x1,x2...r]]\n"的形式
    #打开并读取一行
    file_obj = open(filepath_str,'rt',encoding='utf-8')
    
    notprint = True
    for line_str in file_obj:
        
        #删除\n
        line_str = line_str.replace('\n','')
        line_dic = eval(line_str)
        value_lls = list(line_dic.values())
        key_ls = list(line_dic.keys())
        #打印表头
        if notprint:
            j = 0
            print('k|',end='')
            for i in value_lls[0][0:-1]:
                print('x{}          '.format(j),end='')
                j += 1
            print('r            ',end='')
            print('\n')
            #打印表线
            for i in value_lls[0]:
                print('-'*12,end='')
            print('\n')
            notprint = False

        print(key_ls[0],end='|')
        for i in value_lls[0]:
            print('{:<12.8f}'.format(i),end='')
        print('\n')
    file_obj.close()


def get_key_and_r(filename_str):
    #把奇怪数据结构中的key和r单独取出变成列表
    file_obj = open(filename_str,'rt',encoding='utf-8')
    key = []
    r_value = []
    for line_str in file_obj:
        #删除\n
        line_str = line_str.replace('\n','')
        line_dic = eval(line_str)
        lstvalue = list(line_dic.values())[-1][-1]
        keynum = list(line_dic.keys())[0]
        key.append(keynum)
        r_value.append(lstvalue)
    return key,r_value


def minulogten(list):#这个函数直接给你把list中的每一个元素全部变成10负对数
    for i in range(len(list)):
        list[i] = np.log10(1/abs(list[i]))    
    return list










    

