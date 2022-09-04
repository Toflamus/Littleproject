# radius=25
# area=3.1415*radius*radius
# print(area)
# print("{:.2f}".format(area))

# import turtle
# turtle.pensize(2)
# turtle.circle(10)
# turtle.circle(20)
# turtle.circle(60)
# turtle.circle(160)
# turtle.circle(200)

from turtle import *
fillcolor("red")
begin_fill()
while True:
   forward(200)
   right(144)
   print(abs(pos()))#最后一个print会输出一个科学计数法，这是因为其中的运算都是以浮点数运算的这是五次浮点运算的误差
   
   if abs(pos())<1:
        break
end_fill()

