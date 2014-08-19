class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive3(self, num):
        def findNext(item, flag):
            length = 0
            while item + flag in d:
                d[item + flag] = True
                item = item + flag
                length += 1
            return length
        
        maxLength = 1
        d = {}
        for item in num:
            d[item] = False
        for item in num:
            if not d[item]:
                left = findNext(item, -1)
                right = findNext(item, 1)
                if left + right + 1 > maxLength:
                    maxLength = left + right + 1 # plus this number
        return maxLength