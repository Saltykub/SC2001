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


