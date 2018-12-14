import os
import socket


def main():
    host = '0.0.0.0'
    port = 8080

    # Create an INET, STREAMing socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allow socket to be reused right away (good for debugging)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print("Binding to {}:{}".format(host, port))
    serversocket.bind((host, port))

    # Become a server socket
    serversocket.listen(5)

    while True:
        # Accept connections from outside
        print("Listening for connections")
        (clientsocket, address) = serversocket.accept()
        print("A client has connected!")

        # Get request from the client
        http_request = b''
        receive_size = 5

        # Read data from socket until there is no data left
        while True:
            chunk = clientsocket.recv(receive_size)

            if chunk == b'':
                print("Client socket closed!")
                exit()

            http_request += chunk
            print("Part of HTTP Request:", http_request)

            # Check if the whole HTTP request has been received
            if contains_http_request(http_request):
                break

        print("We have a complete HTTP request:", http_request)

        # Build a response based on the request
        http_response = parse_http_request(http_request)
        print("Responding:", http_response)

        # Respond to request
        clientsocket.send(http_response)

        # Close the socket
        clientsocket.close()


def contains_http_request(data):
    return False


def parse_http_request(request):
    return b''


if __name__ == '__main__':
    main()
