from socket import *
import os

# Set the server port number
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

#bind socket to a specific port
serverSocket.bind(("", serverPort))

#start accepting connections
serverSocket.listen(1)


print("The server is ready to receive")

while True:
    #to create socket for the connection
    connectionSocket, addr = serverSocket.accept()

    #to receive http request from client and decode it
    sentence = connectionSocket.recv(1024).decode()

    #split the Http request sent into lines
    group_requests = sentence.split("\n")

    #only take first line of request
    firstLine = group_requests[0].strip()
    command, url, version = group_requests[0].split(" ")
    url = url.replace("/", "")

    print("Command" + command)
    print("url :" + url)
    print("version" + version)

    #I removed the location for privacy purpose.
    #check if the file exists
    if os.path.isfile("location of where the http file will be" + url):
        #if file exist, read
        with open("coen366.html", "r") as file:
            content = file.read()
        # Set the HTTP response status and headers
        status_line = "HTTP/1.1 200 OK\r\n"
        headers = "Content-Type: text/html\r\n\r\n"
        response = status_line + headers + content
        #to send response to client
        connectionSocket.sendall(response.encode())
    else:
        #send 404 if file not found
        print("does not exist " + url)
        status_line = "HTTP/1.1 404 OK\r\n"
        headers = "Content-Type: text/plain\r\n\r\n"
        response = status_line + headers + "Error 404: File not found - " + url
        #send response to client
        connectionSocket.sendall(response.encode())

    get_request = group_requests[0].split("/")
    print(get_request)

    capitalizedSentence = sentence.upper()

    #close connection socket
    connectionSocket.close()
