class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0: return False
        # 1 get the range of x (<10 or <100 or <1000...)
        startN = 0
        temp = x
        while temp / 10 > 0:
            startN = startN + 1
            temp = temp / 10
        if startN == 0: return True # only one digit like 3 or 6
        while x > 0:
            firstDigit = x / pow(10, startN)
            lastDigit = x % 10
            if firstDigit != lastDigit: return False
            else: 
                nextX = x % pow(10, startN)
                x = (nextX - lastDigit) / 10
                startN -= 2
        return True
print Solution().isPalindrome(9999)