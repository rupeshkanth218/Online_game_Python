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

pos=[(0,0),(100,100)]

def read_pos(s):
    s=s.split(",")
    return int(s[0]), int(s[1])

def make_pos(t):

    return f"{t[0]},{t[1]}"

def threaded_client(conn, player):
    
    conn.send(str.encode(make_pos(pos[player])))
    reply=""
    while True:
        
        try:
            data=read_pos(conn.recv(2048).decode())
            pos[player]=data
            
            
            if not data:
                print("Disconnected")
                break
            else:
                if player==1:
                    reply=pos[0]
                else:
                    reply=pos[1]
                print("Received:",data)
                print("sending: ",reply)
            conn.sendall(str.encode(make_pos(reply)))
        
        except Exception as e:
            break
    print("Connection lost")
    conn.close()
        


currentPlayer=0
while True:
    conn, addr =s.accept()
    print("Connected to:",addr)
    
    start_new_thread(threaded_client,(conn,currentPlayer))

    currentPlayer+=1
