import random

n = 1000000 # magnitude of samples
for i in range(1,11): 
    f = open(f"input{str(i*n)}.txt","a")
    data = random.sample(range(1,10000000+1),i*n) # range of values from 1 to maximum allowed size of datasets
    for i in range(0,len(data)):
        if (i != len(data)-1):
            f.write(str(data[i]) + ",")
        else:
            f.write(str(data[i]))
f.close()

