'''
Created on May 24, 2014

Partition List

@author: zhouguangyi2009
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head == None:
            return None
        else:
            # extra two list
            large = ListNode(0)
            small = ListNode(0)
            largeHead = large
            smallHead = small
            while head != None:
                print "times"
                if head.val < x:
                    print (head.val,x)
                    small.next = head
                    small = small.next
                else:
                    large.next = head
                    large = large.next
                head = head.next
            print small.next.val
            print small.next.next.val
            print large.next.val
            print large.next.next.val
            small.next = largeHead.next
            return smallHead.next

node1 = ListNode(4)
node2 = ListNode(3)
#node3 = ListNode(2)
#node4 = ListNode(1)
node1.next = node2
#node2.next = node3
#node3.next = node4
ret = Solution().partition(node1, 2)
print "w" , ret.val
print "w" , ret.next.val