class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def swap(self, arr, front, temp):
        arrTemp = arr[front]
        arr[front] = arr[temp]
        arr[temp] = arrTemp
    
    def sortColors(self, A):
        index0 = front = 0
        index1 =  len(A) - 1
        while front < index1:
            if A[front] == 1:
                index0 = front + 1 if index0 == 0 else index0
                while index0 <len(A) and A[index0] != 0:
                    index0 += 1
                if index0 < len(A): 
                    self.swap(A, front, index0)
                    index0 += 1
                front += 1
            elif A[front] == 2:
                while index1 > front and A[index1] == 2:
                    index1 -= 1
                if index1 > front:
                    self.swap(A, front, index1)
                    index1 -= 1
            else: front += 1
        return A
'''
[0, 1, 2]
[0, 0]
[0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2]
'''