import socket as s
import threading as t

SERVER_ADDRESS = ("localhost", 12345)
BUFFER_SIZE = 4096

def main():
    server_UDP = s.socket(s.AF_INET, s.SOCK_DGRAM)
    server_UDP.bind(SERVER_ADDRESS)
    _, client_address = server_UDP.recvfrom(BUFFER_SIZE)
    print(f"connessione a {client_address}")
    server_UDP.sendto("Starting communication...".encode(), client_address)
    # Crea i thread per inviare e ricevere messaggi
    thread_invio = t.Thread(target=invio, args=(server_UDP, client_address))
    ricezione()
    thread_invio.start()

# Funzione per inviare messaggi
def invio(server_UDP, client_address):
    while True:
        data = input("")
        server_UDP.sendto(data.encode('utf-8'), client_address)
        if data.lower()=="exit":
            print("chiudo la connessione")
            break

# Funzione per ricevere messaggi
def ricezione(server_UDP):
    while True:
        data, address = server_UDP.recvfrom(BUFFER_SIZE)
        print(f"Client {address}: {data.decode('utf-8')}")
        if data.decode('utf-8').lower()=="exit":
            print("chiudo la connessione")
            break

if __name__ == "__main__":
    main()