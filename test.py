import socket
import sys
 
# создаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Привязываем сокет к порту
#server_address = (str(socket.gethostbyname(socket.gethostname())), 10000)
server_address = (str(socket.gethostbyname('192.168.0.117')), 10000)
print('Старт сервера на {} порт {}'.format(*server_address))
sock.bind(server_address)
 
# Слушаем входящие подключения
sock.listen(1)
 
while True:
    # ждем соединения
    print('Ожидание соединения...')
    connection, client_address = sock.accept()
    try:
        print(f'Подключено к: {client_address}\n')
        # Принимаем данные порциями и ретранслируем их
        while True:
            data = connection.recv(16)
            print(f'Получено: {data.decode()}')
            if data:
                print('Обработка данных...')
                data = data.upper()
                print('Отправка обратно клиенту.\n')
                connection.sendall(data)
            else:
                print('Нет данных от: ', client_address)
                break
 
    except:
        # Очищаем соединение
        print("Not success")
        connection.close()