#这是一个对numpy库的实验

import numpy as np


# a = np.ones((4,5))
# print (a)
# print(a.dtype)
a = [1,2,3]
b = [5,5,6]
c = [7,8,9]
mrx = np.array([a,b,c],dtype = int)
print(mrx)
me = np.indices((4,5))
print(me)
print(mrx.reshape(1,9))
print(np.empty((3,4),int))