###############################################################################
# client-python.py
# Name: Raahim Owais
# EID: ro7655
###############################################################################

import sys
import socket
import time

SEND_BUFFER_SIZE = 2048

def client(server_ip, server_port):
    """TODO: Open socket and send message from sys.stdin"""
    print('initializing socket')
    
    input_str = sys.stdin.read(SEND_BUFFER_SIZE)
    while input_str:
        print('sending chunk')
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((server_ip, server_port))
            s.send(input_str.encode('utf-8'))
            s.close()
            # # print(input_str, end='')
            time.sleep(1)

            input_str = sys.stdin.read(SEND_BUFFER_SIZE)
        except socket.error as error:
            print('error sending')
            print(error)
            time.sleep(1)
            # print('reconnecting')
            # s.close()
            # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # s.connect((server_ip, server_port))


def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit("Usage: python client-python.py [Server IP] [Server Port] < [message]")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client(server_ip, server_port)

if __name__ == "__main__":
    main()
