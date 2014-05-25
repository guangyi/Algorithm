'''
Created on May 24, 2014

Merge K sorted Array-- with Heap: (arr[i], (indexOfArray, elementIndexInArray))

@author: zhouguangyi2009
'''
import heapq
class Solution:
    # @param arr: a collection of k arr 
    def mergeKsortedArray(self, arr):
        k = len(arr)
        result = []
        heap = []
        for i in range(0, k):
            if arr[i] != []:
                heap.append((arr[i][0],(i, 0)))
        # transform list heap into a heap
        heapq.heapify(heap)
        
        while len(heap) != 0:
            min = heapq.heappop(heap)
            # data structure: (value, (arrIndex, elemIndex))
            arrTup = min[1]
            arrIndex = arrTup[0]
            elemIndex = arrTup[1]
            result.append(min[0])
            elemIndex += 1
            if elemIndex < len(arr[arrIndex]):
                heapq.heappush(heap, (arr[arrIndex][elemIndex],(arrIndex, elemIndex)))
        return result
arr = [
       [1,2,9],
       [0,2,3,4,],
       [5,6]
       ] 
arr2 = [[1,2,3]]
arr3 = [[],[2,3]]
print Solution().mergeKsortedArray(arr)
print Solution().mergeKsortedArray(arr2)
print Solution().mergeKsortedArray(arr3)