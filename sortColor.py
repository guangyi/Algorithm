class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def swap(self, arr, front, temp):
        arrTemp = arr[front]
        arr[front] = arr[temp]
        arr[temp] = arrTemp
    
    def sortColor2(self, A):
        start = 0
        end = len(A) - 1
        while start < end:
            if A[start] == 1:
                temp = start + 1
                while temp < len(A) and A[temp] != 0: # verify temp < length A first!!!
                    temp += 1
                if temp < len(A): self.swap(A, start, temp)
                start += 1
            elif A[start] == 2:
                while end > start and A[end] == 2:
                    end -= 1
                if end > start: self.swap(A, start, end)
            else: start += 1
'''
[0, 1, 2]
[0, 0]
[0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2]
'''