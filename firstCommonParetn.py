class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def commonParent(self, root, a, b):
        resultA = [a.val]
        resultB = [b.val]
        self.common(root, a, resultA)
        self.common(root, b, resultB)
        print resultA, resultB
        
    def common(self, root, a, result):
        if root == None: return
        if root == a: return True
        left = self.common(root.left, a, result)
        if left == True:
            result.insert(0, root.val)
            return True
        right = self.common(root.right, a, result)
        if right == True:
            result.insert(0, root.val)
            return True
        
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
node4.left = node3
node4.right = node5
node5.left = node6

Solution().commonParent(root, node3, node4) #[0,4,3] [0, 4, 5, 6]
