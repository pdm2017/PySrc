# Net02.py
# Client
# command B 창에서 실행 
from socket import *
svrIP = '59.29.224.106'
svrPort = 64000
svrAddr = (svrIP,svrPort)
cliSocket = socket(AF_INET,SOCK_STREAM)

# Server 연결
cliSocket.connect(svrAddr)

# 메세지 수신(recv)
data = cliSocket.recv(1024)
print(data.decode('utf-8'))

# 메세지 전송(send)
cliSocket.send(b"Hello Server")
