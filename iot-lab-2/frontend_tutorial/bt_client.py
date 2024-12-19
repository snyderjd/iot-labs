import socket

host = "D8:3A:DD:70:92:5D"  # Update with the server's Bluetooth MAC address
port = 1  # RFCOMM port

try:
    sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    sock.connect((host, port))
    print("Connected successfully!")

    # Test sending data
    sock.send("Hello, Server!".encode("utf-8"))

    # Receive response
    data = sock.recv(1024).decode("utf-8")
    print("From server:", data)

    while 1:
        text = input("Enter your message: ")
        if text == "quit":
            break

        sock.send(text.encode("utf-8"))
        data = sock.recv(1024).decode("utf-8")
        print(f"From server: {data}")

    sock.close()
except Exception as e:
    print("Bluetooth error:", e)

# import bluetooth

# host = "D8:3A:DD:70:92:5D" # The address of Raspberry PI Bluetooth adapter on the server.
# port = 1
# sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# sock.connect((host, port))
# while 1:
#     text = input("Enter your message: ") # Note change to the old (Python 2) raw_input
#     if text == "quit":
#         break
#     sock.send(text.encode("utf-8"))

#     data = sock.recv(1024).decode("utf-8")
#     print("from server: ", data)

# sock.close()

