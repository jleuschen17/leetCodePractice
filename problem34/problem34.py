import numpy as np

def searchRange(nums, target, k=0):
    mid = len(nums) // 2
    k += mid
    if len(nums) == 0:
        return [-1, -1]
    if nums[mid] == target:
        print(k)
        def findlow(nums, target, mid):
            try:
                if nums[mid - 1] == target and mid - 1 >= 0:
                    return findlow(nums, target, mid - 1)
                else:
                    return mid
            except:
                return mid + 1
        def findhigh(nums, target, mid):
            try:
                if nums[mid + 1] == target:
                    return findhigh(nums, target, mid + 1)
                else:
                    return mid
            except:
                return mid
        solution = [findlow(nums, target, mid) + k - mid, findhigh(nums, target, mid) + k - mid]
        return solution
    elif len(nums) <= 1:
        return [-1, -1]
    elif nums[mid] > target:
        k-=mid
        return searchRange(nums[:mid], target, k)
    else:
        return searchRange(nums[mid:], target, k)

nums = [1]
target = 1
print(searchRange(nums, target))