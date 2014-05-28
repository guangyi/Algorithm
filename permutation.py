class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    '''
    	recurtion way
    	previous store each mid result of recursion
    	is until last recusion, it has every permuation that last element needs.
    '''
    def permute(self, num):
        if not num: return
        if len(num) == 1: return [num]
        previous = self.permute(num[:-1])
        current = num[-1]
        result = []
        for item in previous:
            self.insert(current, item, result)
        return result
    def insert(self, current, previous, result):
        for i in range(0, len(previous)+1):
            temp = [] + previous
            temp.insert(i, current)
            result.append(temp)

print Solution().permute([])
print Solution().permute([1,2,3])
print Solution().permute([1,2,3,4])