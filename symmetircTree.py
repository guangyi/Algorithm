# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None: return True
        thisLevel = [root]
        while thisLevel != []:
            start = 0
            end = len(thisLevel) - 1
            nextLevel = []
            while start < end:
                if (thisLevel[start] and not thisLevel[end]) or (not thisLevel[start] and thisLevel[end]):
                    return False
                elif (thisLevel[start] == thisLevel[end]) or thisLevel[start].val == thisLevel[end].val:
                    start += 1
                    end -= 1
                else: return False
            for item in thisLevel:
                if item != None:
                    nextLevel.append(item.left)
                    nextLevel.append(item.right)
            thisLevel = nextLevel
        return True