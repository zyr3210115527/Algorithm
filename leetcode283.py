def moveZeroes(nums):
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(0)
    return nums
print(moveZeroes([0,1,0,1,0,1,0,1]))