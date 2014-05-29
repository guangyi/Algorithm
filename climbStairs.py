'''
Created on May 19, 2014

@author: zhouguangyi2009
'''
class Solution:
    # @param n, an integer
    # @return an integer
    ''' no memorization not effitiency
    def climbStairs(self, n):
        if n < 0 :
            return 0
        if n == 0:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    '''
    def __init__(self):
        # becuase need to return arr[n]
        # n couldn't be 0, so arr starts from 0
        self.arr = [0, 1, 2]
    
    def climbStairs(self, n):
        if n < 0 :
            return 0
        if n == 0:
            return 1
        if n < len(self.arr):
            return self.arr[n]
        else:
            self.arr.append( self.climbStairs(n - 1) + self.climbStairs(n - 2) )
            return self.arr[n]
            