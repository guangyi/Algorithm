'''
Created on May 20, 2014

@author: zhouguangyi2009
'''
class Solution:
    def magicIndex(self, arr):
        i = 0
        result = []
        while i <= len(arr) - 1:
            if arr[i] - i == 0:
                result.append(i)
                i += 1
            elif arr[i] - i != 0:
                diff = arr[i] - i
                i = i + diff + 1
            else:
                i += 1 
        if len(result)  == 0:
            return False
        return result
print Solution().magicIndex([2,3,3,3])