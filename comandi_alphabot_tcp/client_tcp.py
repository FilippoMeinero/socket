import socket

#10.210.0.76
server_address = ("localhost", 6980)  # indirizzo IP e porta in una tupla
BUFFER_SIZE = 4096  # numero di byte massimo che posso mandare o ricevere

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # STREAM --> protocollo TCP
tcp_client_socket.connect(server_address)

try:
    while True:
        message = input("Scrivi un messaggio per il server: ")
        tcp_client_socket.sendall(message.encode())
finally:
    tcp_client_socket.close()