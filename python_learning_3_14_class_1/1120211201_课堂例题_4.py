# 作业4
'''
水费计算
上海市市属供排水服务区域的居民用户水价同步实行阶梯水价制度：
第一阶梯水量为每户每年0至220立方米(含)，综合水价为3.45元/立方米;
第二阶梯水量为每户每年220至300立方米(含)，综合水价为4.83元/立方米;
第三阶梯水量为每户每年300立方米以上的部分，综合水价为5.83元/立方米。
编写程序，实现输入每户每年的用水量，输出总水费

'''
while 1:
    water_con=float(input("请输入用户用水量："))
    firt_pri=3.45
    second_pri=4.83
    third_pri=5.83

    if water_con >= 0 and water_con <= 220:

        a = water_con * firt_pri
        print("用户总水费为{}".format(a))

    elif water_con>220 and water_con <= 300:

        b = 220*firt_pri + (water_con-220) * second_pri
        print("用户总水费为{}".format(b))
    else:
        c =220*firt_pri + 80 * second_pri + (water_con-300) * third_pri
        print("用户总水费为{}".format(c))