import math

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import expon, kstest

# Загрузка данных
data = pd.read_csv('r2z2.csv', header=None, names=['x'], skiprows=1, dtype=np.float64)

lamb = 2


# Функция распределения предполагаемого распределения
def exp_cdf(x):
    return expon.cdf(x, scale=1 / lamb)


# Вычисление эмпирической функции распределения
def ecdf(data):
    x = np.sort(data)
    y = np.arange(1, len(data) + 1) / len(data)
    return x, y


# Построение графиков ЭФР и функции распределения
x, y = ecdf(data['x'])
f = np.linspace(0, 5, 100)
plt.plot(f, exp_cdf(f), 'r-', label='Экспоненциальное распределение')
plt.plot(x, y, 'b.', markersize=5, label='Эмпирическая ФР')
plt.xlabel('X')
plt.ylabel('Кумулятивная вероятность')
plt.legend(loc='lower right')
plt.show()

# Проверка гипотезы о показательном распределении
alpha = 0.1
n = len(data)
D, _ = kstest(x, expon.cdf, args=(0, 1 / lamb))
p_value = 2 * (1 - expon.cdf(D * np.sqrt(n)))

critical_value = np.sqrt(-0.5 * np.log(alpha / 2) / n)
print(f'Критическое значение статистики Колмогорова: {critical_value * np.sqrt(n)}')
print(f'Статистика: D = {D}, p-value = {p_value}')
print(f'D * √n = {D * np.sqrt(n)}')

print(f'Критическая область: D > {critical_value}')
if D > critical_value:
    print('Гипотеза H0 о показательном распределении отвергается')
else:
    print('Гипотеза H0 о показательном распределении не отвергается')