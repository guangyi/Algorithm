'''
Created on Jul 25, 2014

@author: zhouguangyi2009
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        # method 1
        pathArr = self.sum(root)
        
        # method 2
        print self.sum3(root, 0)
        
        sum = 0
        for arr in pathArr:
            length = len(arr)
            for i in range(0, length):
                sum = sum + arr[i] * pow(10, length - 1 - i)
        return sum
    
    def sum3(self, root, resultSoFar):
        if root == None: return 0
        resultSoFar  = resultSoFar * 10 + root.val
        left = self.sum3(root.left, resultSoFar)
        right = self.sum3(root.right, resultSoFar)
        if left == 0 and right == 0: return resultSoFar
        return left + right
            
    def sum(self, root):
        if root == None: return ''
        leftResult = self.sum(root.left)
        if leftResult:
            for item in leftResult:
                item.insert(0, root.val)
        rightResult =  self.sum(root.right)
        if rightResult:
            for item in rightResult:
                item.insert(0, root.val)
        if (not leftResult) and (not rightResult):
            return [[root.val]]
        return (leftResult or [])   + (rightResult or [])
   
    
        

root = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
root.left = node1
root.right = node4
node1.left = node2
node1.right = node3
node4.right = node5
node5.left = node6
print Solution().sumNumbers(root)
