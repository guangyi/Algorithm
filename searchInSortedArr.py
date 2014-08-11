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
        if start > end: return -1 # if there is only one node  or empty A, return -1 immediately
        mid = start + (end - start) / 2
        if A[mid] == target: return mid
        if A[mid] <= A[end]: # right half is ordered
            if A[mid] < target and target <= A[end]: # target is in right half
                return self.searchHalf(A, mid + 1, end, target)
            else: return self.searchHalf(A, start, mid - 1, target) # target is in left half
        
        elif A[mid] >= A[start]: # left half is ordered
            if A[start] <= target and target < A[mid]:# target in left half:
                return self.searchHalf(A, start, mid - 1, target)
            else: return self.searchHalf(A, mid + 1, end, target) # target in right half:
        return -1
print Solution().search([1,3], 3)