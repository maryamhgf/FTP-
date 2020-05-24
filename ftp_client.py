import socket
import os
import sys
import pickle           
# Create a socket object 
s = socket.socket()      
# Define the port on which you want to connect 
port = 9090               
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
#send command to server
user_command = input("what is your command? ")
print(user_command)
s.send(user_command.encode())
#receiving data
while True:
    if(user_command== "List"):
        print("receiving list...")
        data = s.recv(1000)
        data = pickle.loads(data)
        print("List : " , (data))
        if not data:
            print("ERROR!")
            s.close()
            break
        sys.exit()
    elif(user_command == "Retrieve"):
        file_name = input("Please insert file name: ")
        s.send(file_name.encode())
        print("recieving " , file_name)
        newfilename = "_C"+file_name
        newfile = open(newfilename , 'w+')
        while True:
            filedata = s.recv(1000)
            filedata = filedata.decode()
            newfile.write (filedata)
            if not filedata:
                msg = s.recv(1000)
                msg = msg.decode()
                print(msg)
                print("EOF!")
                s.close()
                sys.exit()   
        newfile.close()
        s.close()   
    elif(user_command== 'Delete'):
        file_name = input("Please insert file name: ")
        s.send(file_name.encode())
        msg = s.recv(1024)
        msg = msg.decode()
        print(msg)
        print("file:  " , file_name)
        s.close()
        sys.exit()
    else:
        print("ERROR!")
        break
# close the connection 
s.close()
sys.exit()    
