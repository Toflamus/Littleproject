fo = open(r"D:\16ComputerScience\Python\Python_study_project\PythonApplication1\Python_configurition\test.txt",'at',encoding = 'UTF-8')
# #1.双反斜杆 \\
# 我们知道，文件夹地址中有这样的反斜杆 \，但是这样的斜杆在python字符串中代表的是转义符，是将后一个字符进行转义，比如，\n,\r,\'，但是要单独再输出反斜杆，就可以再在前面加转义符 \\。这样就能正常表示一个反斜杆。
# "E:\\Python\\Scripts"
# 2.在地址字符串前面加 r
# 第二个写绝对地址的方式是在地址字符串前面加上字母 r，它的作用就是将含有转义字符、特殊含义字符等的字符串变为一般的字符，就是所见即所得，这个方法通常还会用在正则表达式中。
# r"E:\Python\Scripts"
# 3.将反斜杠写为正斜杠 /
# 正斜杠在python中就不是转义之用了，但是却可以用来表示地址，如果写成正斜杠的形式就不用用到前面两种方式了（正斜杠常见在网址，其实网址也可以看作是另一种文件地址）。
# "E:/Python/Scripts"
# 以上就是介绍的在python中写绝对地址的三种方法，希望大家以后都能解决绝对地址写错的问题。


fo.writelines('你追到AG你dfasdfen'+'\n')
fo.close()
