import numpy as np
def firstMissingPositive(nums):
    nums.sort()
    i=0
    while True:
        if i == len(nums):
            break
        if nums[i] <= 0:
            nums.pop(0)
        else:
            i += 1
    i=0
    while True:
        try:
            if nums[i] != i + 1:
                return i + 1
            i+=1
        except:
            return i+1


nums = np.linspace(1, 2**31 - 1, 2**31 - 1)
print(firstMissingPositive(nums))
