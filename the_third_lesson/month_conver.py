
def DfStrofMon(num):#定义一个函数可以自动获取月份的字符串表达
    name = "JanFebMarAprMayJunJulAugSepOctNovDec"#运算符号左右加空格会比较好看
    pos = (num-1)*3
    string = name[pos:pos+3]
    return string

number=eval(input("the number of the month"))#注意input的输入是字符串需要进行转换,使用int转换会更加
Mon=DfStrofMon(number)
print("the short form of the month is",Mon)



