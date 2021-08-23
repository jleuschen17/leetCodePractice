def problem15(nums):
	triplets = []
	arr = ['i', 'j', 'k']
	for i in range(len(nums)):
		for j in range(len(nums)):
			for k in range(len(nums)):
				if i != j and i != k and j != k and (nums[i] + nums[j] + nums[k]) == 0:
					solutions = []
					checker = 0
					for x in range(len(arr)):
						for y in range(len(arr)):
							for z in range(len(arr)):
								if x != y and x != z and y != z:
									solutions.append([nums[x], nums[y], nums[z]])
					for solution in solutions:
						if solution in triplets:
							checker = 1
					if checker == 0:
						triplets.append([nums[i], nums[j], nums[k]])
	return triplets

nums = [-1, 0, -1, 1, 2, -4]
print(problem15(nums))
					
