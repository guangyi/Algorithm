class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if A == []: return False
        if len(A) == 1: return True
        result = False
        lastPosition = len(A) - 1
        for testPosition in range(len(A) - 2, -1, -1):
            if A[testPosition] >= lastPosition- testPosition:
                result = True
                lastPosition = testPosition
            else: result = False
        return result
    
    # jumpGame 2
    def jump(self, A):
        if len(A) == 1: return 0
        result = 0
        prevRange = 0
        currRange = 0
        for i in range(0, len(A)):
            if i + A[i] > currRange:
                if i > prevRange:
                    result += 1
                    prevRange = currRange
                currRange = i + A[i]
            if currRange >= len(A) - 1: return result + 1
    
    # jumpGame 2         
    def jumpDP(self, A):
        '''works but not efficient!!! '''
        result = [0]
        for testPosition in range(1, len(A)):
            minStep = 9223372036854775807
            for prevPosition in range(0, len(A[:testPosition])):
                if A[prevPosition] >= testPosition - prevPosition:
                    if result[prevPosition] < minStep: minStep = result[prevPosition]
            result.append(minStep + 1)
        return result[-1]
print Solution().canJump([2,3,1,1,4])
print Solution().canJump([3,2,1,0,4])
print Solution().canJump([0,4])
print Solution().jumpDP([2,3,1,1,4])
print Solution().jump([2,3,1,1,4])