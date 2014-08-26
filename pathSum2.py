class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum2(self, root, sum):
        result = []
        self.path2(root, [], 0, sum, result)
        return result
    def path2(self, root, pathArr, currSum, sum, result):
        if root == None: return 
        if not root.left and not root.right and currSum + root.val == sum:
            result.append(pathArr + [root.val])
            return 
        pathArr.append(root.val)
        currSum = currSum + root.val
        if root.left:
            self.path2(root.left, pathArr, currSum, sum, result)
        if root.right:
            self.path2(root.right, pathArr, currSum, sum, result)
        pathArr.pop()
        return 
     

     
    def pathSum(self, root, sum):
        result = []
        if root != None:  result = self.path(root, sum, 0)
        return result
    def path(self, root, sum, currSum):
        if root.val + currSum == sum:
            # root is leave
            if (not root.left) and (not root.right): 
                return [[root.val]]
        currSum = currSum + root.val
        tempResult = []
        if root.left:
            leftLevel = self.path(root.left, sum, currSum)
            if leftLevel:
                for arr in leftLevel:
                    arr.insert(0, root.val)
                    tempResult.append(arr)
        if root.right:
            rightLevel = self.path(root.right, sum, currSum)
            if rightLevel: 
                for arr in rightLevel:
                    arr.insert(0, root.val)
                    tempResult.append(arr)
        return tempResult
        