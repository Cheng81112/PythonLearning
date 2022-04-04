'''
BMI的定义如下：
BMI = 体重（kg）÷身高2（m2）
例如，一个人身高1.75米、体重75公斤，他的BMI值为24.49

'''

height = eval(input("请输入身高（米）："))
weight = eval(input("请输入体重（千克）："))
BIM = weight / pow(height,2)
print("BIM数值为：{}" .format(BIM))


wto , dom = "","" # 序列赋值

# 第一个分支 WTO标准
if BIM < 18.5:
    wto = "偏瘦"
elif BIM >= 18.5 and BIM < 25:
    wto = "正常"
elif BIM >= 25 and BIM <30:
    wto = "偏胖"

else:
    wto="肥胖"

# 第二个分支 我国卫生标准

if BIM < 18.5:
    dom = "偏瘦"
elif BIM >= 18.5 and BIM < 24:
    dom = "正常"
elif BIM >=24 and BIM <28:
    dom = "偏胖"
else:
    dom = "肥胖"
print("国际标准{} , 国内标准{}" .format(wto,dom))




