'''
Created on Feb 24, 2013

This is the test solution for the No.2-7

@author: zhouguangyi2009
'''

from creatLinkedList import creatNode

def isPalindrom(head):
    fast = creatNode(head, '')
    slow = creatNode(head, '')
    stack = []
    while(fast != 'null') &( fast.next != 'null'):
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    if fast == 'null':
        slow = slow.next
    
    while slow != 'null':
        if slow.data != stack.pop():
            return False
        slow = slow.next
    return True
n5 = creatNode('null', 0)
n4 = creatNode(n5, 1)
n3 = creatNode(n4, 2)
n2 = creatNode(n3, 2) 
n1 = creatNode(n2, 1) 
n0 = creatNode(n1, 0)
head = n0
a = isPalindrom(head)
print a