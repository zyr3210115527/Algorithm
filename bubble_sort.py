def bubble_sort(arr):
    n=len(arr)
    state=True
    while state:
        i=0
        state = False
        while i<n-1:
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                state=True
            i+=1
    return arr

print(bubble_sort([1,2,3,4,51,6,7,10,8,9]))