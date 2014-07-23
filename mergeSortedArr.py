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
        if m == 0: 
            for item in B:
                A.append(item)
        indexAB = m + n - 1
        indexA = m - 1
        indexB = n - 1
        for indexAB in range(m + n - 1, -1, -1):
            if indexB < 0: 
                A[indexAB] = A[indexA]
                indexA -= 1
            elif indexA < 0: 
                A[indexAB] = B[indexB]
                indexB -= 1
            else:
                if A[indexA] >= B[indexB]:
                    A[indexAB] = A[indexA]
                    indexA -= 1
                else:
                    A[indexAB] = B[indexB]
                    indexB -= 1
            indexAB -= 1
A = [1,2,3, None]        
Solution().merge(A , 3, [1], 1)
print A

B = []
Solution().merge(B , 0, [1], 1)
print B