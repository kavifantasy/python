import socket
import logging
def main():
   # logging.basicConfig(filename="C:\\Users\\admin\\Desktop\\visual python\\log.log",level=logging.DEBUG)
    #logger=logging.getLogger()  (or) following method
    LOG_FORMAT="%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(
        filename="C:\\Users\\admin\\Desktop\\visual python\\log.log",
        level=logging.DEBUG,
        format=LOG_FORMAT,
        filemode='w'

    )
    logger=logging.getLogger()
    host='192.168.11.196'
    port=5002

    #create socket
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Created socket")
    logger.info("created Socket")

    #bind host and port to socket
    s.bind((host,port)) #In tuple format
    print("Binded host and port to socket")
    logger.debug("Binded")
    #listen one connection at a time
    s.listen(1)

    #Accept connection
    print("Waiting for client to connect...")
    conn,addr=s.accept()
    print("Connection from:"+str(addr))

    #Server runs infinitely for
    #send and recv messages
    while True:#infinite loop
        #receive 1024 bytes of data from client at a time
        data=conn.recv(1024).decode('utf-8')
        #{
        if not data:
            break
        print(data)
        #data=data.lower()
        #} if u want to change functionality change code here
       # print("Sending:"+data)
        conn.send(input("Enter your message to client:").encode("utf-8"))
    conn.close()

if __name__=="__main__":
    main()