class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num) < 3: return []
        num.sort()
        result = []
        prev = None
        for i in range(0, len(num) - 2):
            curr = num[i]
            if curr != prev:
                target = 0 - curr
                start = i + 1
                end = len(num) - 1
                while start < end:
                    if (num[start] + num[end]) > target:
                        end -= 1
                    elif (num[start] + num[end]) < target:
                        start += 1
                    elif (num[start] + num[end]) == target:
                        result.append([curr, num[start], num[end]])
                        start += 1
                        end -= 1
                        while (start < end) and (num[start] == num[start - 1]): start += 1
                        while (start < end) and num[end] == num[end + 1]: end -= 1
                prev = curr
        return result