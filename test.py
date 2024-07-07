import math
import numpy as np
import random

# device_cpu_frequency = 10 * (10 ** 9)
# print(device_cpu_frequency)

# queue = []
# queue.insert(0, 5)
# print(queue)
# queue.insert(1, 6)
# print(math.exp(-0.8))

# test = [[250, 250], [750, 250], [250, 750], [750, 750]]
# for i in range(0, 4):
#     print(test[i][0])
#     print(test[i][1])

# x = 1221
# y = x % 10
# print(y)
# print(x)
# x = x / 10
# print(x)
# z = x % 10
# print(z)

# for i in range (0, 10):
#     n = random.uniform(0, 0.5)
#     print(n)
# list1 = np.random.uniform(low=0, high=5, size=5)
# print(list1)
# list1[0] = 10
# print(list1)

# print(list1[1])
# list = []
# for i in range(0, 5):
#     list.append(i)
# print(list.mean(axis=0))

# sla_in_each_slot = [0 for i in range(5)]
# print(sla_in_each_slot)


# edge_locations = [[250, 250], [750, 250], [250, 750], [750, 750], [500, 500]]
# print(len(edge_locations))

import numpy as np


def gauss_markov_model(num_steps, mu, sigma):
    # 初始化速度和方向
    velocity = np.zeros(num_steps)
    direction = np.zeros(num_steps)

    # 初始速度和方向
    velocity[0] = np.random.normal(mu, sigma)
    direction[0] = np.random.uniform(0, 2 * np.pi)

    alpha = np.random.uniform(0, 1)

    # 生成模型数据
    for t in range(1, num_steps):
        # 高斯随机变化
        velocity[t] = alpha * velocity[t - 1] + (1 - alpha) * mu + np.sqrt(1 - alpha ** 2) * np.random.normal(0, sigma)

        # 方向随机变化
        direction[t] = alpha * direction[t - 1] + (1 - alpha) * np.random.uniform(0, 2 * np.pi) + np.sqrt(
            1 - alpha ** 2) * np.random.normal(0, sigma)

    return velocity, direction


# 示例用法
num_steps = 100  # 模拟的时间步数
alpha = 0.8  # 控制参数，影响速度和方向的持久性
mu = 10  # 速度的期望值
sigma = 1  # 高斯分布的标准差

# 调用模型函数
velocity, direction = gauss_markov_model(num_steps, mu, sigma)

# 打印结果示例
print("Velocity:", velocity)
print("Direction:", direction)