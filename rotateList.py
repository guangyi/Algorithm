class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head == None: return head
        last = head
        end = head
        for i in range(0, k):
            if end.next != None:end = end.next
            # k can larger than the length of node
            # just return to head and do it again
            else: end = head 
        if end == last: # end and last is the same, no need to return
            return head
        while end.next != None:
            last = last.next
            end = end.next
        end.next = head
        head = last.next
        last.next = None
        return head