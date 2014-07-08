class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        D = dict()
        for word in strs:
            w = ''.join(sorted(word))
            # key in D and key in D.keys() get the same result
            # but D.keys() will create a list of keys When lots of data -- out of time
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