import sys
import numpy as np


class Linear_regression:

    def gradient_descent(self, alpha, array, deviation, max_iteration):
        # 数据行数
        m = array.shape[0]
        # 特征个数
        n = array.shape[1]
        # theta初始值
        theta = np.array([[0]*n])

        X = np.c_[np.ones(m), array[:,:-1]]
        Y = array[:, [-1]]
        # cost function
        J = np.sum(np.square(np.dot(X,theta.T) - Y)) / (2 * m)
        print(f'm:{m}, n:{n}, theta:{theta}, X:{X}, Y:{Y}, J:{J}', sep='\n')
        sys.exit()
        converged = False
        iteration = 0
        grad = 1.0 / m * np.sum(np.array([[(np.dot(X, theta.T) - Y) * X[:, [i]] for i in range(m)]]))

        print(grad)
        sys.exit()
        while not converged:
            grad = 1.0/m*np.sum(np.array([(np.dot(X, theta.T) - Y)*X[:,[i]] for i in range(m)]))
            # 同步更新theta
            tem =theta - alpha*grad
            # 更新theta
            theta = tem
            # 均方误差
            e = 1 / (2 * m) * np.sum(np.square(X*theta.T - Y))
            if abs(J - e) <= deviation:
                print(f'Converged, iterations: {iteration} !!!')
                converged = True
            J = e
            # 累计迭代次数
            iteration += 1
            print(iteration, theta, deviation)
            if iteration == max_iteration:
                print("Reach the maximum number of iterations")
                converged = True
        return theta

    def mean_normalization(self, array):
        m = array.shape[0]
        mean = np.mean(array, axis=0)
        std = np.std(array, axis=0)
        mean_array = np.array([mean] * m)
        std_array = np.array([std] * m)
        # codomain = np.max(array, axis=0) - np.min(array, axis=0)
        # codomain_array = np.array([codomain]*m)
        new_data = (array - mean_array) / mean_array
        return new_data




if __name__ == '__main__':
    linear = Linear_regression()
    array = np.arange(1,9).reshape(4,2)
    data = linear.mean_normalization(array)
    alpha = 0.0003
    deviation = 0.000000001
    max_iteration = 1000000
    print(linear.gradient_descent(alpha, array, deviation, max_iteration))


