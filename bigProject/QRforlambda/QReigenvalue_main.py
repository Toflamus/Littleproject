#调用官方库



from fileinput import filename
import matplotlib
import matplotlib.pyplot as plt
# matplotlib.rcParams['font.family'] = 'SimHei'
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
import numpy as np 
import scipy.sparse as sp
from Json_Csv_functionpack import *








def qrfactorizationIte(mrx_A_array,accuracy,qrfile):

    #准备部分
    akplus = mrx_A_array
    ak = mrx_A_array
    lak = np.tril(ak,-1)#获得A的下三角部分
    lamol =np.linalg.norm(lak,ord = np.inf)#A下三角部分的无穷范数
    k = 0

    
    while lamol> accuracy :
        #建立几个临时储存的结构，在循环内部建立每次刷新,然后写入文件。这样在大量迭代的时候不会占用过多内存
        store_dic = {}
        store_ls = []
        #运算部分
        q,r = np.linalg.qr(ak)
        akplus = r @ q
        lak = np.tril(ak,-1)#获得A的下三角部分
        lamol =np.linalg.norm(lak,ord = np.inf)
        #把无穷范数变成10的负对数
        lamollog10 = np.log10(1/abs(lamol))

        #存储部分
        
        store_ls.append(lamollog10)
        # print()
        store_dic[k] = store_ls#这里储存好了一个字典
        writejson(store_dic,qrfile)    

        #迭代交换值的部分
        
        ak = akplus.copy()
        eigenvalue = np.diag(r, 0)
        #计数部分
        k += 1 
    return eigenvalue






def main():
    A = np.array([[6,7,8,7],[4,7,6,5],[5,2,10,6],[3,5,8,9]])
    #使用三种不同的方法制造矩阵，但是可能后续会面临数据结构的问题
    # B = np.array([[5,-1,0,0,0],[-1,4.5,0.2,0,0],
    # [0,0.2,1,-0.4,0],[0,0,-0.4,3,1],[0,0,0,1,3]])

    line1B = [5,4.5,1,3,3]
    line2B = [-1,0.2,-0.4,1,0]
    line3B = [0,-1,0.2,-0.4,1]
    dataB = np.array([line1B,line2B,line3B])
    offsetB = np.array([0,-1,1])
    B = sp.dia_matrix((dataB,offsetB),shape=(5,5))
    B = B.toarray()

    # lineC = [1,1/2,1/3,1/4,1/5,1/6,1/7,1/8,1/9,1/10,1/11]
    # dataC = np.array([lineC,lineC,lineC,lineC,lineC,lineC,lineC,lineC,lineC,lineC,lineC])
    # offsetC = np.array([0,-1,1,-2,2,-3,3,-4,4,-5,5])
    # C = sp.dia_matrix((dataC,offsetC),shape = (6,6))

    C = np.zeros((6,6))
    for i in range(6):
        for j in range(6):
            C[i,j] = 1/(i+j+1)

    QR_figeure = []
    #定义常量
    accuracy = 0.000001
    n = [A,B,C]

    #进行测试

    for i in range(len(n)):
        filename  = 'bigProject\QRforlambda\QRforeigenvalue{}'.format(i)

        file = open(filename, 'w').close()

        eigenvalue = qrfactorizationIte(n[i],accuracy,filename)
        print('the eigenvalue attay for matrix {} is {}'.format(i,eigenvalue))
        QR_figeure.append(get_key_and_r(filename))


    plt.figure(figsize=(5, 2.7), layout='constrained')   
    s1 = plt.plot(QR_figeure[0][0], QR_figeure[0][1], label='QR_A' ) 
    s2 = plt.plot(QR_figeure[1][0], QR_figeure[1][1], label='QR_B') 
    s3 = plt.plot(QR_figeure[2][0], QR_figeure[2][1], label='QR_C') 
    #s4 = plt.plot(QR_figeure[3][0], minulogten(QR_figeure[3][1]), label='QR n = 100000') 
    
    plt.xlabel('k')  # Add an x-label to the axes.
    plt.ylabel(r'$-\lg_{}{L}$')  # Add a y-label to the axes.
    plt.title("QRIte")  # Add a title to the axes.
    plt.legend();  # Add a legend.
    plt.show()
main()