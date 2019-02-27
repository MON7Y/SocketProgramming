import socket

host='localhost'
port=4000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

s.listen(1)
print("Server listening on port:",port)
c,addr = s.accept()

print("Connection from:",str(addr))

c.send(b"Hellooooo")
c.close()






