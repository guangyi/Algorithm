'''
Created on May 19, 2014

@author: zhouguangyi2009
'''
class Solution:
    # @return an integer
    def __init__(self):
        self.result = 0
        self.aux = [0]
        self.aux.append(0)
    def numTrees(self, n):
        return self.recer(1, n+1)
            
    def recer(self, start, end):
        result = 0
        if start >= end:
            return 1
        elif (end - start) == 1:
            return 1
        for i in range(start, end):   
#            smaller = self.recer(start, i)
#            larger = self.recer(i+1, end)
#            result = result + smaller * larger
            if (i-start) < len(self.aux):
                result = result + self.aux[i-start]
                #print end, start, "short", result
            else:
                smaller = self.recer(start, i)
                if (i-start) > 0:
                    print i-start, "insert", smaller,
                    self.aux[i-start] = smaller
                larger = self.recer(i+1, end)
                result = result + smaller * larger
        return result
print Solution().numTrees(3)