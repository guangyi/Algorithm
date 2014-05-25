'''
Created on May 24, 2014

Merge K Sorted List--heap ( (node.val, node) )

@author: zhouguangyi2009
'''
import heapq
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node:
                heap.append((node.val, node))
        
        #transform list heap into heap
        heapq.heapify(heap)
        if heap:
            head = ListNode(0)
            curr = head
        else:
            return None
        while heap:
            small = heapq.heappop(heap)
            curr.next = small[1]
            curr = curr.next
            if small[1].next:
                heapq.heappush(heap, (small[1].next.val, small[1].next))
        return head.next
