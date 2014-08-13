class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        return  self.conbination(candidates, target)
        
    def conbination(self, candidates, target):
        if target == 0: return [[]]
        if candidates == []: return []
        if target < candidates[0]: return []
        result = []
        prev = None
        for i in range(0, len(candidates)):
            if candidates[i] > target: break
            else:
                if candidates[i] != prev:
                    prev = candidates[i]
                    res = self.conbination(candidates[i:], target - candidates[i])
                    if res != []:
                        for arr in res:
                            arr.insert(0, candidates[i])
                            result.append(arr)
        return result