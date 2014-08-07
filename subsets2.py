class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        if S == []: return []
        if len(S) == 1: return [S,[]]
        S.sort()
        
        current = [S[0]]
        subsets = self.subsetsWithDup(S[1:])
        result = [] + subsets
        for arr in subsets:
            temp = arr + []
            if (current + temp) not in subsets:
                result.append(current + temp)
        return result