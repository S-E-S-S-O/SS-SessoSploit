import socket
import sys

def serop():
    #Taking some input
    port = input("Please tell the port you want to listen on \n")
    port = int(port)

    #Making the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("localhost", port)
    print("Server started")
    sock.bind(server_address)

    sock.listen(1)

    while True :
        print ("Waiting for a connection")
        connection, client_address = sock.accept()
        try:
            client_address = str(client_address)
            print("We got a connection from" + client_address)
            while True:
                data = connection.recv(16)
                data = str(data)
                print ("received \n "+ data)
                if data:
                    print ("sending data back to the client")
                    connection.send(b'Hello Client !!')
                else:
                    print("no more data from" + client_address)
                    break
                
        finally:
            print("Done")
