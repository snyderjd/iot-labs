import socket

# The address of Raspberry Pi bluetooth adapter on the server. The server might have multiple bluetooth adapters
hostMACAddress = "D8:3A:DD:70:92:5D"
port = 1 # Port must be set explicitly (typically 1 for Bluetooth RFCOMM)
backlog = 1
size = 1024

# Create a bluetooth socket
server_sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server_sock.bind((hostMACAddress, port))
server_sock.listen(backlog)

print(f"Listening on {hostMACAddress}, port {port}")

try:
    client_sock, client_info = server_sock.accept()
    print(f"Accepted connection from {client_info}")

    while True:
        data = client_sock.recv(size)
        if data:
            print("Received: ", data.decode("utf-8"))
            client_sock.send(data) # Echo back the received data
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Closing sockets")
    client_sock.close()
    server_sock.close()

# import bluetooth

# hostMACAddress = "D8:3A:DD:70:92:5D" # The address of Raspberry PI Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
# port = 0
# backlog = 1
# size = 1024
# s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# s.bind((hostMACAddress, port))
# s.listen(backlog)
# print("listening on port ", port)
# try:
#     client, clientInfo = s.accept()
#     while 1:   
#         print("server recv from: ", clientInfo)
#         data = client.recv(size)
#         if data:
#             print(data.decode("utf-8"))
#             client.send(data.encode("utf-8")) # Echo back to client
# except: 
#     print("Closing socket")
#     client.close()
#     s.close()
