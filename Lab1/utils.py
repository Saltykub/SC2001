import random

def insertion_sort (arr,l,r):
    keys = 0
    for i in range (l+1,r+1):
        for j in range(i,l,-1):
            keys+=1
            if(arr[j] < arr[j-1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return keys

def merge(arr,l,r):
    keys = 0
    mid = (l+r)//2
    i = l
    j = mid+1
    temp = []
    while(i <= mid and j <= r):
        keys+=1
        if(arr[i] < arr[j]):
            temp.append(arr[i])
            i+=1
        else: 
            temp.append(arr[j])
            j+=1
    while(i <= mid):
        temp.append(arr[i])
        i+=1
    while(j <= r):
        temp.append(arr[j])
        j+=1
    idx = 0
    for k in range(l,r+1):
        arr[k] = temp[idx]
        idx+=1
    return keys

def merge_sort(arr,l,r):
    if(l < r):
        keys = 0
        mid = (l+r) // 2
        keys += merge_sort(arr,l,mid)
        keys += merge_sort(arr,mid+1,r)
        keys += merge(arr,l,r)
        return keys
    else : return 0

def merge_sort_hybrid(arr,l,r,s):
    keys = 0
    if(r-l+1 <= s):
        keys += insertion_sort(arr,l,r)
    else:
        mid = (l+r) // 2
        keys+= merge_sort_hybrid(arr,l,mid,s)
        keys+= merge_sort_hybrid(arr,mid+1,r,s)
        keys+= merge(arr,l,r)
    return keys


def generate_sample(n):
    data = [random.randint(1, 10000000) for _ in range(n)]  
    return data


# def mergeSortwithComparisons(arr):
#     if len(arr) <= 1:
#         return arr,0

#     mid = len(arr) // 2
#     leftHalf = arr[:mid]
#     rightHalf = arr[mid:]
#     totalkeycomparisons = 0
#     sortedLeft,leftkeycomparisons = mergeSortwithComparisons(leftHalf)
#     sortedRight,rightkeycomparisons = mergeSortwithComparisons(rightHalf)
#     totalkeycomparisons = leftkeycomparisons+rightkeycomparisons
#     return mergeWithComparisons(sortedLeft, sortedRight,totalkeycomparisons)

# def mergeWithComparisons(left, right,totalkeycomparisons):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#         totalkeycomparisons+=1

#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result,totalkeycomparisons



