# preparazione all'applicazione
utenti = {}


# sviluppo l'applicazione
def app(addr, msg):
    command = msg[0:2]
    payload = msg[2:]
    if command == "/r":
        # TODO registrare l'utente
        utenti[payload] = addr
        for nome, add in utenti.items():
            server_socket.sendto(
                f"Server: {nome}: sta partecipando alla chat".encode(), add
            )

    elif command == "/m":
        # TODO leggere il messaggio e inoltrarlo
        index = payload.find("\n")
        nome = payload[:index]
        messaggio = payload[index + 1 :]
        for nome, add in utenti.items():
            server_socket.sendto(f"{nome}: {messaggio}".encode(), add)

    elif command == "/l":
        # TODO leggere solo se non va in porto prima
        pass

    elif command == "/e":
        # TODO loggoutare
        pass
    else:
        # TODO ritornare messaggio con comando non valido
        pass

    return f"utente: {utenti}"


import socket

UDP_IP_ADDRESS = "192.168.0.152"
UDP_PORT_NO = 12000

server_socket = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM
)  # nella libreria socket, chiami l'oggetto socket
server_socket.bind(
    (UDP_IP_ADDRESS, UDP_PORT_NO)
)  # bind serve per mettersi in ascolto, dando un IP ed un numero di porta

print("UDP server up and listening")
while True:
    data, addr = server_socket.recvfrom(1024)  # qui ascolto la richiesta
    print(
        "Received message: ", addr, data.decode()
    )  # stampo a video l'indirizzo e i dati decodificati
    msg = data.decode()  # messaggio testuale

    if addr[0] == UDP_IP_ADDRESS and data.decode() == "quit":
        print("sto chiudendo il server...")
        break

    resp = app(addr, msg)

    # server_socket.sendto(resp.encode(), addr)


print("server chiuso")
