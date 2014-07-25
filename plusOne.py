class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        newArr = []
        carry = 1 # plus one as carry
        for i in range(len(digits) - 1, -1, -1):
            carry,digit = divmod(digits[i] + carry, 10)
            newArr.insert(0, digit)
        if carry != 0: newArr.insert(0, carry)
        return newArr
print Solution().plusOne([0])
print Solution().plusOne([1,0,9])
print Solution().plusOne([9,9])
'''
[1]
[1, 1, 0]
[1, 0, 0]
'''