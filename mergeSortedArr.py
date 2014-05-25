'''
Created on May 17, 2014

@author: zhouguangyi2009
'''
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i = m-1
        j = n-1
        k = m + n
        while i >= 0 and j >=0:
            if A[i] <= B[j]:
                A[k] = B[j]
                j -= 1
            else:
                A[k] = A[i]
                i -= 1
            k -= 1
        while j >= 0:
            A.insert(k,  B[j])
            k -= 1
            j -= 1
        return A
                
print Solution().merge([1,2,3,None], 3, [1], 1)
