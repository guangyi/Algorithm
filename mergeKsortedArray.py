'''
Created on May 24, 2014

Merge K sorted Array-- with Heap: (arr[i], (arr, i))

@author: zhouguangyi2009
'''
import heapq
class Solution:
    # @param arr: a collection of k arr 
    def mergeKsortedArray(self, arr):
        k = len(arr)
        heap = []
        for i in range(0, k):
            heap.append((arr[i][0],(arr[i])))
        # transform list heap into a heap
        heapq.heapify(heap)
            