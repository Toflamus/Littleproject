#调用官方库
from tkinter import N
import scipy.sparse as sp 
import matplotlib.pyplot as plt
# matplotlib.rcParams['font.family'] = 'SimHei'
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
import numpy as np
from Json_Csv_functionpack import *
import datetime
#需要统计运算时间的代码
def generateA (n):
    # offset = np.array([0,-1,1])
    # line1 = []
    # line2 = []
    # for i in range(n):
    #     line1.append(2)
    #     line2.append(-1)
    #    # np.append(data[0],[2])
    #    # np.append(data[1],[-1])
    #    # np.append(data[2],[-1])

    # data = np.array([line1,line2,line2])

    # B = sp.dia_matrix((data,offset),shape = (n,n))#注意里面是一个tuple#100000会爆栈
    A = sp.dok_matrix((n,n),dtype=np.float64)#注意要使用array
        # A = sp.dok_matrix(,dtype = np.float64,shape = (n,n))
    #A = np.zeros((n,n),dtype = np.float64)
    for i in range(n):
        #print(A.toarray())
        if i != (n-1)/2 or i != n/2:#这里注意这个全部减一的顺序
            A[i, n-i-1] = 0.5 #这里要舍掉1还要再舍掉1#他说对角矩阵不支持修改
        A[i,i] = 2.5
    for i in list(range(n))[1:]:
        A[i,i-1] = -1
    for i in list(range(n)[0:-1]):
        A[i,i+1] = -1
     
    return sp.lil_matrix(A) 
#print(generateA(10))

def generateb(n):
    b = np.zeros((1,n))
    b[0,0] = 3
    b[0,n-1] = 3
    for i in list(range(n))[1:-1]:
        b[0,i] = 2
    for i in [int((n)/2-1),int((n)/2)]:#注意这个地方是n-1,而且别忘了凡是除法自动返回浮点数
        b[0,i] = 1
    return b.T
#print(generateb(10))

def generatex0(n):
    x0 = np.empty((1,n))
    #x0 = np.matrix(np.random.rand(n))
    return x0.T
#print(generatex0(10))


def CGIte(mrx_A_array,vec_b_array,vec_x0_array,accuracy,CGIfile):

    #准备部分
    xkplus = vec_x0_array*2
    xk = vec_x0_array
    
    rkplus = vec_b_array - mrx_A_array @ xk
    rk = vec_b_array - mrx_A_array @ xk

    pkplus = vec_b_array - mrx_A_array @ xk
    pk = vec_b_array - mrx_A_array @ xk
    
    k = 0

    #notstop = True
    while np.linalg.norm(rk,ord = np.inf) > accuracy and pk.T @ (mrx_A_array @ pk)  > accuracy :
    #while np.linalg.norm(xkplus - xk,ord = np.inf) > accuracy  :
        #建立几个临时储存的结构，在循环内部建立每次刷新,然后写入文件。这样在大量迭代的时候不会占用过多内存
        store_dic = {}
        store_ls = []
        #运算部分
        # a = np.dot(rk.T,rk)
        # b = np.dot(pk,(mrx_A_array @ pk))
        a = rk.T @ rk
        b = pk.T @ (mrx_A_array @ pk)
        #alphak =np.dot(rk.T,rk) /np.dot(pk.T,mrx_A_array @ pk)#?????????????
        alphak = a/b
        # alphak = a/b
        xkplus = xk + alphak * pk
        rkplus = rk - alphak * (mrx_A_array @ pk)
        batak = (rkplus.T @ rkplus)/(rk.T @ rk)
        pkplus = rkplus + batak * pk
        #存储部分
            #本次储存只需要把r写进去就行
        c = rkplus.sum(axis = 1)#把一个矩阵变成列表
        store_ls.append(np.linalg.norm(c,ord = np.inf))#把r加入到列表最后#把r加入到列表最后
        #print(store_ls)
        store_dic[k] = store_ls#这里储存好了一个字典
        writejson(store_dic,CGIfile)    

        #迭代交换值的部分
        
        
        xk = xkplus.copy()
        rk = rkplus.copy()
        pk = pkplus.copy()

        #计数部分
        k += 1 
        # and np.linalg.norm(rkplus,ord = np.inf) <= accuracy
        #判断循环是否进行部分
        #if rk.T @ rk <= accuracy or pk.T @ (mrx_A_array @ pk)  <= accuracy:
            #notstop = False# SparseEfficiencyWarning: Comparing a sparse matrix with a scalar greater than zero using <= is inefficient, try using > instead.
                            #warn(bad_scalar_msg, SparseEfficiencyWarning)
    #由于计算数据写入了文件中不需要return
    return 0


def main():
    #定义一些常量
    #定义常量
    accuracy = 0.000001
    n = [100,1000,10000,100000]
    
    CG_figeur = []
    for i in n:
        #生成初始值
        ori_A = generateA(i)
        #print(ori_A.toarray())#为什么不让我修改lil啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        ori_b = generateb(i) 
        
        ori_x0 = generatex0(i)
        
        #生成文件名
        filename = 'bigProject\Conjugate_gradient\CGdata{}.txt'.format(i)
        #时间统计上
        starttime = datetime.datetime.now()
        #清空file
        file = open(filename, 'w').close()
        #进行迭代
        CGIte(ori_A,ori_b,ori_x0,accuracy,filename)
        #时间统计下
        endtime = datetime.datetime.now()
        interval=(endtime - starttime).microseconds
        print("When calculating n = {} , computer takes {} microseconds ".format(i,interval))
        CG_figeur.append(get_key_and_r(filename))

    

    plt.figure(figsize=(5, 2.7), layout='constrained')  
    
        # Plot some data on the axes.
        # s0 = plt.plot(sor_fig[0][0], minulogten(sor_fig[0][1]), label='SOR w = {}'.format(w[0]) ) 
        # s1 = plt.plot(sor_fig[1][0], minulogten(sor_fig[1][1]), label='SOR w = {}'.format(w[1]) ) 
        # s2 = plt.plot(sor_fig[2][0], minulogten(sor_fig[2][1]), label='SOR w = {}'.format(w[2]) ) 
        # s3 = plt.plot(sor_fig[3][0], minulogten(sor_fig[3][1]), label='SOR w = {}'.format(w[3]) ) 
        # s4 = plt.plot(sor_fig[4][0], minulogten(sor_fig[4][1]), label='SOR w = {}'.format(w[4]) )CG
        # plt.plot(CG_figeur, minulogten(CG_figeur[0][1]), label='CG w =0.8' )
    s1 = plt.plot(CG_figeur[0][0], minulogten(CG_figeur[0][1]), label='CG n = 100' ) 
    s2 = plt.plot(CG_figeur[1][0], minulogten(CG_figeur[1][1]), label='CG n = 1000') 
    s3 = plt.plot(CG_figeur[2][0], minulogten(CG_figeur[2][1]), label='CG n = 10000') 
    s4 = plt.plot(CG_figeur[3][0], minulogten(CG_figeur[3][1]), label='CG n = 100000') 
    
    plt.xlabel('k')  # Add an x-label to the axes.
    plt.ylabel(r'$-\lg_{}{r}$')  # Add a y-label to the axes.
    plt.title("CGIte")  # Add a title to the axes.
    plt.legend();  # Add a legend.
    plt.show()
main()