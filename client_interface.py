import socket as sock
import string
import sys
import select
import server.py

def input_name() {
  username = raw_input()
  connection = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
}

def connect(connection, username) {
    if connection.connect(hosting, curr_port):
        print("Connected!")
        connection.send(username)
    else:
        sys.exit()
}

def print_message(data) {
    sys.stdout.write(data)
}

def get_message(connection) {
    message=sys.stdin.readline()
    connection.send(message)
}
def talk(connection, conversation) {
    for msg in conversation:
        if msg == connection:
            information = msg.recv(5050)
            if information:
                print_message(information)
            else:
                print 'Error!'
                sys.exit()
        else:
            information = sys.stdin.readline()
            connection.send(information)
}

def _main():
    if len(sys.argv) > 1:
        hosted = sys.argv[1]
    else:
        hosted = input("Indicate IP Address")
    
    port_address = 5050

    connection, username

    input_name()

    connect(connection, username)

    talk(connection, conversation)
