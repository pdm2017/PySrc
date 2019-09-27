# Net01.py
# Server
# command A 창에서 실행 
from socket import *
svrIP = '59.29.224.106' # Host IP
svrPort = 64000
svrAddr = (svrIP,svrPort)
svrSocket = socket(AF_INET,SOCK_STREAM)
svrSocket.bind(svrAddr)
svrSocket.listen(0)
# Listening 상태 완료

# Connect  허락 
cliSocket, cliAddr = svrSocket.accept()

# 메세지 전송(send)
cliSocket.send(b"Welcome Py Server")

# 메세지 수신(recv)
data = cliSocket.recv(1024)
print(data.decode('utf-8'))
