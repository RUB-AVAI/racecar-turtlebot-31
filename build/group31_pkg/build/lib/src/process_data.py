import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit
import math
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from scipy.interpolate import CubicSpline, interp1d
from numpy import interp

data = np.load("data/data-2.npy")
valid = []
data2 = []
fig, ax = plt.subplots()


x_positions = (data[:, 2] + data[:, 3]) / 2

ax.scatter(x_positions, data[:, 1], marker=".", color="red")

l_reg = LinearRegression()
l_reg.fit(x_positions.reshape(-1, 1), data[:, 1].reshape(-1, 1))
print(l_reg.coef_)
print(l_reg.intercept_)

def f(x):
    return l_reg.intercept_ + x * l_reg.coef_[0]

X = np.linspace(np.min(x_positions), np.max(x_positions))
ax.plot(X, f(X))


#preprocess: merge duplicates
# data = data[np.argsort(data[:, 2])]

# print(data.shape)

# processed = []

# prev = [-1, -1, -1]
# sum_range = 0
# sum_angle = 0
# counter = 0
# for data_point in data:
#     range = data_point[0]
#     angle = data_point[1]
#     box_size = data_point[2]
#     if range < 4000:
#         if box_size == prev[2]:
#             sum_range += range
#             sum_angle += angle
#             prev = data_point
#             counter += 1
#             continue
#         elif counter > 1:
#             processed.append([sum_range / counter, sum_angle / counter, prev[2]])
#             counter = 1
#         prev = data_point
#         sum_range = range
#         sum_angle = angle

# processed_data = np.array(processed)
# np.save("data/merged_data", processed_data)
# print(processed_data.shape)

# ax.scatter(processed_data[:, 2], processed_data[:, 0], marker=".", color="blue")

        
    

# for i in range(len(data)):
#     if data[i, 0] < 4000: 
#         if data[i, 2] < 30000:
#             valid.append([data[i, 0], data[i, 1], data[i, 2]])
#         else:
#             data2.append([data[i, 0], data[i, 1], data[i, 2]])

# data = np.array(valid)
# data2 = np.array(data2)

# # merge duplicates

# print(data)


IMSAVE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/data_viz"

# cs = CubicSpline(processed_data[:, 2], processed_data[:, 0])
# cs = interp1d(processed_data[:, 2], processed_data[:, 0], bounds_error=True)
# xs = np.arange(2000, 270000, 1)

# print(np.max(processed_data[:, 2]))
# ax.plot(xs, cs(xs))



# z = np.polyfit(data[:, 2], data[:, 0], 10)
# p = np.poly1d(z)


# xp = np.linspace(0, 28000)
# ax.plot(xp, p(xp), "-")

# z2 = np.polyfit(data2[:, 2], data2[:, 0], 2)
# p2 = np.poly1d(z2)

# xp = np.linspace(28000, 300000)
# ax.plot(xp, p2(xp))

# def func(x, a, b, c):
#     return a * np.log(b * x) + c

# popt, pocv = curve_fit(func, data[:, 2], data[:, 0])

# print(*popt)

# y_fit = np.array(func(data[:, 2], *popt))

# # scatter each cluster individually so they get different colors
# ax.scatter(data[:, 2], y_fit, marker=".", color="blue")

    
fig.tight_layout()
fig.savefig(IMSAVE_PATH)