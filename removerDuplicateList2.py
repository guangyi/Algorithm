 class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        values = []
        nodes = []
        if head == None: return None
        while head != None:
            if head.val in values:
                i = values.index(head.val)
                nodes[i] = False 
            else: 
                values.append(head.val)
                nodes.append(head)
            head = head.next
        nodes = [value for value in nodes if value != False]
        if nodes:
            for i in range(0, len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
            nodes[-1].next = None
            head = nodes[0]
        else: head = None
        return head
    
    def deleteDuplicates2(self, head):
        if head == None: return None
        prev = head
        curr = head.next
        head = None if curr else head
        duplicates = False
        while curr != None:
            if prev.val == curr.val:
                prev = prev.next
                curr = curr.next
                duplicates = True
            else:
                if curr.next and curr.next.val == curr.val:
                    while curr.next and curr.next.val == curr.val:
                        curr = curr.next
                    curr = curr.next
                    prev.next = curr
                else:
                    if head == None:
                        head = prev if not duplicates else curr
                    prev = prev.next
                    curr = curr.next
        return head