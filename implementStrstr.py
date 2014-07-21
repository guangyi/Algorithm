class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        hayIndex = ndlIndex = 0
        if needle == '': return haystack
        while hayIndex < len(haystack):
            if haystack[hayIndex] != needle[ndlIndex]:
                hayIndex = hayIndex - ndlIndex + 1
                ndlIndex = 0
            else:
                ndlIndex += 1
                hayIndex += 1
                if ndlIndex >= len(needle):
                    return haystack[hayIndex - len(needle):]
        return None