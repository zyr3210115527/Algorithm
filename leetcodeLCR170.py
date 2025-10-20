def ans(object):
    nums=0
    for i in range(len(object)-1):
        for j in range(i+1,len(object)):
            if object[i]<object[j]:
                nums+=1
    return nums
print(ans([1,4,2,3]))