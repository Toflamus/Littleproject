#调用官方库
from array import array


import matplotlib
import matplotlib.pyplot as plt
# matplotlib.rcParams['font.family'] = 'SimHei'
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
import numpy as np
from Json_Csv_functionpack import *



#一下两个函数并没有甚么用
def inputA():#这个函数可以获得并返回一个矩阵
    mrx_A_str = input("请使用列表的形式输入你的矩阵")
    mrx_A_array = np.array(mrx_A_str)
    return mrx_A_array

def inputb():#这个函数可以获得并返回一个向量
    vec_b_str = input('请使用列表的格式输入你的向量')
    vec_b_array = np.array(vec_b_str)
    return vec_b_array


def JacobiIte(mrx_A_array,vec_b_array,vec_x0_array,accuracy,jacobifile):
    
    mrx_U_array = - np.triu(mrx_A_array,1)#严格上三角负阵
    mrx_L_array = - np.tril(mrx_A_array,-1)#严格下三角负阵
    mrx_D_array = mrx_A_array + mrx_U_array + mrx_L_array#对角部分
    mrx_Drev_array = np.linalg.inv(mrx_D_array)

    mrx_B_array = mrx_Drev_array @ (mrx_L_array+mrx_U_array)
    vec_f_array = mrx_Drev_array @ (vec_b_array)
    k = 0#迭代次数计数器
    vec_x_array = vec_x0_array#用来存储xn的
    vec_y_array = vec_x0_array#用来存储xn+1的
    
    notstop = True
    while notstop :
        #建立两个临时储存的结构，在循环内部建立每次刷新,然后写入文件。这样在大量迭代的时候不会占用过多内存
        store_dic = {}
        store_ls = []
        
        vec_y_array = mrx_B_array @ vec_x_array + vec_f_array
        r = np.linalg.norm((vec_y_array - vec_x_array),ord = np.inf)
        #存储部分
        # store_ls = list(vec_y_array).append(r)
        store_ls = vec_y_array.tolist()
        store_ls.append(r)#把r加入到列表最后#把r加入到列表最后
        store_dic[k] = store_ls#这里储存好了一个字典
        writejson(store_dic,jacobifile)
        #迭代交换值的部分
        vec_x_array = vec_y_array
        #计数部分
        k += 1
        #计算部分
        #判断循环是否进行部分
        if r <= accuracy:
            notstop = False
    #由于计算数据写入了文件中不需要return
    return 0
    

def SORIte(mrx_A_array,vec_b_array,vec_x0_array,accuracy,w,SORfile):
    mrx_U_array = - np.triu(mrx_A_array,1)#严格上三角负阵
    mrx_L_array = - np.tril(mrx_A_array,-1)#严格下三角负阵
    mrx_D_array = mrx_A_array + mrx_U_array + mrx_L_array#对角部分
    
    mrx_Lw_array = (np.linalg.inv(mrx_D_array - w * mrx_L_array)) @ ((1-w) * mrx_D_array + w * mrx_U_array)
    vec_f_array = w * (np.linalg.inv(mrx_D_array - w * mrx_L_array)) @ vec_b_array

    k = 0#迭代次数计数器
    vec_x_array = vec_x0_array#用来存储xn的
    vec_y_array = vec_x0_array#用来存储xn+1的
    notstop = True

    while notstop :
        #建立两个临时储存的结构，在循环内部建立每次刷新,然后写入文件。这样在大量迭代的时候不会占用过多内存
        store_dic = {}
        store_ls = []
        
        #计算部分
        vec_y_array = mrx_Lw_array @ vec_x_array + vec_f_array
        r = np.linalg.norm((vec_y_array - vec_x_array),ord = np.inf)
        #存储部分
        store_ls = vec_y_array.tolist()
        store_ls.append(r)#把r加入到列表最后
        store_dic[k] = store_ls#这里储存好了一个字典
        writejson(store_dic,SORfile)
        #迭代交换值的部分
        vec_x_array = vec_y_array
        #计数部分
        k += 1
        #判断循环是否进行部分
        if r <= accuracy:
            notstop = False
    #由于计算数据写入了文件中不需要return
    return 0



def main():
    #首先先定义一波各种参数
    #文件名
    Jacobifile = 'Python_configurition\\bigProject\Jacobi_SOR_Iteration\Jacobidata.txt'
    SORfile =['Python_configurition\\bigProject\Jacobi_SOR_Iteration\SORdata0.txt','Python_configurition\\bigProject\Jacobi_SOR_Iteration\SORdata1.txt','Python_configurition\\bigProject\Jacobi_SOR_Iteration\SORdata2.txt',
    'Python_configurition\\bigProject\Jacobi_SOR_Iteration\SORdata3.txt','Python_configurition\\bigProject\Jacobi_SOR_Iteration\SORdata4.txt']
    
    
    #定义常量
    accuracy = 0.000001
    w = [0.8,1,1.2,1.4,1.6]
    #题目中所给的矩阵和向量
    ori_A = (np.array([11,4,-5,-1,10,-3,-3,-17,14])).reshape(3,3)
    ori_b = np.array([6,3,-8]) 
    ori_x0 = np.array([0,0,0])#好像不用转置
    #每次执行清空文件中内容
    file = open(Jacobifile, 'w').close()

    JacobiIte(ori_A,ori_b,ori_x0,accuracy,Jacobifile)
    read_json_print_table(Jacobifile)
    jaco_fig = get_key_and_r(Jacobifile)#用来绘图的数据元组
    
    #打印表格
    j = 0
    sor_fig = []
    for i in w:
        file = open(SORfile[j], 'w').close()
        SORIte(ori_A , ori_b , ori_x0 , accuracy , i ,SORfile[j])
        read_json_print_table(SORfile[j])
        sor_fig.append(get_key_and_r(SORfile[j]))#用来绘图的数据元组列表
        j+=1
    


    #这是一个优雅的绘图函数
    #自变量是一个列表[(x1,y1),]
    #列表中是一个元组元组中的每一个元素是列表，可以！
    
    
    # fig,ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    # ax.plot(jaco_fig[0], minulogten(jaco_fig[1]), label='Jacobi')  # Plot some data on the axes.
    # ax.plot(sor_fig[0][0], minulogten(sor_fig[0][1]), label='SOR w = {}'.format(w[0]) ) 
    # ax.plot(sor_fig[1][0], minulogten(sor_fig[1][1]), label='SOR w = {}'.format(w[1]) ) 
    # ax.plot(sor_fig[2][0], minulogten(sor_fig[2][1]), label='SOR w = {}'.format(w[2]) ) 
    # ax.plot(sor_fig[3][0], minulogten(sor_fig[3][1]), label='SOR w = {}'.format(w[3]) ) 
    # ax.plot(sor_fig[4][0], minulogten(sor_fig[4][1]), label='SOR w = {}'.format(w[4]) ) 
    
    
    # ax.set_xlabel('k')  # Add an x-label to the axes.
    # ax.set_ylabel(r'$-\log_{10}{r}$')  # Add a y-label to the axes.
    # ax.set_title("Jacobi&SOR Ite")  # Add a title to the axes.
    # ax.legend();  # Add a legend.
    # plt.show()

    plt.figure(figsize=(5, 2.7), layout='constrained')
    j1 = plt.plot(jaco_fig[0], minulogten(jaco_fig[1]), label='Jacobi')  
   
    # Plot some data on the axes.
    # s0 = plt.plot(sor_fig[0][0], minulogten(sor_fig[0][1]), label='SOR w = {}'.format(w[0]) ) 
    # s1 = plt.plot(sor_fig[1][0], minulogten(sor_fig[1][1]), label='SOR w = {}'.format(w[1]) ) 
    # s2 = plt.plot(sor_fig[2][0], minulogten(sor_fig[2][1]), label='SOR w = {}'.format(w[2]) ) 
    # s3 = plt.plot(sor_fig[3][0], minulogten(sor_fig[3][1]), label='SOR w = {}'.format(w[3]) ) 
    # s4 = plt.plot(sor_fig[4][0], minulogten(sor_fig[4][1]), label='SOR w = {}'.format(w[4]) ) 
    
    s0 = plt.plot(sor_fig[0][0], minulogten(sor_fig[0][1]), label='SOR w =0.8' ) 
    
    s1 = plt.plot(sor_fig[1][0], minulogten(sor_fig[1][1]), label='SOR w = 1' ) 
    s2 = plt.plot(sor_fig[2][0], minulogten(sor_fig[2][1]), label='SOR w = 1.2') 
    s3 = plt.plot(sor_fig[3][0], minulogten(sor_fig[3][1]), label='SOR w = 1.4') 
    s4 = plt.plot(sor_fig[4][0], minulogten(sor_fig[4][1]), label='SOR w = 1.6') 
    
    plt.xlabel('k')  # Add an x-label to the axes.
    plt.ylabel(r'$-\lg_{}{r}$')  # Add a y-label to the axes.
    plt.title("Jacobi&SOR Ite")  # Add a title to the axes.
    plt.legend();  # Add a legend.
    plt.show()

    

main()