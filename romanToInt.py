class Solution:
    # @return an integer
    def romanToInt2(self, s):
        dictR = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1  }
        Sum = 0
        i = 0
        while i < len(s):
            if s[i:i + 2] in dictR:
                Sum = Sum + dictR[s[i:i+2]]
                i += 2
            else:
                Sum = Sum +dictR[s[i]]
                i += 1
        return Sum
   
    def romanToInt(self, s):
        dictR = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1  }
        if len(s) == 1: return dictR[s]
        i = 0 
        j = 1
        result = 0
        while j < len(s):
            if s[i] + s[j] in dictR:
                result = result + dictR[s[i] + s[j]]
                i += 2
                j += 2
            else:
                result = result + dictR[s[i]]
                i += 1
                j += 1
        if i < len(s): result = result + dictR[s[i]]
        return result
        
print Solution().romanToInt('MCMXCVI')
print Solution().romanToInt('DCXXI')
print Solution().romanToInt('MMCCCXCIX')

print Solution().romanToInt2('MCMXCVI')
print Solution().romanToInt2('DCXXI')
print Solution().romanToInt2('MMCCCXCIX')