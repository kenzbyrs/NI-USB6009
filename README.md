# NI-USB6009
The remote control system uses a client and server to retrieve data acquisition from the NI USB6009 device.

# NI.py
First, you can see the packages and libraries used and can be installed first via pip install ...
The server will take the IP port on the signal used which will later be received by the client.
This is the server part for the socket program to connect the TCP/IP port on the client and the National Instrumentation USB6009 device connectivity.
run the data acquisition tool from the NI USB 6009 tool, to make it into a .txt file that will be sent to the client.

# Client.py
This client section displays the appropriate host port column from the server, so that it can connect and run.
and receives acquisition data from the server in the form of a .txt file to be represented as a graphic plot.

# Conclusion of how it works
A python software development for using data acquisition tools, namely National Instrumentation USB6009. To get this system there must be a tool first, if it isn't there then the server system will not be able to run.
1. The NIUSB6009 device must be connected to the laptop
2. Run the python code in the NI.py file on the terminal and you will get the IP signal
3. Run the python code in the Client.py file and enter the IP port that you got from the server
4. After that the server will work to acquire data from the NI USB6009 device which is immediately made into a .txt file to be sent to the client
5. After the server has finished sending the .txt file, the client will automatically receive it in real time and save the .txt file in the directory.
6. After that, the .txt file containing the acquisition data will immediately be displayed as a graphic signal plot
7. This process will continue to repeat itself several times according to the client's request.



