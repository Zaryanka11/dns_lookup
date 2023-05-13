import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import time

# СЮДА НАШ МАСССИИИИИВ ИЗМЕНЯЕМЫХ ДАНННЫЫХХХХХ
data = [0] # НОЛИК УБРАТЬ, ЭТО ДЛЯ НАГЛЯДНОСТИ!!!!!!!!!!!!!!!!!!!!!!!!!
# ИНТЕРАВАЛ ИЗМЕНЕНИЯ(ДОБАВЛЕНИЯ ДАННЫХ В МАССИВ) ДАННЫХХХХХХХ
update_interval = 1
# ИНТЕРВАЛ ЗАПИСИ ДАННЫХ В ФАЙЛ
write_interval = 10



df = pd.DataFrame({'time': [datetime.now()], 'humidity': data})
fig, ax = plt.subplots()
line, = ax.plot(df['time'], df['humidity'])

# Задаем основные настройки графика
ax.set_xlabel('Time')
ax.set_ylabel('Humidity')
ax.set_title('Real-time Plot')
ax.set_ylim(min(data) - 1, max(data) + 1)

# Создаем txt файл для записи данных
file = open("data.txt", "a")

# Задаем интервал обновления данных и записи в файл (в секундах)
next_write_time = time.time() + write_interval

# Основной цикл программы
while True:
    # Обновляем данные
    data.append(data[-1])
    df_new = pd.DataFrame({'time': [datetime.now()], 'humidity': [data[-1]]})
    df = pd.concat([df, df_new], ignore_index=True)

    # Обновляем график
    line.set_data(df['time'], df['humidity'])
    ax.set_xlim(datetime.now() - pd.Timedelta(seconds=60), datetime.now())
    ax.set_ylim(min(data) - 1, max(data) + 1)

    # Записываем данные в файл с заданной периодичностью
    if time.time() >= next_write_time:
        file.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + str(data[-1]) + '\n')
        next_write_time += write_interval

    # Перерисовываем график и ждем заданное количество секунд
    plt.draw()
    plt.pause(update_interval)

