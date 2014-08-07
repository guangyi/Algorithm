class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverse(self, head, newHead):
        if head == newHead: return head
        start = self.reverse(head.next, newHead)
        start.next = head
        head.next = None
        return head
    def reverseKGroup(self, head, k):
        if k == 1: return head
        if head == None: return 
        newHead = head
        for index in range(1, k):
            if newHead.next == None: return head
            newHead = newHead.next
        nextEnd = newHead.next
        newEnd = self.reverse(head, newHead)
        newEnd.next = self.reverseKGroup(nextEnd, k)
        return newHead