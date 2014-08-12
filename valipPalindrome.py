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

    # this accepted too
    def isPalindrome2(self, s):
        if s == '': return True
        s = ''.join(s.lower().split())
        char = string.lowercase + '0123456789'
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] in char and s[end] in char: 
                if s[start] != s[end]: return False
                else:
                    start += 1
                    end -= 1
            if s[start] not in char: start += 1 
            if s[end] not in char: end -= 1
        return True
print Solution().isPalindrome('A    man, a plan, a canal: Panama') # True
print Solution().isPalindrome('race a car') # False
print Solution().isPalindrome('    ,,  ') # True
print Solution().isPalindrome('ab2a') # False