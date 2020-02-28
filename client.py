# client.py
# Usage: ./client <host> <port number>
# This is a client used for testing the functionality of the server
# Import socket module 
import socket, sys  
  
def Main(): 
    host = sys.argv[1] # local host IP '127.0.0.1' 
    port = int(sys.argv[2])
    #query = sys.argv[3]
    # Setup client socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    print("client socket made")

    # connect to server
    s.connect((host,port)) 
  
    # message you send to server     
    while True: 
        user_query = input('\nEnter a query : ') 
        # message sent to server 
        s.send(user_query.encode('ascii')) 
  
        # messaga received from server 
        data = s.recv(1024) 
  
        # print the received message 
        # here it would be a reverse of sent message 
        print('Received from server :',str(data.decode('ascii'))) 
  
        # ask the client whether he wants to continue 
        ans = input('\nMake another Query(y/n) :') 
        if ans == 'y': 
            continue
        else: 
            break
    # close the connection 
    s.close() 
  
if __name__ == '__main__': 
    Main() 
