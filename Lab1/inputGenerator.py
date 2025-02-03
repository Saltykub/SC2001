import random

n = 1000000 # number of samples
for i in range(1,4):
    f = open(f"input{str(i*n)}.txt","a")
    data = random.sample(range(1,i*(n+1)),i*n)
    for i in range(0,len(data)):
        if (i != len(data)-1):
            f.write(str(data[i]) + ",")
        else:
            f.write(str(data[i]))
f.close()

