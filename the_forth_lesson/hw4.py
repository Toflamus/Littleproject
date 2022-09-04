#分析
#输入：一个公式，可以使用eval转换成语句
#处理：两种方式：梯形面积法和Monte Carle法
#输出：一个积分值
from math import *
from random import *
#常量定义
infimum=0#定义下确界
supremum=1#定义上确界
accuration = 0.01#定义精度
Darts = 10000#定义Monte Carlo方法的镖数
#自带9个函数库
Linear = 'x'
Early_Pause = 'x+(1-sin(x*pi*2+pi/2)/(-8))'
Late_Pause = 'x+(1-sin(x*pi*2+pi/2)/8)'
Slow_Wavy = 'x+sin(x*pi*5)/20'
Fast_Wavy = 'x+sin(x*pi*20)/80'
Power = '(x+(1-x)*0.03)**2'
Inverse_Power = '1-(1-x)**1.5'
Fast_Power = '(x+(1-x)/2)**8'
Inverse_Fast_Power = '1-(1-x)**3'

funclib = [Linear,Early_Pause,Late_Pause,Slow_Wavy,Fast_Wavy,Power,Inverse_Power,Fast_Power,Inverse_Fast_Power]
#函数定义

def determiny(function,x):
    y=eval(function)
    return y
def calbyArea(function):
    Area = 0
    i=infimum
    while i<=supremum:
        x=i
        yi=eval(function)
        j=i+accuration
        x=j
        yj=eval(function)
        Area+=(yi+yj)*accuration*0.5
        i+=accuration
    return Area
def calbyMon(function,Darts):
    m = determiny(function,infimum)
    n = determiny(function,supremum)
    hits=0
    for i in range(Darts+1):
        x=uniform(infimum,supremum)
        y=uniform(m,n)
        if y<=determiny(function,x):
            hits+=1        
    total_area = (supremum-infimum)*(n-m)
    Area = total_area * (hits/Darts)
    return Area
#执行命令
for i in range(9):
    functionStr=funclib[i]
    Area=calbyMon(functionStr,Darts)
    Brea=calbyArea(functionStr)
    print('使用MO方法，函数f(x)='+functionStr+"在[{},{}]".format(infimum,supremum)+"上的定积分是{}".format(Area))
    print('使用一般方法，函数f(x)='+functionStr+"在[{},{}]".format(infimum,supremum)+"上的定积分是{}".format(Brea))

functionStr = input("现在您可以输入想要测试的函数")
infimum = eval(input('定义域下界是(非负)'))
supremum = eval(input('定义域上界是（非负）'))
Area=calbyMon(functionStr,Darts)
Brea=calbyArea(functionStr)
print('使用MO方法，函数f(x)='+functionStr+"在[{},{}]".format(infimum,supremum)+"上的定积分是{}".format(Area))
print('使用一般方法，函数f(x)='+functionStr+"在[{},{}]".format(infimum,supremum)+"上的定积分是{}".format(Brea))
