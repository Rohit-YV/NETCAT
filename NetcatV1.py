import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return ""
    try:
        output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode()}"

class NetCat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()

    def send(self):
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)
        try:
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:
                        break
                if response:
                    print(response)
                    buffer = input('>')
                    buffer += '\n'  
                    self.socket.send(buffer.encode())

        except KeyboardInterrupt:
            print('User terminated.')
            self.socket.close()
            sys.exit()

    def handle(self, client_socket):
        try:
            if self.args.execute:
                output = execute(self.args.execute)
                client_socket.send(output.encode())

            elif self.args.upload:
                file_buffer = b''
                while True:
                    data = client_socket.recv(4096)
                    if not data:
                        break
                    file_buffer += data
                with open(self.args.upload, 'wb') as f:
                    f.write(file_buffer)
                message = f'Saved file {self.args.upload}'
                client_socket.send(message.encode())

            elif self.args.command:
                cmd_buffer = b''
                while True:
                    client_socket.send(b'BHP: #>')
                    while b'\n' not in cmd_buffer:
                        data = client_socket.recv(64)
                        if not data:
                            break
                        cmd_buffer += data
                    response = execute(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''

        except Exception as e:
            print(f'Exception: {e}')
        finally:
            client_socket.close()

    def listen(self):
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)
        print(f"Listening on {self.args.target}:{self.args.port}")

        while True:
            client_socket, addr = self.socket.accept()
            print(f"Accepted connection from {addr}")
            client_handler = threading.Thread(target=self.handle, args=(client_socket,))
            client_handler.start()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='BHP Net TOOL',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''example:
            netcat.py -t 192.168.1.1 -p 5555 -l -c #command shell
            netcat.py -t 192.168.1.1 -p 5555 -l -c -e='cat /etc/passwd' #execute command
            netcat.py -t 192.168.1.1 -p 5555 -l -c -u=my_test.txt #upload file
            echo 'ABC' | netcat.py -t 192.168.1.1 -p 5555  #echo text to server
            netcat.py -t 192.168.1.1 -p 5555 #connect to server
        ''')
    )
    parser.add_argument('-c', '--command', action='store_true', help='command shell')
    parser.add_argument('-e', '--execute', help='execute command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int, help='specified port')
    parser.add_argument('-u', '--upload', help='upload file')
    parser.add_argument('-t', '--target', help='specified IP address')

    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()

    nc = NetCat(args, buffer.encode())
    nc.run()
