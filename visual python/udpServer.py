import socket
def main():
    host='localhost'
    port=5006

    #create socket
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("Created socket")

    #bind host and port to socket
    s.bind((host,port)) #In tuple format
    print("Binded host and port to socket")
    

    #listen one connection at a time
    #s.listen(1)

    #Accept connection
    print("Waiting for client to connect...")
    print("Connection from:"+str(addr))

    #Server runs infinitely for
    #send and recv messages
    while True:#infinite loop
        #receive 1024 bytes of data from client at a time
        data, addr = s.recvfrom(1024)
        data=data.decode('utf-8')
        print("Message from:"+str(addr))
        #{
        #if not data:
        #    break
        print(data)
        data=data.upper()
        #} if u want to change functionality change code here
        rint("Sending:"+data)
        s.sendto(data.encode("utf-8"),addr)
    conn.close()

if __name__=="__main__":
    main()