def intToRoman(num: int) -> str:
	modvalues = [1000, 500, 100, 50, 10, 5, 1]
	romnums = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
	numvalues = []
	for x in range(len(modvalues)):
		numvalues.append(num // modvalues[x])
		num = num % modvalues[x]
	final_num = ''
	print(numvalues)
	numvalues.append(0)
	for x in range(numvalues[0]):
		final_num+=romnums[0]
	for x in range(1, len(numvalues)):
		if numvalues[x] == 1 and numvalues[x+1] == 4:
			final_num+=romnums[x+1]
			final_num+=romnums[x-1]
			numvalues[x+1] = 0
		elif numvalues[x] == 4:
			final_num+=romnums[x]
			final_num+=romnums[x-1]
		else: 
			for y in range(numvalues[x]):
				final_num+=romnums[x]
	return(final_num)
print(intToRoman(69))
		
		
		
