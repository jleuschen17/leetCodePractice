
def removeElement(nums, val):
    k=len(nums)
    orlen = len(nums)
    i=0
    while True:
        if nums[i] == val:
            nums.pop(i)
            k-=1
            i-=1
        i+=1
        if i == len(nums):
            break
    for i in range(orlen - len(nums)):
        nums.append('_')
    return nums, k






nums = [1, 2, 3, 3, 4, 5, 6, 7, 8, 8]
print(removeElement(nums, 3))










