class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        strdigits = str(digits)
        lstdigits = list(strdigits)
        finaldigits = []
        for x in range(len(lstdigits)):
            finaldigits.append(int(lstdigits[x]))
        combos = []
        if len(finaldigits) > 0:
                for i in range(len(mappings[finaldigits[0]])):
                    try:
                        if len(finaldigits) > 1:
                            for j in range(len(mappings[finaldigits[1]])):
                                try:
                                    if len(finaldigits) > 2:
                                        for k in range(len(mappings[finaldigits[2]])):
                                            try:
                                                if len(finaldigits) > 3:
                                                    for l in range(len(mappings[finaldigits[3]])):
                                                        try:
                                                            combos.append(mappings[finaldigits[0]][i] +
                                                                          mappings[finaldigits[1]][j] +
                                                                          mappings[finaldigits[2]][k] +
                                                                          mappings[finaldigits[3]][l])
                                                        except IndexError:
                                                            break
                                                else:
                                                    combos.append(mappings[finaldigits[0]][i] +
                                                                  mappings[finaldigits[1]][j] +
                                                                  mappings[finaldigits[2]][k])
                                            except:
                                                break
                                    else:
                                        combos.append(mappings[finaldigits[0]][i] +
                                                      mappings[finaldigits[1]][j])
                                except:
                                    break
                        else:
                            combos.append(mappings[finaldigits[0]][i])
                    except:
                        break

        else:
            return []
        return combos
