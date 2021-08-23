class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        brokenstrs = []
        for x in range(len(strs)):
            brokenstrs.append(list(strs[x]))
        i = 0
        finalword = ''
        while True:
            try:
                checker = 0
                letter = brokenstrs[0][i]
                #print('Letter: ', letter)
                for x in range(len(brokenstrs)):
                    if brokenstrs[x][i] == letter:
                        #print('Comparison letter', x, ':', brokenstrs[x][i])
                        pass
                    else:
                        #print('Letters Dont match')
                        checker = 1
                        break
                if checker == 0:
                    #print('Adding', letter, 'to', finalword)
                    finalword += letter
                else:
                    break
                i += 1
            except:
                break
        return finalword
