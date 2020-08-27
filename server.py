import sys
import string
import select
import socket as sock

def set_up_server() {
    store_addresses = {}
    username = ""
    connected_users = {}
    port = 5050

    new_socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

    new_socket.bind(("localhost", port))

    new_socket.listen(30)

    connected_users.append(new_socket)

    return new_socket
}

def send_message(sock, msg, connections):
    for socket in connections:
        if sock != new_socket and sock != socket:
            try:
                socket.send(msg)
                return True
            except:
                connected_users.remove(socket)
                socket.close()
                return False

def accept_connection(new_socket):
    upsock, address = new_socket.accept()
    uname = upsock.recv(buffer)
    connected_users.append(upsock)


def _main_():
    new_server = set_up_server()
    send_message(sock, msg)

    while True:
        l_curr_socks, r_curr_socks, read_sockets = select.select(connected_users, [], [])

        for curr_sock in r_curr_socs:
            if curr_sock == socket:
                accept_connection(read_sockets)
            else:
                try:
                    init_info = upsock.recv(2032)
                    final_info = init_info[init_info.index("\n")]
                    new_msg = final_info

                    if init_info != "":
                        send_message(socket, new_msg, r_curr_socks)
                except:
                    curr_sock.getpeername()
                    connected_users.remove(curr_sock)
                    connected_users.close()
                    del store_addresses[(name, current)]
    new_server.close()

            
                



