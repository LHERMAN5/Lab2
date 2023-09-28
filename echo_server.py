#!/usr/bin/env python3
import socket
import time
from threading import Thread

#define address & buffer size
HOST = ""
PORT = 8080
BUFFER_SIZE = 1024

def handle_connection(conn, addr):
    print("Connected by", addr)

    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        print(data)
        conn.sendall(data)



def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)

        while True:
            conn, addr = s.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()


def start_server():
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        conn, addr = s.accept()
        
        handle_connection(conn, addr)
            


def main():
  start_threaded_server()

if __name__ == "__main__":
    main()
