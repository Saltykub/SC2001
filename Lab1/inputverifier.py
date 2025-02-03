f = open("/SC2001/Lab1/inputs/input1000000.txt","r")
data = f.readline()
data = data.split(",")
for i in range(0,len(data)):
    data[i] = int(data[i])
print(len(data))