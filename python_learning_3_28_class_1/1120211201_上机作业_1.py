"""
1.使用函数实现,输入每户每年的用水量，输出总水费
•	水费计算
•	上海市市属供排水服务区域的居民用户水价同步实行阶梯水价制度：
•	第一阶梯水量为每户每年0至220立方米(含)，综合水价为3.45元/立方米;
•	第二阶梯水量为每户每年220至300立方米(含)，综合水价为4.83元/立方米;
•	第三阶梯水量为每户每年300立方米以上的部分，综合水价为5.83元/立方米。
"""
def calculateFee(consumption):
    if consumption >= 0 and consumption <= 220:
        fee = 3.45 * consumption
        print("Total cost %.2f￥" % fee)
    elif consumption > 220 and consumption <= 300:
        fee = 3.45 * 220 + (consumption - 220) * 4.83
        print("Total cost %.2f￥" % fee)
    elif consumption > 300:
        fee = 3.45 * 220 + 80 * 4.83 + (consumption - 300) * 5.83
        print("Total cost %.2f￥" % fee)
calculateFee(100)
calculateFee(250)
calculateFee(400)