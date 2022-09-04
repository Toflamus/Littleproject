# for i in range(101):
#     if i%7==0 and i%5!=0:
#         print(i)

#99乘法表
# for i in range(1,10):
#     for j in range(1,10):
#         if i>=j:
#             print("{0:2}*{1:2}={2:2}\t".format(i,j,i*j),end="")
#     print('\n')

#计算小于100的最大素数
# primemax=2
# for i in range(2,101)：
#     for j in range(2,i+1):
#         if i%j!=0:
#             if j==i-1:
#                 primemax=i
#         else:
#             break
# print(primemax)

#完全可以倒着来，判断第一个就:可以了
# primemax=None
# for i in range(100,2,-1):
#     for j in range(2,i):
#         if i%j!=0:
#             if j==i-1:
#                 primemax=i
                
#         else:
#             break
#     if primemax!=None:
#         break
# print(primemax)

#编写代码输出由*组成的菱形图案

num=int(input('请输入图形大小'))
max=2*num+1
star="*"
for i in range(num):
    s=star*(2*i+1)
    font=" "*(num-1-i)
    print(" "*(num-1-i),end="")
    print(star*(2*i+1),end="")#format 不支持变量作为宽度
    print(font)
for j in range(num-1):
    p=star*(2*(num-j-1)-1)
    fontt=" "*(j+1)
    print(fontt,end="")
    print(p,end="")#format 不支持变量作为宽度
    print(fontt)


