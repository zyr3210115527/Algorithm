def heapy(arr,a,b):
    max=b
    left=b*2+1
    right=b*2+2
    if left<a and arr[left]>arr[b]:
        max=left
    if right<a and arr[right]>arr[max]:
        max=right
    if max!=b:
        arr[max],arr[b]=arr[b],arr[max]
        #这里要把右边的和目前已知最大进行比较
        heapy(arr,a,max)

def heapsort(nums):
    n=len(nums)
    for i in range(n//2-1,-1,-1):
        #n//2-1是二叉树有叉子的最大的数
        heapy(nums,n,i)
    for i in range(n-1,0,-1):
        nums[i],nums[0]=nums[0],nums[i]
        heapy(nums,i,0)
        #调整二叉树大小，最大的剔除了已经归位的数
    return nums

print(heapsort([1,4,2,5,3]))
