'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
'''
class Solution:
    # @return a string
    def countAndSay(self, n):
        result = ['1']
        count = 1
        while count < n:
            temp = []
            counter = 1
            prev = result[0]
            for string in result[1:]:
                if string == prev: counter += 1
                else:
                    temp.append(str(counter))
                    temp.append(prev)
                    prev = string
                    counter = 1
            temp.append(str(counter))
            temp.append(prev)
            result = temp
            count += 1
        return ''.join(result)
print Solution().countAndSay(2)
print Solution().countAndSay(3)
print Solution().countAndSay(4)
print Solution().countAndSay(5)
print Solution().countAndSay(6)
'''
11
21
1211
111221
312211
'''