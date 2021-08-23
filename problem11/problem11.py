def maxArea(height):
	total = 0
	for x in height: 
		total += x 
	average = total / len(height)
	index = 0
	firstheight = 0
	if height[0] > height[-1]:
		heightbound = height[-1]
		nheightbound = height[0]
	else:
		heightbound = height[0]
		nheightbound = height[-1]
	for x in range(len(height) - 1):
		#print('x: ', x)
		if height[x] >= average: 
			firstheight = height[x]
			index = x
			break
	if firstheight == 0:
		for x in range(len(height) - 1):
			if height[x] > firstheight:
				firstheight = height[x]
				index = 0
	lastheight = 0
	lindex = 0
	#print('Index: ', index)
	y = len(height) - 1
	while y > index:
		if height[y] >= average:
			lastheight = height[y]
			lindex = y
			break
		y-=1
	z = len(height) - 1
	if lastheight == 0:
		while z > index:
			if height[z] > lastheight:
				lastheight = height[z]
				lindex = z
			z-=1
	#print('First Height: ', firstheight)
	#print('Last Height: ', lastheight)
	#print(lindex - index)
	area = 0
	if (lindex - index == 1):
		if firstheight > lastheight:
			area = lastheight
		else: 
			area = firstheight
	elif firstheight >= lastheight:
		area = lastheight * (lindex - index)
	else:
		area = firstheight * (lindex - index)
	if len(height) <= 2:
		return heightbound
	if area < (heightbound * (len(height) - 1)):
		area = (heightbound) * ((len(height) - 1))
	return area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
			
			
	
