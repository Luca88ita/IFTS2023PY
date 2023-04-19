import socket

UDP_IP_ADDRESS = "192.168.10.202"
UDP_PORT_NO = 12000

server_socket = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM
)  # nella libreria socket, chiami l'oggetto socket
server_socket.bind(
    (UDP_IP_ADDRESS, UDP_PORT_NO)
)  # bind serve per mettersi in ascolto, dando un IP ed un numero di porta

print("UDP server up and listening")

# preparazione all'applicazione
contatore = 0


# sviluppo l'applicazione
def app(msg):
    if msg[0:2] != "/n":
        return f"Protocollo errato"
    else:
        msg = msg[2:]
        try:
            numero = int(msg)
            contatore += numero
            return f"Siamo al numero: {contatore}"
        except:
            return f"Accetto solo numeri interi!"


while True:
    data, addr = server_socket.recvfrom(1024)  # qui ascolto la richiesta
    print(
        "Received message: ", addr, data.decode()
    )  # stampo a video l'indirizzo e i dati decodificati
    msg = data.decode()  # messaggio testuale

    if addr[0] == UDP_IP_ADDRESS and data.decode() == "quit":
        print("sto chiudendo il server...")
        break

    resp = app(msg)

    server_socket.sendto(resp.encode(), addr)


print("server chiuso")
