import sys
import numpy as np


def gradient_descent(alpha, X, Y, deviation, max_iteration):
    # 数据行数
    m = X.shape[0]
    # theta初始值
    theta0, theta1 = 0, 0

    # cost function
    J = 1/(2*m)*sum([(theta0 + theta1*X[i][0] - Y[i])**2 for i in range(m)])
    print(J)
    converged = False
    iteration = 0
    # sys.exit()

    while not converged:
        grad0 = 1.0/m*sum([(theta0 + theta1*X[i][0] - Y[i]) for i in range(m)])
        grad1 = 1.0/m*sum([(theta0 + theta1*X[i][0] - Y[i])*X[i][0] for i in range(m)])
        # 同步更新theta
        temp0 = theta0 - alpha*grad0
        temp1 = theta1 - alpha*grad1
        # 更新theta
        theta0, theta1 = temp0, temp1

        # 均方误差
        e = 1/(2*m)*sum([(theta0 + theta1*X[i][0] - Y[i])**2 for i in range(m)])
        if abs(J-e) <= deviation:
            print(f'Converged, iterations: {iteration} !!!')
            converged = True
        J = e
        # 累计迭代次数
        iteration += 1
        print(iteration, theta0, theta1, deviation)
        if iteration == max_iteration:
            print("Reach the maximum number of iterations")
            converged = True
    return theta0, theta1


if __name__ == '__main__':
    # Y = [i for i in range(100)]
    # X = np.array([[i] for i in range(1, 101)])
    Y = [2,4,6,8]
    X = np.array([[1],[3],[5],[7]])
    alpha = 0.0003
    deviation = 0.000000001
    max_iteration = 1000000
    print(gradient_descent(alpha, X, Y, deviation, max_iteration))