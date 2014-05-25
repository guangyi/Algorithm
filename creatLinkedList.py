'''
Created on Feb 23, 2013

This is the module to create linked List.

@author: zhouguangyi2009
'''
class creatNode(object):
    def __init__(self, next, data):
        self.next = next
        self.data = data
    def __appendToEnd__(self, e_data):
        end = creatNode('', e_data)
        while (self.next != 'null'):
            self = self.next
        self.next = end
'''
n5 = creatNode('null', 5)
n4 = creatNode(n5, 4)
n3 = creatNode(n4, 3)
n2 = creatNode(n3, 2) 
n1 = creatNode(n2, 1) 
n0 = creatNode(n1, 0)     


n = n0
while (n != 'null'):
    print(n.data)
    n = n.next
'''