import socket

UDP_IP = "192.168.10.61"  # 202"
UDP_PORT = 12000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

nome = input("Inserire nome\n")
msg = f"/r{nome}"
sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024)
    print(f"{data.decode()}")
    # messaggio = input("Scrivi un messaggio\n")
    # sock.sendto(messaggio.encode(), (UDP_IP, UDP_PORT))

sock.close()
