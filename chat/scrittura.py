import socket

UDP_IP = "192.168.0.152"
UDP_PORT = 12000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
    while True:
        message = input("Inserire un numero:")
        try:
            int(message)
        except:
            continue
        message = f"/n{message}"
        break

    sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
    data, addr = sock.recvfrom(1024)
    print(f"{data.decode()}")

    risposta = input("Vuoi continuare? (y/n)")
    if risposta.lower() != "y":
        break

sock.close()
