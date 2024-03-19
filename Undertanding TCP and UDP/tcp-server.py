# tcp-server.py
import pandas as pd
from socket import *
import pickle
import xlsxwriter

# create the socket
# AF_INET == ipv4
# AF_INET6 == ipv6
# SOCK_STREAM == TCP
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
#bind a socket to some port on the server
serverSocket.bind(("",serverPort))
serverSocket.listen(5)
print ("The server is ready to receive")

MeetingSA =  xlsxwriter.Workbook("MeetingInfoSA.xlsx")
sheet1 = MeetingSA.add_worksheet()



while True:
     connectionSocket, addr = serverSocket.accept()
     SAdata = connectionSocket.recv(1024)
     sheet1.write(SAdata)
     MeetingSA.close()
     connectionSocket.close()
