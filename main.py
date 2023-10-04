import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ServAdress = ('127.0.0.1', 25)
print('Подключено к {} порт {}'.format(*ServAdress))
sock.connect(ServAdress)

while (1):
        print("Введите /q для выхода из программы")
        mess = input()
        if mess == '/q':
            break
        print(f'Отправка: {mess}')
        message = mess.encode()
        sock.sendall(message)

        # Смотрим ответ
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            mess = data.decode()
            print(f'Получено: {data.decode()}')
sock.close()
