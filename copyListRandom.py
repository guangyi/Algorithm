# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        tempResult = {}
        Head = prev = RandomListNode(0)
        while head != None:
            if head.label not in tempResult:
                newHead = RandomListNode(head.label)
                tempResult[head.label] = newHead
            else:newHead = tempResult[head.label]
            if head.random != None and head.random.label not in tempResult:
                random = RandomListNode(head.random.label)
                tempResult[head.random.label] = random
            else: random = None if not head.random else tempResult[head.random.label]
            newHead.random = random
            prev.next = newHead
            prev = newHead
            head = head.next
        return Head.next

    def main(self):
        head = RandomListNode(0)
        node1 = RandomListNode(1)
        node2 = RandomListNode(2)
        head.next = node1
        head.random = node2
        node1.next = node2
        node1.random = node2
        node2.random = head
        newHead = self.copyRandomList(head)
        while newHead != None:
            print newHead.label
            print newHead.random.label
            newHead = newHead.next
            
Solution().main()