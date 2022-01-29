def maxSubArray(nums):
    max = 0
    curr = 0
    for i in range(len(nums)):
        curr += nums[i]
        if (curr) > max:
            max = curr
    return max

nums = [-2,1,-3,4,-1,2,1,-5,4]


