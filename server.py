import socket

server_address = ("192.168.1.6", 6980) # indirizzo ip e porta in una tupla
BUFFER_SIZE = 4092  # numero di byte massimo che posso mandare o ricevere
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # AF_INET --> ipV4
                                                                        # DGRAM --> protocollo UDP
udp_server_socket.bind(server_address) # associazione del socket all'indirizzo ip e alla porta


data, address = udp_server_socket.recvfrom(BUFFER_SIZE) # BLOCCANTE (è in ascolto)
# address --> indirizzo che fa la richiesta
# data --> dati inviati da quell'indirizzo

message = "CIAO DA SERVER"
print(f'Messaggio ricevuto: {data.decode()} da {address}')  # decodifica dei dati
udp_server_socket.sendto(message.encode(), address)
udp_server_socket.close()