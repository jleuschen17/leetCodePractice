def searchInsert(nums, target, k=0):
    mid = len(nums) // 2
    k += mid
    if nums[mid] == target:
        k-=mid
        return mid + k
    elif len(nums) <= 1:
        return mid + k + 1
    elif nums[mid] > target:
        k-=mid
        return searchInsert(nums[:mid], target, k)
    else:
        return searchInsert(nums[mid:], target, k)

nums = [1, 2, 2, 4, 5, 6, 7, 8]
target = 3
print(searchInsert(nums, target))