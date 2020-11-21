import socket
import sys


# Create socket (allows two computers to connect)
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print('Socket creation error: {}'.format(msg))


# Bind socket to port and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print('Binding socket to port: {}'.format(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print('Socket binding error: {}\nRetrying...'.format(msg))


# Establish a connection with client (socket must be listening for them)
def socket_accept():
    conn, addr = s.accept()
    print('Connection has been established | IP {} | Port {}'.format(
        addr[0], str(addr[1])))
    send_commands(conn)
    conn.close()


# Send commands
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), 'utf-8')
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()


main()
