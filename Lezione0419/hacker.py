import socket

UDP_IP = "192.168.10.61"  # 202"  # replace with the IP address of destination
UDP_PORT = 12000  # replace with the port number of the destination

message = input("inserire un messaggio: ")
# create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

""" for i in range(10):
    message = f"Prova Luca {i+1}"
    # send the message
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT)) """


sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
# data, addr = sock.recvfrom(1024)
# print(f"{data.decode()}")

# Close the connection
sock.close()
