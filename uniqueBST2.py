class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        temp = []
        for i in range(1,  n + 1):
            temp.append(i)
        return self.trees(temp)
    def trees(self, arr):
        if arr == []: return [None]
        if len(arr) == 1: return [TreeNode(arr[0])]
        result = []
        for i in range(0, len(arr)):
            leftArr = arr[0:i]
            rightArr = arr[i + 1:]
            rootLeft =  self.trees(leftArr)
            rootRight = self.trees(rightArr)
            for left in range(0, len(rootLeft)):
                for right in range(0, len(rootRight)):
                    # !!!! create new root node!!!!!
                    root = TreeNode(arr[i])
                    root.left = rootLeft[left]
                    root.right = rootRight[right]
                    result.append(root)
        return result