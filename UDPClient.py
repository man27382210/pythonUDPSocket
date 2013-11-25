from socket import *
serverName='127.0.0.1'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('',5432))
# message = raw_input('xxxxxxxx')
message ='xxxxxx'
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
print serverAddress
clientSocket.close()