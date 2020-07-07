# FTP
Implementation of FTP protocol using socket programming. Clients can delete files, retrieve files, and get a list of files.
Here is how to run the server and the client on linux machines:
All ftp files should be in the same directory as the ftp_server.py file, or you can easily change the path in the code.

Server:

1. Open the terminal and cd to the directory of the codes.

2. In the terminal run the server by: “python ftp_server.py -sp 9090”.

(The server will be run on port 9090).

Client:

1. Open another terminal and cd to the directory of the codes.

2. In the terminal run the client by: “python ftp_client.py -sip 127.0.0.1 -sp 9090”

(Connecting to a server running on localhost and port number 9090)

In the client side, you can type the following commands for their specific purposes:

Delete: you are asked to insert the file name which will be deleted by the server.

List: the server will provide the client with a list of all the files.

Retrieve: you are asked to insert the file name for retrieval. The server will send the client the requested file in 10000B chunks.

Please note that the client should establish a new connection for a new command.

A record of the clients' commands and the server’s responses will be shown in the server’s terminal.
