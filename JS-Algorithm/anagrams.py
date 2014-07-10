class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        D = dict()
        for word in strs:
            w = ''.join(sorted(word)).replace(' ','')
            if w not in D:
                D[w] = [word]
            else: D[w].append(word)
        
        # Return result
        result = []
        for key in D:
            if len(D[key]) > 1:
                for wd in D[key]:
                    result.append(wd)
        return result
    