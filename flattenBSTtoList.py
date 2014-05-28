class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root == None:
            return None   
        right = self.flatten(root.right)
        left = self.flatten(root.left)        
        if right == None and left != None:
            root.right = left
            root.left = None
        elif left != None and right != None:
            rightTemp = right
            root.right = left
            root.left = None
            while left.right != None:
                left = left.right
            left.right = rightTemp
        return root
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
node5 = TreeNode(6)
node6 = TreeNode(7)
root.left = node1
root.right = node4
node1.left = node2
node1.right = node3
node4.right = node5
node5.left = node6
rot =  Solution().flatten(root)
while rot != None:
    print rot.val
    print rot.left
    rot = rot.right