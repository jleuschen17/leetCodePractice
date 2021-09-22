
def removeDuplicates(nums):
    dupcount = 0
    x = 0
    while True:
        if x >= len(nums):
            break
        if nums[x] == nums[x-1]:
            dupcount+=1
        else:
            if dupcount > 0:
                nums[x-dupcount] = nums[x]
        x+=1
    return len(nums) - dupcount


print(removeDuplicates([1,2,3,3,3,4,5,5]))

