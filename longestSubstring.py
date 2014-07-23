class Solution:
    # @return an integer
    def lengthOfLongestSubstring2(self, s):
        length = 0
        for i in range(0,len(s)):
            dictS = []
            while i < len(s) and s[i] not in dictS:
                dictS.append(s[i])
                i += 1
            length = max(length, len(dictS))
        return length
    def  lengthOfLongestSubstring(self, s):
        dictS = []
        length  = 0
        for i in range(0, len(s)):
            if dictS == []:
                dictS.append(s[i])
            else:
                # remove previous character
                dictS.pop(0)
            # start from the first character that is not in the dictS
            start = i + len(dictS)
            while start < len(s) and s[start] not in dictS:
                dictS.append(s[start])
                start += 1
            length = max(length, len(dictS))
        return length
print Solution().lengthOfLongestSubstring2('abcabcbb') #3
print Solution().lengthOfLongestSubstring2('bbbbb')    #1
print Solution().lengthOfLongestSubstring('abcabcbb')  #3
print Solution().lengthOfLongestSubstring('bbbbb')     #1
print Solution().lengthOfLongestSubstring2('wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco') #12
print Solution().lengthOfLongestSubstring('wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco')  #12