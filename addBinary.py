class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        lenA = len(a)
        lenB = len(b)
        result = ''
        idxA = lenA - 1
        idxB = lenB -1
        carry = 0
        while idxA >= 0 or idxB >= 0:
            strA = '0' if idxA < 0 else a[idxA]
            strB = '0' if idxB < 0 else b[idxB]
            string = bin(int(strA) + int(strB) + carry).replace('0b','')
            result = string[-1] + result
            carry = int(string[-2]) if len(string) > 1 else 0
            idxA -= 1
            idxB -= 1
        if carry != 0: result = str(carry) + result
        return result
print Solution().addBinary('111', '1')
print Solution().addBinary('0', '0')