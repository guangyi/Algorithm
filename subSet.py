'''
Created on May 26, 2014

Get all subset of a distinct integer set

@author: zhouguangyi2009
'''

class Solution():
    def subsets(self, S):
        result = []
        maxNum = pow(2, len(S))
        S.sort()
        for integer in range(0, maxNum):
            arr = self.sub(S, integer)
            result.append(arr)
        return result
        
    def sub(self, S, i):
        index = len(S) - 1
        result = []
        while i > 0:
            if i & 1 == 1: result.insert(0, S[index])
            i = i >> 1
            index -= 1
        return result

print Solution().getAllSubset([])
print Solution().getAllSubset([2])       
print Solution().getAllSubset([4,1,0])

   