class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = ''.join(s.split()).lower()
        startIndex = 0
        endIndex = len(s) - 1
        while startIndex < endIndex:
            if re.match('^[0-9a-z]$', s[startIndex]) and re.match('^[0-9a-z]$',s[endIndex]):
                if s[startIndex] != s[endIndex]:return False
                startIndex += 1
                endIndex -= 1
            if not re.match('^[0-9a-z]$', s[startIndex]): startIndex += 1
            if not re.match('^[0-9a-z]$',s[endIndex]): endIndex -= 1
        return True
print Solution().isPalindrome('A    man, a plan, a canal: Panama') # True
print Solution().isPalindrome('race a car') # False
print Solution().isPalindrome('    ,,  ') # True
print Solution().isPalindrome('ab2a') # False