class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head == None or head.next == None: return head
        prev = head
        curr = head.next
        while curr != None:
            if curr.val >= prev.val: # current node is bigger
                curr = curr.next
                prev = prev.next
            elif curr.val < head.val: # current node is smaller than head
                prev.next = curr.next
                curr.next = head
                head = curr
                curr = prev.next
            else:
                prev.next = curr.next
                temp = head
                while curr.val > temp.next.val:
                    temp = temp.next
                temp2 = temp.next
                temp.next = curr
                curr.next = temp2
                curr = prev.next
        return head