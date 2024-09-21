import socket

server_address = ("192.168.1.6", 6980) # indirizzo ip e porta in una tupla
BUFFER_SIZE = 4092  # numero di byte massimo che posso mandare o ricevere
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # DGRAM --> protocollo UDP

message = "CIAO DA CLIENT"
try:
    udp_client_socket.sendto(message.encode(), server_address)
    data, address = udp_client_socket.recvfrom(BUFFER_SIZE)
    print(f'Messaggio ricevuto: {data.decode()} da {address}')  # decodifica dei dati

except OSError as e:
    print(f"ERRORE: {e}")

udp_client_socket.close()