import socket
import serial
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
print("Sections : ", config.sections())
# 获取配置文件参数
ip = config.get('TCP_IP_PORT', 'ip')
port = int(config['TCP_IP_PORT']['port'])

rs232_port = config.get('RS232', 'rs232_port')
bps = int(config['RS232']['bps'])


# 创建TCP socket对象
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP和端口号
tcp_socket.bind((ip, port))

# 监听客户端连接
tcp_socket.listen(128)

# 打开串口
ser = serial.Serial(rs232_port, bps)

while True:
    # 等待客户端连接
    client_socket, client_address = tcp_socket.accept()
    # 接收客户端发送的数据
    data = client_socket.recv(1024)
    print(data, client_address)
    # 将数据转发到串口
    ser.write(data)

    # 关闭客户端连接
    client_socket.close()
