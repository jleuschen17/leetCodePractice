def longestPalindrome(s: str) -> str:
	string = list(s)
	if len(string) == 1:
		return s
	palindromes = []
	for x in range(len(string)):
		for y in range(len(string) + 1):
			newstring = string[x:y]
			if newstring == newstring[::-1]:
				palindromes.append(string[x:y])
	final_palindrome = []
	for palindrome in palindromes:
		if len(palindrome) > len(final_palindrome):
			final_palindrome = palindrome
	answer = ''
	for character in final_palindrome:
		answer += character
	return answer

print(longestPalindrome('cwziydanrqvsdtvnnqgjnbrvvwxwqojeqgxhwxdoktjktulemwpbeqscbbtbfvkxsrjetfdrovcrdwzfmnnihtgxybuairswfewvpuscocqifuwylhssldpjrawqdrbvkykpaggspbfrulcktpbofchzikhzxhpocgvdbwpewpywsgqbczmamprklaoovcfecwchhmsaqkhvuvvzjblmgvqpqtnlipgqsanvovylpmxlmxvymppdykphhaamtxjnnlsqfwjwhyywgurteaummwhvavxbcpgrfffxrowluqmqjaugryxdmwvyokdcfcvcytxpixbvwrdgzctejdoaavgtezexmvxgrkpnayvfarkyoruofqmpnsqdzojxqrjsnfwsbzjmaoigytygukqlrcqaxazvmytgfghdczvzphfdbnxtklaiqqsotavdmhiaermluafheowcobjqmrkmlzyasuhihghgkghjkhgjkkghjkghjghjkghkjghjkkghjkjghgkhjjkghkghjaaabbbaaaghjgyuuygyguytuiyitdr6df46r87dfv6r7f6yfdrte5detrdctghvvghvgvfcxctyfrtdcxefghhjklkjhhgfgjvgfjgjfuyfiuyitugvhjjvggjfhfgjh'))
