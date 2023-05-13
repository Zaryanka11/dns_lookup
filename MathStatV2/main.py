from os import sep
import numpy as np
import matplotlib.pyplot as plt


my_param_x = 118
def get_middle(data):
    return sum(data) / len(data)

def get_dispersion_shifted(data, middle):
    multiply = 0
    for i in range(len(data)):
        multiply += (data[i] - middle) ** 2
    return multiply / len(data)


def get_deviation(data):
    return get_dispersion_shifted(data, get_middle(data))**0.5


def get_coef_cov(v_x, v_y):
    sum = 0
    for i in range(len(v_x)):
        sum += (v_x[i] - get_middle(v_x)) * (v_y[i] - get_middle(v_y))
    return sum / len(v_x)


def get_coef_line_cor(v_x, v_y):
    return get_coef_cov(v_x, v_y) / (get_deviation(v_x) * get_deviation(v_y))

def get_coef_A(v_x, v_y):
    return get_coef_line_cor(v_x, v_y) * get_deviation(v_y) / get_deviation(v_x)


def get_coef_B(v_x, v_y):
    return get_middle(v_y) - a * get_middle(v_x)

def get_value(x, a, b):
    return round(a * x + b, 2)


def get_function(x, middle_x, cor, middle_y):
    return (x - middle_x) / cor + middle_y



v_x = []
v_y = []
with open('16' + "\\r4z2.csv", 'r') as f:
    f.readline()
    inputData = f.readlines()
    for i in range(len(inputData)):
        a, b = inputData[i].replace("\n", "").split(",")
        v_x.append(float(a))
        v_y.append(float(b))
x_middle = get_middle(v_x)
y_middle = get_middle(v_y)
x_deviation = get_deviation(v_x)
y_deviation = get_deviation(v_y)
cov = get_coef_cov(v_x, v_y)
coef_line_cor = get_coef_line_cor(v_x, v_y)
#y = ax + b
a = round(get_coef_A(v_x, v_y), 4)
b = round(get_coef_B(v_x, v_y), 2)
print("y = ", a, "x", " + ", b, sep="")
result_of_param_x_on_y = get_function(118, get_middle(v_x), coef_line_cor, get_middle(v_y))
print(result_of_param_x_on_y)


delta = 0.01
loc_x = min(v_x) * (1 - delta)
loc_x_max = max(v_x) * (1 + delta)
loc_y = min(v_y) * (1 - delta)
loc_y_max = max(v_y) * (1 + delta)
point_size = (loc_x_max - loc_x) * (loc_y_max-loc_y) * 0.01
fig, ax = plt.subplots(1, 1)
line2, = plt.plot([my_param_x, my_param_x], [loc_y , loc_y_max])
plt.plot(v_x, v_y, marker='o', linewidth=0, markersize = point_size)
line1, = plt.plot([loc_x, loc_x_max], [get_value(loc_x, a, b), get_value(loc_x_max, a, b)], linewidth=3, color = 'green')
line3, = plt.plot([110, 130], [get_function(110, get_middle(v_x), coef_line_cor, get_middle(v_y)), get_function(130, get_middle(v_x), coef_line_cor, get_middle(v_y))], linewidth=3, color = 'red')
ax.set_xlim(loc_x, loc_x_max)
ax.set_ylim(loc_y, loc_y_max)
ax.set_xlabel("Ось X")
ax.set_ylabel("Ось Y")
plt.legend([line1, line2, line3], ["(Y по X) y = " + str(round(a, 2)) + "x + " + str(round(b, 4)), "y = (" + str(my_param_x) + " - " + str(round(x_middle, 2)) + ") / " + str(round(coef_line_cor, 2)) + " + " + str(round(y_middle, 2)) + " = " + str(round(result_of_param_x_on_y, 2)),
                                   "(X по Y) y = x / " + str(round(coef_line_cor, 2)) + " + " + str(round((-1 * x_middle / coef_line_cor) + y_middle, 2))])
ax.grid(color='black', linewidth = 0.5, linestyle='--')
plt.show()

