"""
2. 使用函数实现，按照1美元=6人民币汇率编写一个美元和人民币的双向兑换程序
•	说明
•	设计两个函数
•	RMB2Dollar():人民币转美元函数
•	Dollar2RMB():美元转人民币函数
"""
def RMB2Dollar(RMB):
    """人民币转美元函数"""
    exchangeRate =  0.1570
    Dollar = exchangeRate*RMB
    return Dollar

def Dollar2RMB(Dollar):
    """美元转人民币函数"""
    exchangeRate =  6.3689
    RMB = exchangeRate*Dollar
    return RMB
rmb = 100
doll = RMB2Dollar(rmb)
print('100 RMB can exchange',doll,'$' )
doll = 100
rmb = Dollar2RMB(doll)
print('100 Dollar can exchange',rmb,'￥' )
# =========================
# 结果：
# 100 RMB can exchange 15.7 $
# 100 Dollar can exchange 636.89 ￥