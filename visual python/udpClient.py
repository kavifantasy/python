import socket
def main():
    host='localhost'
    port=5005

    server=(host,port)

    #Create socket
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("Created Socket")

    #bind host and port
    s.bind(('localhost',5005))
    print("Connected to the server")

    message= input("Enter message to send to server:\n ")
    
    print("Enter 'q' to quit sending messages")
    while message!='q':
        s.sendto(message.encode('utf-8'),server)
        data, addr = s.recvfrom(1024)
        data=data.decode('utf-8')
        print("Data received from Server:{}"+data)
        message=input('Enter message to send to server:\n')
        
    s.close
if __name__=='__main__':
    main()
