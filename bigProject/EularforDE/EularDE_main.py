#调用官方库
from array import array
import matplotlib
import matplotlib.pyplot as plt
import numpy as np




#def write_data_in_file(pending_dic,filename):



def Iterateonce (mrx,cn_array,h):
    cnplus_hat_array = cn_array + h * mrx @ cn_array
    cnplus_array = cn_array + 1/2 * h * mrx @ (cn_array + cnplus_hat_array) 
    return cnplus_array

def Iteratelots(mrx,c0_array,h,totalt):
    times = int(totalt/h)
    data_dic = {}
    
    cn_array = c0_array
    n = 0
    data_dic[n*h] = cn_array
    for i in range(times):
        n += 1
        cn_array = Iterateonce(mrx,cn_array,h)
        data_dic[n*h] = cn_array
    
    return data_dic

def drawelegantly(data_dic):
    t = data_dic.keys()
    concentration = data_dic.values()
    plt.style.use('_mpl-gallery')
    #plt.style.use('seaborn')
    # plt.style.use('seaborn')
    # plt.style.use('seaborn')

    plt.figure(figsize=(5, 2.7), layout='constrained')

    s0 = plt.plot(t, concentration, label=('ca','cb','cc','cd') ) 
    
    plt.xlabel('t/hour')  # Add an x-label to the axes.
    plt.ylabel('c percentage')  # Add a y-label to the axes.
    plt.title("Reaction Graph")  # Add a title to the axes.
    plt.legend();  # Add a legend.
    plt.show()


def main():
    #定义常量
        #物质的量分数
    ca0 = 0.1119
    cb0 = 0.4313
    cc0 = 0.3613
    cd0 = 0.0955
    c0_array = np.array([ca0,cb0,cc0,cd0])
        #速率常熟（单位h^-1）
    k1 = 0.393
    k2 = 0.186
    k3 = 0.237
    k4 = 0.101#单位为
    mrx = np.array([[-k1,0,0,0],[k1,-(k2+k3),0,0],[0,k2,-k4,0],[0,k3,k4,0]])#最后别忘大括号
        #时间
    h = 0.0005#hour
    totalt = 3#hour
    data_dic = Iteratelots(mrx,c0_array,h,totalt)
    drawelegantly(data_dic)
    

main()