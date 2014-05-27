'''
Created on May 26, 2014

Get all subset of a distinct integer set

@author: zhouguangyi2009
'''

class Solution():
    def getAllSubset(self, Set):
        if not Set:
            return [] 
        # left rotation means get 2^n
        # for each set, max number of subset is 2^n --> n is the size of set
        Max = 1 << len(Set)
        result = []
        for i in range(0, Max):
            if i == 0:
                result.append([])
            else: result.append(self.intToSubset(i, Set))
        return result
    
    def intToSubset(self, i, Set):
        k = i
        index = 0 #
        result = []
        while k > 0:
            if (k & 1) == 1:
                result.append(Set[index])
            index += 1
            k = k >> 1
        result.sort()# if require sorted
        return result

print Solution().getAllSubset([])
print Solution().getAllSubset([2])       
print Solution().getAllSubset([4,1,0])

    '''
    Recursion way
    def subsets(self, Set):
        allsubSet = []
        self.recurSet(Set, len(Set),allsubSet)
        return allsubSet
    
    def recurSet(self, Set, index, allsubSet):
        result = []
        if index == 0:
            allsubSet.append([])
            return [[]]
        else:
            subset = self.recurSet(Set, index-1, allsubSet) 
            result = result + subset
            for item in result:
                newSub = item + [Set[index-1]]
                # single element array sort return None
                if len(newSub) > 1:
                    newSub.sort()
                allsubSet.append(newSub )
        return allsubSet
    '''    