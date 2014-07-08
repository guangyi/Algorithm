'''
Created on May 29, 2014

@author: zhouguangyi2009
'''
class Solution:
    # @return an integer
    def reverse(self, x):
        flag = False
        result = 0
        if x < 0:
            flag = True
        x = abs(x)
        while x != 0:
            digit = x % 10
            result = result * 10 + digit
            x = int(x / 10)
        if flag:
            return -result
        return result