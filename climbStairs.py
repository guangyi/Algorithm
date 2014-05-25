'''
Created on May 19, 2014

@author: zhouguangyi2009
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def __init__(self):
        self.result = 0
        self.arr = [0,1,2]
    def climbStairs3(self, n):
        dp = [0, 1, 2]
        i = 3
        while i <= n:
            dp.append(dp[i-1] + dp[i-2] + dp[i - 3])
            i += 1
        return dp[n] 
    def climbStairs2(self, n, arr):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            if n < len(arr):
                return arr[n]
            else:
                val = self.climbStairs2(n - 2, arr) + self.climbStairs2(n - 1, arr)
                print arr
                arr.append(val)
                return arr[n]
    def climbStairs4(self, n):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            if n < len(self.arr):
                return self.arr[n]
            else:
                val =self.climbStairs4(n - 3) + self.climbStairs4(n - 2) + self.climbStairs4(n - 1)
                self.arr.append(val)
                return self.arr[n]
    def climbStairs(self, n):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            return self.climbStairs(n - 1) + self.climbStairs (n - 2)
    
arr= [0,1,2]
#print Solution().climbStairs2(35, arr)
print Solution().climbStairs4(35)
#print Solution().climbStairs3(3)