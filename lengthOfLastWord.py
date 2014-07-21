class Solution:
    # @param s, a string
    # @return an integer
    # tricky part is 'a b s    ' a string with multiple space at last
    # so need to skip those spaces
    def lengthOfLastWord(self, s):
        strArr = s.split(' ')
        for i in range(len(strArr) - 1 ,-1 ,  -1):
            if strArr[i] != '': return len(strArr[i])
        return 0