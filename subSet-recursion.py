 '''
Created on May 26, 2014

Get all subset of a distinct integer set-- Recursion way

@author: zhouguangyi2009
'''

class Solution():
    #Recursion way
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
   