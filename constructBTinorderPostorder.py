class TreeNode:
    def __init__(self, x):
        self.val = x         
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if inorder == []: return None
        if len(inorder) == 1: return TreeNode(inorder[0])
        root = TreeNode(postorder[-1])
        rootIndexInorder = inorder.index(postorder[-1])
        leftArray = inorder[0: rootIndexInorder]
        rightArray = inorder[rootIndexInorder + 1: ]
        leftArrLength = len(leftArray)
        rightArrLength = len(rightArray)
        root.left = self.buildTree(leftArray, postorder[0: leftArrLength])
        root.right = self.buildTree(rightArray, postorder[leftArrLength : leftArrLength + rightArrLength])
        return root
Solution().buildTree([1,3,2], [3,2,1])