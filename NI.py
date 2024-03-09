import sys
import socket
import animation
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.animation as FuncAnimation
import nidaqmx
import nifgen
import time
import subprocess       
import os, socket, time
import numpy as np
from nidaqmx.constants import Edge
from nidaqmx.constants import AcquisitionType
from nidaqmx.constants import TerminalConfiguration

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 5555))
sock.listen(5)

while True:
    
    print("HOST:", sock.getsockname())

    client, addr = sock.accept()

    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan('Dev1/ai0', terminal_config=TerminalConfiguration.RSE)
        task.timing.cfg_samp_clk_timing(48000, source="", active_edge=Edge.RISING, sample_mode=AcquisitionType.FINITE, samps_per_chan=100)
        data = task.read(100)
        print(data)

        with open('pakhari.txt', 'w') as f:
            f.write(f"{data}")

        x = []
        y = []

        x = np.arange(100)
        y = data

        plt.plot(x, y)
        plt.show()
        plt.cla()

        file_name = "pakhari.txt"
        file_size = os.path.getsize(file_name)

        client.send(file_name.encode())
        client.send(str(file_size).encode())

        with open("pakhari.txt", "rb") as file:
            c = 0
            start_time = time.time()

            while c <= file_size:
                data = file.read(1024)
                if not data:
                    break
                client.sendall(data)
                c += len(data)

        end_time = time.time()

        print("File Transfer Complete. Total Time:", end_time - start_time)

    client.close()

