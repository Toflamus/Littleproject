# 相遇问题：
# 北京和济南两地相距420km， a从北京出发， 时速80km/h， b从济南出发， 时
# 速60km/h， 问两人多长时间相遇， 相遇位置距北京多远
# 要求： 时间精度取0.01小时， 用计算机思维而非数学思维解决问题， 用turtle库
# 模拟相遇的过程， 文档形式提交（ 运行过程截图、 思路及总结等）
# 提示： turtle库支持两支画笔同时作画

#思路：
#经过简单数学计算可以得知一共需要3h相遇
#时间精度0.01h那么数据需要变化300次
#假设每次北京车每次前进像素0.8，济南车每次前进像素0.6
#然后判断相遇条件当两者距离小于等于10的时候就可以停止了（为了清晰我将两者的x轴错开了10）
#最后只需统计行走路程要当两者相遇的时候打印出来即可。
import turtle
#setup
turtle.setup(650,350,200,200)
a=turtle.Pen()
b=turtle.Pen()

#define const
aspeed=0.8
bspeed=0.6

# a.xcor("red")
a.penup()
a.pensize(5)
a.goto(240,5)
a.pendown()
a.pencolor('blue')
# a.speed(0.8)

# b.xcor('blue')
b.penup()
b.pensize(5)
b.pencolor('red')
b.goto(-180,-5)
b.pendown()
# b.speed(0.6)
i=0
while(abs(a.pos()-b.pos())>10.002):
    # print(abs(a.pos()-b.pos()))
    a.fd(aspeed)
    b.fd(bspeed)
    a.seth(180)
    xa=i*aspeed
    xb=i*bspeed
    # time.sleep(0.001)
    i+=1
print("the time consume is {:.2f}h".format(int(i/100)))
print('the distance to Beijing is {:.0f}'.format(int(xa)))

