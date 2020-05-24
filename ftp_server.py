import socket   
import os
import sys
import pickle       

# next create a socket object 
s = socket.socket()
print ("Socket successfully created!")
port = 9090
s.bind (('127.0.0.1', port))
print ("Socket binded to port %s" %(port))
s.listen(5)
#files:
###***Path is directory of ftp files:
path = './'
fileslist=[]
filesdirectorylist=[]
for r, d, f in os.walk(path):
    for file in f:
        fileslist.append(os.path.join(file))
        filesdirectorylist.append(os.path.join(r , file))
#printing list in server:
for f in fileslist:
    print("list")
    print(f)
print ("Socket is listening!")
listtosend = pickle.dumps(fileslist)
while True:
    c, addr = s.accept()     
    print ('Got connection from', addr )
#receiving commands
    data = c.recv(1024)
    data = data.decode()
    print('revieved command is: ', data)
    if(data== "List"):
        c.send(listtosend)
        print("List sent !")
    elif(data== "Retrieve"):
        filename = c.recv(1024)
        filename = filename.decode()
        print("filename is: " , filename)
        if filename in fileslist:
            #finding its directory:
            i = fileslist.index(filename)
            filedir = filesdirectorylist[i]
            file = open(filedir , 'r')
            l = file.read(1000)
            while(l):
                c.send(l.encode())
                l = file.read(1000)
            file.close()
            print("EOF!")
        else:
            print("File NOT FOUND!")
            os.remove("_C"+filename)
            msg = "file not found!"
            c.send(msg.encode())
        c.close()
        #sys.exit()
    elif(data== "Delete"):
        filename = c.recv(1024)
        filename = filename.decode()
        print("Deleting...")
        if filename in fileslist:
            i = fileslist.index(filename)
            filedir = filesdirectorylist[i] 
            os.remove(filedir)
            print("Done!")
            print("file "+filename+" has deleted successfully!")
            c.send("Deleted successfully!".encode())
        else:
            print("file NOT FOUND!")
            c.send("NOT FOUND!".encode())
        c.close()
        #sys.exit()
        #else:
            #print("NOT FOUND!")
    else :
        c.send("Invalid commad!".encode())
        print("Invalid commad!")
        c.close()
        #sys.exit()

# Close the connection with the client 
c.close() 