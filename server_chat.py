import socket

server_address = ("192.168.1.6", 6980) # indirizzo ip e porta in una tupla
BUFFER_SIZE = 4096 # numero di byte massimo che posso mandare o ricevere

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # DGRAM --> protocollo UDP
udp_server_socket.bind(server_address) # associazione del socket all'indirizzo ip e alla porta

print("Server in ascolto...")

while True:
    data, address = udp_server_socket.recvfrom(BUFFER_SIZE)
    print(f'Messaggio ricevuto: {data.decode()} da {address}')
    
    message = input("Scrivi un messaggio per il client: ")
    udp_server_socket.sendto(message.encode(), address)
