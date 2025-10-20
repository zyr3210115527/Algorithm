def merge(nums1, m, nums2, n):
    i,j=0,0
    if m==0:
        nums1=nums2
        return nums1
    if n==0:
        return nums1
    for w in range(n+m):
        if nums1[w]==0 and nums1[w-1]!=0:
            nums1[w]=9999999
    while j<n:
        if nums1[i]<=nums2[j]:
            i+=1
        if nums1[i]>nums2[j]:
            nums1.insert(i,nums2[j])
            j+=1

    for x in range(n):
        nums1.pop()

    return nums1
print(merge([1,2,3,0,0,0],3,[1,3,5],3))
