import csv

import numpy as np
from scipy import stats
from scipy.stats import t
from math import sqrt

data = r"r2z1.csv"
x_el = []
y = []
with open(data, "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        x_el.append(row[0])
        y.append(float(row[1])) if row[1] else None

x = [float(x) for x in x_el if x != ""]

n1 = len(x)
n2 = len(y)
alpha = 0.025

#выборочные средние и стандартные отклонения для обеих выборок:
x_mean = sum(x)/n1
y_mean = sum(y)/n2
print(x_mean)
print(y_mean)

std1, std2 = np.std(x, ddof=1), np.std(y, ddof=1)

# статистикa
t = (x_mean - y_mean) / np.sqrt((std1**2 / n1) + (std2**2 / n2))

# критическая область
df = n1 + n2 - 2

# критическая константа
t_critical = stats.t.ppf(1 - alpha, df)

# р-значение
p_value = 1 - stats.t.cdf(t, df)

if t > t_critical:
    print("Отклоняем нулевую гипотезу")
else:
    print("Принимаем нулевую гипотезу")

print("Статистика t: ", t)
print("Критическая константа: ", t_critical)
print("p-значение: ", p_value)