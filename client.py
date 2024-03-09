import os, socket, time
import io
import csv
import sys
import numpy as np
import socket
import animation
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.animation as FuncAnimation
import nifgen
import subprocess
import nidaqmx
import os, socket, time
from nidaqmx.constants import Edge
from nidaqmx.constants import AcquisitionType
from nidaqmx.constants import TerminalConfiguration

while True:
    
    host = input("Enter Host Name:")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((host,5555))
        print("Connected Successfully")
    except:
        print("Unable to Connect")
        time.sleep(10)
        continue
        
    file_name = sock.recv(100).decode()
    file_size = sock.recv(100).decode()

    with open("pakhari.txt", "wb") as file:
        c = 0 
        
        start_time = time.time()
        
        while (file_size):
            data = sock.recv(1024)
            c += len(data)
            file.write((data))
            
            if not (data):
                break

    with open('pakhari.txt', 'r') as f:
            for data in f:
                print(data)
                
    end_time = time.time()    
        
    print("File Accept Complete. Total Time: ", end_time - start_time)

    sock.close()
    