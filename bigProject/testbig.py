#调用官方库


from scipy.sparse import *
import matplotlib.pyplot as plt
# matplotlib.rcParams['font.family'] = 'SimHei'
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
import numpy as np





def generateA (n):
    offset = np.array([0,-1,1])
    line1 = []#以后赋值多用array少用list
    line2 = []
    for i in range(n):
        line1.append(2)
        line2.append(-1)
    data = np.array([line1,line2,line2])
    A = dia_matrix((data,offset),shape = (n,n),dtype=np.float64)
    #cnmcnmccnmcnmcnmcnmcnmcnmcnmc我真是服了注意你的变量类型
    #A = dia_matrix(np.eye(100))
    A = lil_matrix(A)
    A[0,99] = 100
    A[0,0] = 100
    for i in range(n):
        if i != (n-1)/2 or i != n/2:
            print(i,n-i-1)
            A[i, n-i-1] = 2.8#cnmcnmccnmcnmcnmcnmcnmcnmcnmc我真是服了
            print(A[i, n-i-1])      
    return lil_matrix(A) 
print(generateA(100).toarray())


# def generateb(n):
#     b = np.zeros((1,n))
#     b[0,0] = 3
#     b[0,n-1] = 3
#     for i in list(range(n))[1:-1]:
#         b[0,i] = 2
#     for i in [int((n)/2-1),int((n)/2)]:#注意这个地方是n-1,而且别忘了凡是除法自动返回浮点数
#         b[0,i] = 1
#     return b

# print(generateb(100000))