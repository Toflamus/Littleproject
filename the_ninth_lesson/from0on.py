import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
import numpy as np

# plt.figure(figsize=(8,4),facecolor= 'blue',edgecolor="red")
# plt.axes([0,0,0.6,0.6])
# a = plt.subplot(2,3,4)
# #plt.subplots_adjust(0.5,0.5)
# plt.legend(a,a,'what’sthat')
# plt.show()

x = np.linspace(0,6,100)
y = np.cos(2*np.pi*x)*np.exp(-x)+0.8
plt.plot(x,y,'k',color = 'r',linewidth = 3, linestyle = '-')
plt.show()