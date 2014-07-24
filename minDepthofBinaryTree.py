# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0: return right + 1
        if right == 0: return left + 1
        return min(left, right) + 1