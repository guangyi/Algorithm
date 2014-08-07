class Solution:
    # @return a string
    def getPermutation(self, n, k):
        number = []
        nFactorial = 1
        for i in range(0, n):
            number.append(str(i + 1))
            nFactorial = nFactorial * (i + 1) # (n)!
        result = ''
        k -= 1
        for index in range(0, n):
            nFactorial /= (n - index) # start as (n - 1)!
            digit = k / nFactorial
            result = result + number[digit]
            k = k % nFactorial
            for j in range(digit + 1, n - index):
                number[j - 1] = number[j]
        return result