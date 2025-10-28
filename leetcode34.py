def searchRange(nums, target):
    res=[]
    l,r=0,len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            s,t=mid,mid
            while s<len(nums):
                if nums[s]==target:
                    s+=1
                else:
                    break
            while t>=0:
                if nums[t]==target:
                    t-=1
                else:
                    break
            return(t+1,s-1)
        elif nums[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return (-1,-1)
print(searchRange([1,2,3,4,5,6],9))
