from pickletools import optimize
import scipy as scp
import numpy as np

x = np.array([4568,5820,6525,7400,9045,10350,11050,11820,12850,13840])
y = np.array([0.00399,0.00386,0.0368,0.0362,0.0349,0.0339,0.0341,0.0323,0.0324,0.0321])

def liquidfunction(p):
    a,b,c = p
    return y-a*(x**b) +c

r = scp.optimize.leastsq(liquidfunction,[0.5,-0.1,0.001],maxfev = 2000)
# a,b,c = r[0]
print(r)
#备注
#第一次调试打印出来
# RuntimeWarning: Number of calls to function has reached maxfev = 800.
#   warnings.warn(errors[info][0], RuntimeWarning)
#(array([-2.11148887e+10, -3.22142729e+00, -3.60868337e-02]), 5)
#出现一个warning还有最后的莫名其妙的整数，官网文档一查发现了warning的含义就是到了上限没有迭代出来改成2000迭代出来
#ier int
#An integer flag. If it is equal to 1, 2, 3 or 4, the solution was found. Otherwise, the solution was not found. In either case, the optional output variable ‘mesg’ gives more information.

