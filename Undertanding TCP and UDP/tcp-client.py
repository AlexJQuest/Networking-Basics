# tcp-client.py
import numpy
import pandas as pd
import  pytz
from datetime import date, datetime
from socket import *
import pickle

#read in meeting data and do converstions to time and date
resevents = pd.read_excel("MeetingInfo.xlsx", index_col=0)
print(resevents)

time_format = "%Y/%m/%d"
now = datetime.now().strftime(time_format)
print(now)


cityname = pd.read_excel("MeetingInfo.xlsx", index_col=0, usecols="B" )
citytime = pd.read_excel("MeetingInfo.xlsx", index_col=0, usecols="C" )
citydate = pd.read_excel("MeetingInfo.xlsx", index_col=0, usecols="A" )

file = open("MeetingInfo.xlsx" , "rb")
filedata = file.read(1024)
#print(cityname)
#print(citytime)
#print(citydate)



serverName = "127.1.1.0"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
clientSocket.send(filedata)

clientSocket.close()


