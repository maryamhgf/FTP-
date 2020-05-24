# FTP-
Implementation of FTP server and clients can delete, retrieve, and take list of files.


***All ftp files should be in ftp_server.py directory, or you can easily change the path in code.***

Server:(Ubuntu)

1. Open terminal and type cd "directory of the codes".

2. The server will be run in port 9090(you can change it in the code.)

3. Type python ftp_server.py -sp 9090 in the terminal.

Client:(Ubuntu)

1. Open a new terminal and type cd "directory of the codes".

2. Type python ftp_client.py sip- server-ip sp- 9090 (For example: python client.py sip- 9090 sp- 9090)

For every new client open a new terminal and type the previous command.

Commands:

1. Delete name of file: server will delete that file.

2. List: client can see all the files.

3. Retrieve name of file: server will send the file in 10000B parts. 

For new command client should establish a new connection.
