# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None: return False
        return self.pathSum(root, sum, 0)
    
    def pathSum(self, root, sum, currSum):
        # have negative number!!! so can't return False when root + subroot == sum --
        if root.val + currSum == sum:
            if (not root.left) and (not root.right): return True
        
        # only execute steps below when root.val + currSum < sum
        currSum = currSum + root.val
        if root.left:
            left = self.pathSum(root.left, sum, currSum)
            if left == True: return True
        if root.right:
            right = self.pathSum(root.right, sum, currSum)
            if right == True: return True
        return False