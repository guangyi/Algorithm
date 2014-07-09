'''Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
class Solution:
    # @return a list of lists of integers

    def combine(self, n, k):
        arr = []
        for i in range(1, n+1):
            arr.append(i)
        return self.combineHelp(arr, k) 
        
    def combineHelp(self,arr,num):
        if num == 1:
            newArr = []
            for item in arr:
                newArr.append([item])
            return newArr
        result = []
        for i in range(0, len(arr) - num + 1):
            select = arr[i]
            tempResult = self.combineHelp(arr[i + 1:], num - 1)
            for item in tempResult:
                item.append(select)
                result.append(item)
        return result
    
print Solution().combine(4, 3)