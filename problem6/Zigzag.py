def convert(s: str, numRows: int) -> str:
        string = list(s)
        numofrows = numRows
        if numofrows == 1 or len(string) == 1:
            return s
        numofcolumns = len(string) // 2
        if len(string) % (numofrows - 1) == 0 and numofrows != 2:
            pass
        else:
            numofcolumns += 1
        data = []
        strpos = 0
        for x in range(numofrows):
            data.append([])
        for x in range(numofrows):
            for y in range(numofcolumns):
                data[x].append(' ')
        finalstring = ''
        #print(data)
        y = 0
        while y < numofcolumns:
            for x in range(numofrows):
                if strpos <= len(string) - 1:
                    #print(strpos)
                    if y % (numofrows - 1) == 0:
                        #print('1Position: ', x, y)
                        #print(string[strpos])
                        data[x][y] = string[strpos]
                        strpos+=1
                        #print(x)
                    else:
                        #print('2Position: ', numofrows - (y % (numofrows - 1)) - 1, y)
                        #print(string[strpos])
                        data[numofrows - (y % (numofrows- 1)) - 1][y] = string[strpos]
                        strpos += 1
                        if numofrows - (y % (numofrows - 1)) - 1 == 1 and y % (numofrows - 1) != 0:
                            #print('breaking')
                            #print('----------------')
                            break
                        y+=1
                    #for x in range(numofrows):
                        #print(data[x])
                    #print('------------------')
            y+=1


        for x in range(numofrows):
            print(data[x])
        for x in range(numofrows):
            for y in range(numofcolumns):
                if data[x][y] != ' ':
                    finalstring+=data[x][y]
        return finalstring
convert('WILLISANUGLYBASTARDANDMACADENEEDSTOKILLHIMSELFIMMEDIATLYBECAUSENOONELIKESHIM', 3)
