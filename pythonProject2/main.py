from os import sep
import matplotlib.pyplot as plt

#Х
my_param_x = 118

#Среднее значение (мат.ожидание)
def get_middle(data):
    return sum(data) / len(data)

#Дисперсия обычная (смещённая)
def get_dispersion_shifted(data, middle):
    multiply = 0
    for i in range(len(data)):
        multiply += (data[i] - middle) ** 2
    return multiply / len(data)

#Стандартное отклнение
def get_deviation(data):
    return get_dispersion_shifted(data, get_middle(data))**0.5

#Коэффициент ковариации
def get_coef_cov(v_x, v_y):
    sum = 0
    for i in range(len(v_x)):
        sum += (v_x[i] - get_middle(v_x)) * (v_y[i] - get_middle(v_y))
    return sum / len(v_x)

#Коэффициент линейной кореляции
def get_coef_line_cor(v_x, v_y):
    return get_coef_cov(v_x, v_y) / (get_deviation(v_x) * get_deviation(v_y))

#Коэффициент А для линейной регресии
def get_coef_A(v_x, v_y):
    return get_coef_line_cor(v_x, v_y) * get_deviation(v_y) / get_deviation(v_x)

#Коэффициент В для линейной регресии
def get_coef_B(v_x, v_y):
    return get_middle(v_y) - a * get_middle(v_x)

#Находим функцию по аргументу (y=ax+b)
def get_value(x, a, b):
    return round(a * x + b, 2)


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
#Уравнение линейной регрессии: y = ax + b
a = round(get_coef_A(v_x, v_y), 4)
b = round(get_coef_B(v_x, v_y), 2)
print("y = ", a, "x", " + ", b, sep="")
result_of_param_x_on_y = get_middle(v_y) + get_coef_line_cor(v_x, v_y) * (my_param_x - get_middle(v_x))
print(result_of_param_x_on_y)

#Использую библиотеку Python для построения окна с графиком
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
ax.set_xlim(loc_x, loc_x_max)
ax.set_ylim(loc_y, loc_y_max)
ax.set_xlabel("Ось X")
ax.set_ylabel("Ось Y")
plt.legend([line1, line2], ["y = " + str(round(a, 2)) + "x + " + str(round(b, 4)), "y = " + str(round(result_of_param_x_on_y, 2))])
ax.grid(color='black', linewidth = 0.5, linestyle='--')
plt.show()