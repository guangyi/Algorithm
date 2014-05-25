'''
Created on Apr 15, 2014

@author: zhouguangyi2009
'''

class Solution():
    
    def magnitude(self, arr):
        length = len(arr)
        result = []
        if length == 0:
            return -1
        else:
            for i in range(0, length):
                left = True
                right = True
                for j in range(0, i):
                    #j is all the element on the left side of a[i]
                    #if all a[j] < a[i] then satisfy 50% of the requirements
                    if arr[j] > arr[i]:
                        left = False
                for k in range(i+1, length):#a[k] are all the elements on the right side of a[i]
                    #if a[j] > a[i] satisfy 50% of the requirement
                    if arr[k] < arr[i]:
                        right = False
                if (left and right):# if left and right both are True, then find an index that satisfy all requirements
                    result.append(i)
            if result != None:
                return result
            else: return -1
re = Solution().magnitude([4444,4444,4444])
print re