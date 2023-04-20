import socket

UDP_IP = "192.168.0.152"  # 202"
UDP_PORT = 12000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

nome = input("Inserire nome\n")
msg = f"/r{nome}"
sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024)
    print(f"{data.decode()}")
    # messaggio = input("Scrivi un messaggio\n")
    # messaggio = f"/m{messaggio}"
    # sock.sendto(messaggio.encode(), (UDP_IP, UDP_PORT))

sock.close()
