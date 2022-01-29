def groupAnagrams(strs):
    pastLetters = []
    anaGrams = {}
    for i in range(len(strs)):
        currStr = list(strs[i])
        currStr.sort()
        currStr = tuple(currStr)
        if currStr not in pastLetters:
            anaGrams[currStr] = []
            pastLetters.append(currStr)
        anaGrams[currStr].append(strs[i])
    finalAnagrams = []
    for letter in pastLetters:
        finalAnagrams.append(anaGrams[letter])
    return finalAnagrams

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))