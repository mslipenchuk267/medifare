# server.py
# Usage: ./server <port number>
# This is the main server process that creates and dispatches
#  threads to clients.

import socket, sys
from _thread import *
import threading
from fuzzywuzzy import process
#import warnings
#warnings.filterwarnings('ignore')
  
# Global vars
medical_procedures_dict =   {
  "knee replacement x-ray": 300,
  "knee alignment anesthesia": 3000,
  "eye glasses exam": 30,
  "Lasik eye surgery": 1900
}

# util functions
def visualize_results(user_query, best_match, price):
    user_info = "User Search: " + user_query
    print(user_info)
    matched_info = "Matched Result: " + best_match + " : $" + str(price)
    print(matched_info)

# thread function service_client 
def service_client(c): 
    while True: 
        # 1. data received from client 
        user_search_query = c.recv(1024) 
        if not user_search_query: 
            print('...exiting client') 
  
            break
        # convert ascii bytes to string
        user_search_query = str(user_search_query.decode('ascii'))

        # 2. Search query in medical treatment list
        medical_procedure_list = medical_procedures_dict.keys()
        # Score user query against procedure list
        match_scores = process.extract(user_search_query,medical_procedure_list)
        print("Match Scores:")
        print(match_scores)
        # Select the string with the highest matching percentage
        best_match = process.extractOne(user_search_query,medical_procedure_list)
        print("Best Match:")
        print(best_match)

        matched_procedure_price = medical_procedures_dict[best_match[0]]

        # 3. Display Result
        visualize_results(user_search_query, best_match[0], matched_procedure_price)

        # 4. send back reversed string to client 
        response = best_match[0] + " : $" + str(matched_procedure_price)
        c.send(response.encode('ascii')) 
  
    # connection closed 
    c.close() 
  
  
def Main(): 
    host = "" 
    port = int(sys.argv[1])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # allow address/port to be reused immediately after end of program
    # this is so we don't get stuck in TIME_WAIT for a few
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bind server
    s.bind((host, port)) 
    print("Server socket binded", port) 

    # put the socket into listening mode 
    s.listen(5)
    print("Server is listening")

    # a forever loop until client wants to exit 
    while True: 
        # Receive client
        c, addr = s.accept() 

        # lock acquired by client 
        #print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 

        # Start a new thread to service client
        start_new_thread(service_client, (c,)) 

    s.close() 

if __name__ == '__main__': 
    Main() 
