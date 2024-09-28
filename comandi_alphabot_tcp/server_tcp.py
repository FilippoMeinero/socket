import socket

server_address = ("localhost", 6980)  # indirizzo IP e porta in una tupla
BUFFER_SIZE = 4096  # numero di byte massimo che posso mandare o ricevere

# creazione del socket TCP
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind(server_address)
tcp_server_socket.listen(1)  # il server è in ascolto per una connessione

print("Server in ascolto su {}:{}".format(*server_address))

try:
    while True:
        print("In attesa di una connessione...")
        connection, client_address = tcp_server_socket.accept()
        print("Connessione stabilita con", client_address)

        try:
            while True:
                data = connection.recv(BUFFER_SIZE)
                if data:
                    print("Messaggio ricevuto:", data.decode())
                else:
                    break
        finally:
            connection.close()
            print("Connessione chiusa con", client_address)
finally:
    tcp_server_socket.close()
    print("Server chiuso")
