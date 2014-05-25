'''
Created on May 20, 2014

@author: zhouguangyi2009
'''
#Assumption no repeat elements
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        return self.searchHalf(A, 0, len(A)-1, target)
        
    def searchHalf(self, A, start, end, target):
        if start > end:
            return -1
        mid = int ((start + end)/ 2)
        midVal = A[mid] 
        startVal = A[start] 
        endVal = A[end]
        if midVal == target:
            return mid
        # left half is ordered
        if midVal >= startVal:
            if target <= midVal and target >= startVal:
                # target is in left half
                return self.searchHalf(A, start, mid-1, target)
            else:
                return self.searchHalf(A, mid+1, end, target)
                # target is in right half
        # right half is ordered
        elif midVal < startVal:
            # target in right half:
            if target >= midVal and target <= endVal:
                return self.searchHalf(A, mid+1, end, target)
            # target in left half:
            else:
                return self.searchHalf(A, start, mid-1, target)
        return -1
print Solution().search([1,3], 3)