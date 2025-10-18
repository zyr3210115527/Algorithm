def sortColors(nums):
    n=len(nums)
    i=0
    w=0
    while i<n-w:
        if nums[i]==0:
            nums.pop(i)
            nums.insert(0,0)
        if nums[i]==2:
            nums.pop(i)
            nums.append(2)
            i-=1
            w+=1
        i+=1
    return nums

print(sortColors([0,1,2,0,1,1,2,2,0,0,2]))
