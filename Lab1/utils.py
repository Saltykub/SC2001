def insertion_sort (arr,l,r):
    for i in range (l,r+1):
        for j in range(i,l,-1):
            if(arr[j] < arr[j-1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]

def merge(arr,l,r):
    mid = (l+r)//2
    i = l
    j = mid+1
    temp = []
    while(i <= mid and j <= r):
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

def mergeSortwithComparisons(arr):
    if len(arr) <= 1:
        return arr,0

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]
    totalkeycomparisons = 0
    sortedLeft,leftkeycomparisons = mergeSortwithComparisons(leftHalf)
    sortedRight,rightkeycomparisons = mergeSortwithComparisons(rightHalf)
    totalkeycomparisons = leftkeycomparisons+rightkeycomparisons
    return mergeWithComparisons(sortedLeft, sortedRight,totalkeycomparisons)

def mergeWithComparisons(left, right,totalkeycomparisons):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        totalkeycomparisons+=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result,totalkeycomparisons

def merge_sort(arr,l,r):
    if(l < r):
        mid = (l+r) // 2
        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1,r)
        merge(arr,l,r)

def merge_sort_hybrid(arr,l,r,s):
    if(r-l+1 <= s):
        insertion_sort(arr,l,r)
    else:
        mid = (l+r) // 2
        merge_sort_hybrid(arr,l,mid,s)
        merge_sort_hybrid(arr,mid+1,r,s)
        merge(arr,l,r)


