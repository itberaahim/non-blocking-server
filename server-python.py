###############################################################################
# server-python.py
# Name: Raahim Owais
# EID: ro7655
###############################################################################

import sys
import socket
import _thread

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10

def handle_connection(thread_name, conn):
    data = conn.recv(RECV_BUFFER_SIZE)
    print(data.decode('utf-8'), end = '')
    # sys.stdout.write(data.decode('utf-8'))
    # sys.stdout.flush()
    conn.close()

def server(server_port):
    """TODO: Listen on socket and print received message to sys.stdout"""
    global QUEUE_SIZE

    # print('initializing socket')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', server_port))
        s.listen(QUEUE_LENGTH)

        while True:
            conn, addr = s.accept()
            # print('Connected by', addr)

            _thread.start_new_thread(handle_connection, ("", conn, ))


def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)

if __name__ == "__main__":
    main()
