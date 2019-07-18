import socket
def main():
    host='localhost'
    port=5000

    #Create socket
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Created Socket")

    #bind host and port
    s.connect((host,port))
    print("Connected to the server")

    message= input("Enter message to send to server:\n ")
    
    print("Enter 'q' to quit sending messages")
    while message!='q':
        s.send(str.encode(message,'utf-8'))
        data=s.recv(1024).decode('utf-8')
        print("Data received from Server:{}".fromat(data))
        message=input('Enter message to send to server:\n')
        print(message)
    s.close
if __name__=='__main__':
    main()
