import time
import socket

s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
s.connect(('localhost', 8080))

num_measurements = 100
start = time.time()

for i in range(num_measurements):
    s.sendall('ping'.encode('utf-8'))
    data = s.recv(1024)

elapsed_time_millis = int((time.time() - start) * 1000)
print(f'計測回数: {num_measurements} 回')
print(f'合計時間: {elapsed_time_millis} ms')
print(f'平均時間: {elapsed_time_millis / num_measurements} ms')
