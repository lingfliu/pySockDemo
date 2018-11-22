import socket
import time
import threading

host = '127.0.0.1'
port = 9003
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.bind((host, port))
except socket.error as msg:
    print('bind failed, err = ', msg[1])

sock.listen(0)

tx_threads = {}
rx_threads = {}

def writeThread(conn):
    cnt = 0
    while True:
        time.sleep(0.0001)
        conn.sendall(('received ' + str(cnt)).encode(encoding='ASCII'))
        cnt += 1
        print("sending idx=", cnt)

def readThread(conn):
    while True:
        time.sleep(0.0001)
        data = conn.recv(1024)
        print("received data from", data)
        if not data:
            break

while True:
    conn, addr = sock.accept()
    print("client connected, addr ", addr)
    writethrd = threading.Thread(target=writeThread, args=(conn,))
    readthrd = threading.Thread(target=readThread, args=(conn,))
    tx_threads[addr] = writethrd
    rx_threads[addr] = readthrd
    writethrd.start()
    readthrd.start()


