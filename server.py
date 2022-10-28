import socket
from _thread import *
import sys

server="192.168.1.19"
port=5050

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))

except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server started")

def threaded_client(conn):
    conn.send(str.encode("connected"))
    reply=""
    while True:
        try:
            data=conn.recv(2048)
            reply=data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                print("Received:".reply)
                print("sending: ",reply)
            conn.sendall(str.encode(reply))
        except :
            break
    print("Connection lost")
    conn.close()
        

while True:
    conn, addr =s.accept()
    print("Connected to:",addr)
    start_new_thread(threaded_client,(conn,))
