import socket

num_messaggi = 10

# configurazione server
server_address = ("192.168.1.6", 6980) # indirizzo ip e porta in una tupla
BUFFER_SIZE = 4092  # numero di byte massimo che posso mandare o ricevere

# creazione socket UDP
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # DGRAM --> protocollo UDP
udp_server_socket.bind(server_address) # associazione del socket all'indirizzo ip e alla porta


print("Server UDP in ascolto")

# loop per ricevere messaggi
for _ in range(num_messaggi):
    data, address = udp_server_socket.recvfrom(BUFFER_SIZE) # BLOCCANTE (è in ascolto)
    # address --> indirizzo che fa la richiesta
    # data --> dati inviati da quell'indirizzo

    print(f"Messaggio ricevuto da {address}: {data.decode()}")
    udp_server_socket.sendto(b"Messaggio ricevuto", address)    # b --> indica che è una stringa di byte

udp_server_socket.close()