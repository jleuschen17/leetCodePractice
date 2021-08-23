class Solution:
    def isValid(self, string):
        if len(string) % 2 != 0:
            return False
        strlist = list(string)
        strlist.append(' ')
        keydict = {'(': ')', '{': '}', '[': ']'}
        left = ['(', '{', '[']
        right = [')', '}', ']']
        def listLoop(strlist):
            placements = []
            length = 0
            checker = 0
            x = 0
            while True:
                try:
                    if strlist[x] in left:
                        #print('Entered on iteration:', x)
                        length += 1
                        placements.append(strlist[x])
                        checker = 1
                    elif strlist[x] in right:
                        #print('Entered on iteration:', x)
                        if checker == 0 or length == 0:
                            return False
                        placements.append(strlist[x])
                        length -= 1
                    if length == 0 and checker == 1:
                        #print('Entered on iteration:', x)
                        #print('Length of Placement List:', len(placements))
                        #print('Iteration Length:', len(placements) // 2)
                        iterations = len(placements) // 2
                        for y in range(iterations):
                            if keydict[placements[y]] != placements[-1 - y]:
                                print('FAIL')
                                return False
                        if (len(strlist) - 2) == x:
                            return True
                        newstrlist = strlist[x + 1:]
                        return listLoop(newstrlist)
                    x += 1
                except:
                    #print('ERROR')
                    return False
            return False
        return listLoop(strlist)
