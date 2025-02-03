f = open('SC2001/Lab1/inputs/input10000000.txt',"r") #change path string depending on root folder
data = f.readline()
data = data.split(",")
for i in range(0,len(data)):
    data[i] = int(data[i])
print(len(data))