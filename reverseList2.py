class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if head == None: return
        if m == n: return head
        index = 1
        temp = head
        oldStart = None
        while temp != None:
            if index == m - 1: 
                oldStart = temp
            if index == n:
                newStart = temp
                oldEnd = temp.next
                break
            index += 1
            temp = temp.next
        
        newEnd = oldStart.next if oldStart else head
        self.reverse(newEnd, m, n)
        if oldStart: oldStart.next = newStart
        else: head = newStart
        newEnd.next = oldEnd   
        return head  
    def reverse(self, head, m, n):
        if m == n: return head
        prev = self.reverse(head.next, m + 1, n)
        prev.next = head
        head.next = None
        return head
    
    # reverse list using two pointers instead of recursion.
    def reverseBetween2(self, head, m, n):
        if head == None or head.next == None or m == n: return head
        sentinelNode = ListNode(0)
        sentinelNode.next = head
        temp = sentinelNode
        index = 1
        while index <= n:
            if index == m:
                leadingListTail = temp
            temp = temp.next
            index += 1
        reverseListHead = leadingListTail.next
        reverseListTail = temp
        trailingListHead = reverseListTail.next
        reversedListHead = self.reverse2(reverseListHead, reverseListTail)
        leadingListTail.next = reversedListHead
        # reverseLiseHead now is reversed-List's tail.
        reverseListHead.next = trailingListHead
        return sentinelNode.next
    
    def reverse2(self, head, tail):
        end = tail.next
        reversedHead = None
        curr = head
        while curr != end:
            temp = curr.next
            curr.next = reversedHead
            reversedHead = curr
            curr = temp
        return reversedHead

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
head = Solution().reverseBetween2(node1,2, 5) 
while head != None:
    print head.val
    head = head.next