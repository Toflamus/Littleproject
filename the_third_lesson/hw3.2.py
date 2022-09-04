# 万年历问题
# 基本要求：
# 输入： 日期（ 年月日） ， 格式自主定义
# 输出： 该日期为星期几
# 例如：
# 请输入日期（ 格式： yyyy/mm/dd） :
# 2021/08/12
# 2021年8月12日是： 星期四
# 要求： 不能使用time库、 calendar库
# 尽量使用自定义函数进行换算


#输入：一个包含年月日的字符串：提取年月日并转换成整型变量
#处理：1，年份处理，包含几个闰年并计算天数
#     2，月份处理，当年是不是闰年，在月份并计算天数
#     3，日期处理，直接相加。
#输出：一个日期的汉字表达
#定义常量
yeardays=365
monthdays1=31
monthdays2=30
monthdays3=28
weekdays=7
century=100
startyear=2001
#封装函数
def dayDif(year,month,day):
    #year part
    y=year-startyear
    daysofy=yeardays*y+y//4-y//100+y//400
    #month part
    monthdaylist=[31,28,31,30,31,30,31,31,30,31,30,31]
    sum=0
    for i in range(month-1):
        sum+=int(monthdaylist[i])
   
    if month>=2:
        if year%4==0 and year%100!=0:
            sum+=1
        elif year%4==0 and year%100==0 and year%400==0:
            sum+=1
    totaldays=daysofy+sum+day
    return totaldays

#输入处理
today = input("请输入日期（ 格式： yyyy/mm/dd） :")
todayyear = int(today[0:4])
todaymonth = int(today[5:7])
todayday = int(today[8:])
total=dayDif(todayyear,todaymonth,todayday)
youbi=total%7

#输出处理
rilist = ['日','一','二','三','四','五','六']
print(todayyear,'年',todaymonth,'月',todayday,'日是星期'+rilist[youbi])
