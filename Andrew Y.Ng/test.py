import numpy as np
import random


def gradient_descent(alpha, x, y, ep=0.0001, max_iter=10000):
    converged = False
    iter = 0
    m = x.shape[0]  # 数据的行数

    # 初始化参数(theta)
    t0 = np.random.random(x.shape[1])
    t1 = np.random.random(x.shape[1])

    # 代价函数, J(theta)
    J = sum([(t0 + t1 * x[i] - y[i]) ** 2 for i in range(m)])

    # 进行迭代
    while not converged:
        # 计算训练集中每一行数据的梯度 (d/d_theta j(theta))
        grad0 = 1.0 / m * sum([(t0 + t1 * x[i] - y[i]) for i in range(m)])
        grad1 = 1.0 / m * sum([(t0 + t1 * x[i] - y[i]) * x[i] for i in range(m)])

        # 更新参数 theta
        # 此处注意，参数要同时进行更新，所以要建立临时变量来传值
        temp0 = t0 - alpha * grad0
        temp1 = t1 - alpha * grad1
        t0 = temp0
        t1 = temp1

        # 均方误差 (MSE)
        e = sum([(t0 + t1 * x[i] - y[i]) ** 2 for i in range(m)])

        if abs(J - e) <= ep:
            print('Converged, iterations: ', iter, '!!!')
            converged = True

        J = e  # 更新误差值
        iter += 1  # 更新迭代次数

        if iter == max_iter:
            print('Max interactions exceeded!')
            converged = True

    return t0, t1


if __name__ == '__main__':
    Y = [i for i in range(100)]
    X = np.array([i] for i in range(100))
    alpha = 0.001
    deviation = 0.0001
    max_iteration = 10000
    gradient_descent(alpha, X, Y, deviation, max_iteration)