class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def __init__(self):
        self.result = []
   
    def searchRange(self, A, target):
        self.search(A, 0, len(A) - 1, target)
        if not self.result: self.result = [-1, -1]
        return self.result
    def search(self, A, start, end, target):
        if end < start: return
        #print start, end
        mid = start + (end - start) / 2
        if A[mid] < target:
            self.search(A, mid + 1, end, target)
        elif A[mid] > target:
            self.search(A, start, mid - 1, target)
        else: #A[mid] == target
            small = mid - 1
            big = mid + 1
            if small < 0: self.result.insert(0, mid)
            else:
                if A[small] == target:
                    self.search(A, start, mid - 1, target)
                else: # A[small] != target:
                    self.result.insert(0, mid)
            if big >= len(A): self.result.append(mid) 
            else:
                if A[big]  == target:
                    self.search(A, mid + 1, end, target)
                else: self.result.append(mid)
        return
print Solution().searchRange([2,3,7,7,8,8,8,9], 6)
print Solution().searchRange([3,7,7,8,8,8,9,10], 8)
print Solution().searchRange([3,7,7,8,8,8,8], 8)
print Solution().searchRange([3,3,7,7,8,8,8,9], 3)
'''
[-1, -1]
[3, 5]
[3, 6]
[0, 1]
'''