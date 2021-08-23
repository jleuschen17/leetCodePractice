class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = list(s)
        total = 1
        totals = [1]
        if len(string) == 0:
            return 0
        past_values = [string[0]]
        past_values_dict = {string[0]: 0}
        x = 1
        while x < len(string):
            if string[x] not in past_values:
                past_values.append(string[x])
                past_values_dict[string[x]] = x
                total += 1
                x += 1
            else:
                totals.append(total)
                past_values = []
                total = 0
                x = past_values_dict[string[x]] + 1
        totals.append(total)
        answer = max(totals)
        return answer

