class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0: return None
        if len(inorder) == 1: return TreeNode(inorder[0])
        root = TreeNode(preorder[0])
        rootIndex = self.getSubArr(inorder, root.val)
        leftArr = inorder[0: rootIndex]
        rightArr = inorder[rootIndex + 1:]
        leftLength = len(leftArr)
        root.left = self.buildTree(preorder[1: leftLength + 1], leftArr)
        root.right = self.buildTree(preorder[leftLength + 1: ], rightArr)
        return root
    
    def getSubArr(self, inorder, target):
        for i in range(0, len(inorder)):
            if inorder[i] == target:
                return i
