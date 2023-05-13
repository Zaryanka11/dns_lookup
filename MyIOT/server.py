import socket

##
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import time
###

#import spl as spl

serv_sock = socket.socket()
serv_sock.bind(('', 53210))
serv_sock.listen(10)


##


# СЮДА НАШ МАСССИИИИИВ ИЗМЕНЯЕМЫХ ДАНННЫЫХХХХХ
data_values = [0] # НОЛИК УБРАТЬ, ЭТО ДЛЯ НАГЛЯДНОСТИ!!!!!!!!!!!!!!!!!!!!!!!!!
# ИНТЕРАВАЛ ИЗМЕНЕНИЯ(ДОБАВЛЕНИЯ ДАННЫХ В МАССИВ) ДАННЫХХХХХХХ
update_interval = 1
# ИНТЕРВАЛ ЗАПИСИ ДАННЫХ В ФАЙЛ
write_interval = 10



df = pd.DataFrame({'time': [datetime.now()], 'humidity': data_values})
fig, ax = plt.subplots()
line, = ax.plot(df['time'], df['humidity'])

# Задаем основные настройки графика
ax.set_xlabel('Time')
ax.set_ylabel('Humidity')
ax.set_title('Real-time Plot')
ax.set_ylim(min(data_values) - 1, max(data_values) + 1)

# Создаем txt файл для записи данных
file = open("data.txt", "a")

# Задаем интервал обновления данных и записи в файл (в секундах)
next_write_time = time.time() + write_interval




###



while True:
    print('START')
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)


    # if name == 'main':
    #     with open("result.txt", "w", encoding="utf-8") as result_file:
    #         for s in spl:
    #             dateval, , lst = s.partition('>>>')
    #             print(*[f'{date_val}>>>{elem}' for elem in lst.split(';')], sep='\n', file=result_file)
    #
    # import sys
    #
    # stdoutOrigin = sys.stdout
    # sys.stdout = open("result.txt", "w")

    #
    # def data_gen():
    #     yield from map(int, sys.stdin)


    while True:
        # Пока клиент не отключился, читаем передаваемые
        # им данные и отправляем их обратно
        data = client_sock.recv(1)
        if not data:
            # Клиент отключился
            break
        # client_sock.sendall(data)
        data_d = int(data[0])
        print('Decimal :', data_d)
        # print(data)
    client_sock.close()


    ##
    # Обновляем данные
    data_values.append(data_d)
    df_new = pd.DataFrame({'time': [datetime.now()], 'humidity': [data_values[-1]]})
    df = pd.concat([df, df_new], ignore_index=True)

    # Обновляем график
    line.set_data(df['time'], df['humidity'])
    ax.set_xlim(datetime.now() - pd.Timedelta(seconds=60), datetime.now())
    ax.set_ylim(min(data_values) - 1, max(data_values) + 1)

    # Записываем данные в файл с заданной периодичностью
    if time.time() >= next_write_time:
        file.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + str(data_values[-1]) + '\n')
        next_write_time += write_interval

    # Перерисовываем график и ждем заданное количество секунд
    plt.draw()
    plt.pause(update_interval)
    ###

    # sys.stdout.close()
    # sys.stdout = stdoutOrigin