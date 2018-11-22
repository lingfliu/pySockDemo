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

cli_threads = {}

def clientThread(conn):
    cnt = 0
    reply = [0x00, 0xaa, 0x00, 0xcc, 30, 0x00, 0x00, 0x00]
    # conn.sendall(bytearray(reply))
    conn.sendall('hello'.encode(encoding='ASCII'))
    while True:
        time.sleep(0.0001)
        # conn.sendall(bytearray(reply))
        # conn.sendall('hello'.encode(encoding='ASCII'))
        data = conn.recv(1024)
        print("received data from", data)
        reply = data
        if not data:
            break
        # conn.sendall(('received '+str(cnt)).encode(encoding='ASCII'))
        # cnt += 1
        # print("sending idx=", cnt)
            # break
        # conn.sendall(bytearray(reply))

while True:
    conn, addr = sock.accept()
    print("client connected, addr ", addr)
    thrd = threading.Thread(target=clientThread, args=(conn,))
    cli_threads[addr] = thrd
    thrd.start()


