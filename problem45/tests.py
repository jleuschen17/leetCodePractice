
nums = [4,1,1,3,1,1,1]
currJump = 0
nxtValue = 0
for i in range(1, nums[0] + 1):
    if (nums[i] + i - 1) > nxtValue:
        currJump = i
        nxtValue = nums[i] + i - 1
        print(nxtValue)
        print(nums[i] + i - 1)
        print('-------------------')
print(nxtValue)
