import numpy as np
import random
import math
import matplotlib.pyplot as plt
from time import *


def init_x(n, d):
    """
    :param n: 粒子总数量
    :param d: 粒子种基因个数(维度)
    :return population:随机生成的种群(二维list)
    """
    population = []
    for i in range(n):
        gene = []
        for j in range(d):
            a = np.random.randint(0, 2)
            gene.append(a)
        population.append(gene)
    return population


def init_v(n, d, V_max, V_min):
    """
    :param n: 粒子总数量
    :param d: 粒子种基因个数(维度)
    :return: 随机生成的种群(二维list)
    """
    v = []
    for i in range(n):
        vi = []
        for j in range(d):
            a = random.random() * (V_max - V_min) + V_min
            vi.append(a)
        v.append(vi)
    return v


def fitness(p, n, d, w, w_max, v, afa):
    """
    :param p: 粒子群
    :param n: 群体粒子个数
    :param d: 粒子维数
    :param w: 物品的重量列表
    :param w_max: 背包最大容量
    :param v: 物品的价值列表
    :param afa: 惩罚系数
    :return: fitvalue每一个粒子的价值
    :return: fitweight每一个粒子的重量
    tips: 如果物品总重量大于背包最大容量时，引入惩罚系数
    """
    fitvalue = []
    fitweight = []
    for i in range(n):
        a = 0  # 每个粒子的重量
        b = 0  # 每个粒子的价值(适应度)
        for j in range(d):
            if p[i][j] == 1:
                a += w[j]
                b += v[j]
        if a > w_max:
            b = 0
            # b = b + afa * (w_max - a)  # 超重
        fitvalue.append(b)
        fitweight.append(a)
    return fitvalue, fitweight


def update_pbest(p, fitvalue, pbest, px, m):
    """
    更新个体最优
    :param p: 当前种群
    :param fitvalue: 当前每个粒子的适应度
    :param pbest: 更新前的个体最优
    :param px: 更新前的个体最优解
    :param m: 粒子数量
    :return: 更新后的个体最优值、个体最优解
    """
    pb = pbest
    for i in range(m):
        if fitvalue[i] > pbest[i]:
            pbest[i] = fitvalue[i]
            px[i] = p[i]
    return pb, px


def update_gbest(p, pbest, gbest, g, m):
    """
    更新全局最优解
    :param p: 粒子群
    :param pbest: 个体适应度(个体最优)
    :param gbest: 全局最优
    :param g: 全局最优解
    :param m: 粒子数量
    :return: gbest全局最优，g对应的全局最优解
    """
    gb = gbest
    for i in range(m):
        if pbest[i] > gb:
            gb = pbest[i]
            g = p[i]
    return gb, g


def update_v(v, x, m, n, pbest, g, c1, c2, vmax, vmin):
    """
    更新速度
    :param v:更新前的速度
    :param x: 更新前的位置
    :param m: 粒子数量
    :param n: 粒子维度
    :param pbest: 个体最优解(二维列表)
    :param g: 全局最优解(一维列表)
    :param c1: 加速因子
    :param c2: 加速因子
    :param vmax: 最大速度
    :param vmin: 最小速度
    :return: 更新后的速度二维列表
    """
    for i in range(m):
        a = random.random()
        b = random.random()
        for j in range(n):
            # 计算动态惯性权值
            w = W_max - (W_max - W_min)*i/T
            # 更新速度
            v[i][j] = w*v[i][j] + c1 * a * (pbest[i][j] - x[i][j]) + c2 * b * (g[j] - x[i][j])
            # 边界处理条件
            if v[i][j] < vmin:
                v[i][j] = vmin
            if v[i][j] > vmax:
                v[i][j] = vmax
    return v


def update_x(x, v, m, n):
    """
    更新x
    :param x:更新前的x
    :param v: 更新后的v
    :param m: 粒子数量
    :param n: 粒子维度
    :return: 更新后的x
    """
    for i in range(m):
        for j in range(n):
            a = random.random()
            x[i][j] = 1 / (1 + math.exp(-v[i][j]))
            if x[i][j] > a:
                x[i][j] = 1
            else:
                x[i][j] = 0
    return x


# main()
if __name__ == '__main__':
    begin_time = time()
    Weight = [95, 75, 23, 73, 50, 22, 6, 57, 89, 98]  # 物品体积
    Value = [89, 59, 19, 43, 100, 72, 44, 16, 7, 64]  # 物品价值
    N = 200  # 群体粒子个数
    D = len(Weight)  # 粒子维数
    T = 100  # 最大迭代次数
    c1 = 1.5  # 学习因子1
    c2 = 1.5  # 学习因子2
    W_max = 0.8  # 惯性权重最大值
    W_min = 0.4  # 惯性权重最小值
    V_max = 10  # 速度最大值
    V_min = -10  # 速度最小值
    Weight_max = 300  # 背包容量

    afa = 10  # 惩罚系数
    item = []  # 用于记录每一次迭代的全局最优值
    itemg = []  # 用于记录每一次迭代的全局最优解

    x = init_x(N, D)  # 初始化x
    v = init_v(N, D, V_max, V_min)  # 初始化v

    fv, fw = fitness(x, N, D, Weight, Weight_max, Value, afa)  # 计算第一次迭代的适应度
    pb, px = fv, x  # 由于是第一次迭代，个体最优为当前值
    gb, g = update_gbest(x, pb, 0, [], N)  # 同理，寻找第一代的全局最优
    item.append(gb)  # item列表记录每一次迭代的全局最优
    itemg.append(g)
    v = update_v(v, x, N, D, px, g, c1, c2, V_max, V_min)  # 更新下一代的速度
    x = update_x(x, v, N, D)  # 更新下一代的位置

    for i in range(T):
        fv, fw = fitness(x, N, D, Weight, Weight_max, Value, afa)
        pb, px = update_pbest(x, fv, pb, px, N)
        gb, g = update_gbest(x, pb, gb, g, N)
        item.append(gb)
        itemg.append(g)
        v = update_v(v, x, N, D, px, g, c1, c2, V_max, V_min)
        x = update_x(x, v, N, D)

    print(gb)
    plt.plot(item)
    plt.show()
    end_time = time()
    run_time = end_time - begin_time
    print('粒子群算法计算时间为：', run_time)
