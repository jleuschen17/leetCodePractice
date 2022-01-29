def strStr(haystack, needle):
    haystack = list(haystack)
    needle = list(needle)
    if len(needle) == 0:
        return 0
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            matchCheckStack = haystack[i:len(needle) + i]
            if matchCheckStack == needle:
                return i
    return 0

haystack = ''
needle = ''
print(strStr(haystack, needle))