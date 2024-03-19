#Adrian Alex Jacobs
#3850269


import socket

c = socket.socket()

c.connect(("localhost",9999))

print(c.recv(1024).decode())



#contains a file
# write data in a file.
file1 = open("Routes.txt","w")
L = ["This program returns the shortest paths your current trip\n"] 


#provides a source and destination location to server
print("This program will return the shortest paths your current trip\n")
src = input("\nEnter your start point\n  Bellville\nNyanga\n Bellville South\nPhilippi\nMatland\nParow\nLandsdowne\nRondebosch\nKuilsriver\nWynberg\nSea Point\nBishop Lavis\nCape Town Central\nTable Bay Harbour\nDelft\nMowbray\nRavensmead\nGoodwood\nElsies River\nPort of Entry\nPort of Entry\nKensington\nAthlone\nWoodstock\nPinelands\nBelhar\nManenberg\nClaremont\n: ")
des = input("\n\nEnter your end point\n  Bellville\nNyanga\n Bellville South\nPhilippi\nMatland\nParow\nLandsdowne\nRondebosch\nKuilsriver\nWynberg\nSea Point\nBishop Lavis\nCape Town Central\nTable Bay Harbour\nDelft\nMowbray\nRavensmead\nGoodwood\nElsies River\nPort of Entry\nPort of Entry\nKensington\nAthlone\nWoodstock\nPinelands\nBelhar\nManenberg\nClaremont\n: ")
print("Start: {} \n End: {}" .format(src, des))
c.send(bytes(src,"utf-8"))
c.send(bytes(des,"utf-8"))

#recieved the best path from the server
path = c.recv(1024).decode()
print(path)


# write the path in a file.
file1.writelines(path)
file1.close() #to change file access modes