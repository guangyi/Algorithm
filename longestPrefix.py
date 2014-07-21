class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ''
        prefix = strs[0]
        for i in range(1, len(strs)):
            if prefix == '': return ''
            prefix = self.findCommon(prefix, strs[i])
        return prefix
            
    def findCommon(self, str1, str2):
        result = ''
        for i in range(0, min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                result = result + str1[i]
            else: return result
        return result
print Solution().longestCommonPrefix(['a','a','b']) #''
print Solution().longestCommonPrefix(['a','a','ab']) #a
print Solution().longestCommonPrefix(['acde','acd','acdf']) #acd