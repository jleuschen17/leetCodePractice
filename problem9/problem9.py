class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        i = 0
        digits = 0
        nx = x
        if x < 0:
            nx = -x
        while True:
            if nx % pow(10, i) == nx:
                digits = i
                break
            else:
                i+=1
        finalnum = 0
        for i in range(digits):
            digit = nx % 10
            nx = nx // 10
            finalnum += (digit * pow(10, digits - i - 1))
        if finalnum > 2147483647 or finalnum < -2147483648:
            return 0
        if x == finalnum:
            return True
        return False
