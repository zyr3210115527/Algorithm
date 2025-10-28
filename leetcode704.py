def search(nums, target):
    left,right=0,len(nums)-1
    while left<=right:
        index = (left+right)//2
        if nums[index]==target:
            return index
        if nums[index]>target:
            right = index-1
        if nums[index] < target:
            left = index+1
    return -1
print(search([-1,0,3,5,9,12],2))
