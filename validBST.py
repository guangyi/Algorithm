def isValidBST(self, root):
        # 9223372036854775807 is sys.maxint but OJ don't understand it
        return self.isValid(root, -9223372036854775807, 9223372036854775807)
    def isValid(self, root, start, end):
        if root == None: return True
        if root.val <= start or root.val >= end: return False
        left = self.isValid(root.left, start, root.val)
        if left == False: return False
        right = self.isValid(root.right, root.val, end)
        if right == False: return False
        return True