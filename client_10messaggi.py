import socket

num_messaggi = 10

# configurazione del client
server_address = ("192.168.1.6", 6980) # indirizzo ip e porta in una tupla
BUFFER_SIZE = 4092  # numero di byte massimo che posso mandare o ricevere

# creazione del socket UDP
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # DGRAM --> protocollo UDP

# invio dieci messaggi
for i in range(num_messaggi):
    message = (f"Messaggio n {i+1} dal CLIENT")
    udp_client_socket.sendto(message.encode(), server_address)
    data, address = udp_client_socket.recvfrom(BUFFER_SIZE)
    print(f'Messaggio ricevuto: {data.decode()} da {address}')  # decodifica dei dati

udp_client_socket.close()