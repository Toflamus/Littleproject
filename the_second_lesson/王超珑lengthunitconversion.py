
#the conversion of inch ,centmeter ,and feet
def TheConversionFunction(Height):#to define a function
    if (Height[-2:] in ['ft']):
        Height_in_cm=(eval(Height[0:-2]))*30.48
    elif(Height[-2:] in ['cm']):
        Height_in_cm=(eval(Height[0:-2]))
    elif(Height[-2:] in ['in']):
        Height_in_cm=(eval(Height[0:-2]))*2.54
    else:
        print("format wrong")
    return Height_in_cm

def TheOutputFunction(result,height_cm):
    if (result in ['ft']):
        Output = height_cm*30.48
    elif (result in ['cm']):
        Output = height_cm
    elif (result in ['in']):
        Output = height_cm*2.54
    else:
        print("format wrong")
    return Output


height = input("please input the hight with unit, input N to end")
result = input("please decide which unit you want: ft cm ot in")

while height[-1] not in ['N','n'] :
    
    height_in_cm=TheConversionFunction(height)
    output=TheOutputFunction(result,height_in_cm)
    print("{:.2f}".format(output),result)
    height = input("please input the hight with unit, input N to end")
    if height[-1] in ['N','n']:
        break
    result = input("please decide which unit you want: ft cm ot in")




