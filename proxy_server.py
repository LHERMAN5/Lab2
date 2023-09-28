#!/usr/bin/env python3
import socket, sys
import time
from threading import Thread

#define address & buffer size
HOST = "127.0.0.1"
PORT = 8080
BUFFER_SIZE = 4096

def send_request(host, port, request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
        c.connect((host, port))
        c.send(request)
        c.shutdown(socket.SHUT_WR)
        data = c.recv(BUFFER_SIZE)
        result = b'' + data

        while len(data) > 0:
            data = c.recv(BUFFER_SIZE)
            result += data
        return result

def handle_connection(conn, addr):
    print("Connected by", addr)

    request = b''
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        print(data)
        request += data
    response = send_request("www.google.com", 80, request)
    conn.sendall(response)

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
        

        s.bind((HOST, PORT))
        s.listen(2)
        
        conn, addr = s.accept()
        
        handle_connection(conn, addr)
            


def main():
  start_threaded_server()

if __name__ == "__main__":
    main()
