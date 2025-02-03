from utils import *
from time import process_time

# sample_data = [5,4,3,2,1]
# parameter for merge_sort is array, start index, stop index, step for using insertion sort 
# merge_sort_hybrid(sample_data,0,4,1)
#print(sample_data)
f = open('Lab1/inputs/input1000.txt',"r") #change path string depending on root folder
data = f.readline()
data = data.split(",")
for i in range(0,len(data)):
    data[i] = int(data[i])

# Start the stopwatch / counter 
t1_start = process_time() 

data,keycomparisons = mergeSortwithComparisons(data)
# Stop the stopwatch / counter
t1_stop = process_time()

# key comps with Nathan's function: 220099687
# key comps with Chong Wei's function: 220102334

print(f"Key Comparisons:{keycomparisons}")
print("Elapsed time during the whole program in seconds:",
                                         t1_stop-t1_start) 



