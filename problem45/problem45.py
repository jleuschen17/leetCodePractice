def jump(nums):
    if len(nums) <= 2:
        if len(nums) <= 1:
            return 0
        return 1

    def jumpRecur(nums, jumps):
        print(jumps, nums)
        if len(nums) == 1:
            return jumps
        if len(nums) == 2 or nums[0] >= len(nums) - 1:
            return jumps + 1
        nxtValue = 0
        for i in range(1, nums[0] + 1):
            if nums[i] + i - 1 > nxtValue:
                currJump = i
                nxtValue = nums[i]
        for i in range(currJump):
            nums.pop(0)
        jumps += 1
        return jumpRecur(nums, jumps)

    return jumpRecur(nums, 0)


nums = [4,1,1,3,1,1,1]
print(jump(nums))
