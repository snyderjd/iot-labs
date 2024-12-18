import bluetooth

hostMACAddress = "D8:3A:DD:70:92:5D" # The address of Raspberry PI Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 0
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
print("listening on port ", port)
try:
    client, clientInfo = s.accept()
    while 1:   
        print("server recv from: ", clientInfo)
        data = client.recv(size)
        if data:
            print(data.decode("utf-8"))
            client.send(data.encode("utf-8")) # Echo back to client
except: 
    print("Closing socket")
    client.close()
    s.close()

