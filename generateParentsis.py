'''
Created on Jul 9, 2014

@author: zhouguangyi2009
'''
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        self.n = n
        result = self.generateHelp(5, n - 1, n, [[5]])
        finalResult = []
        for arr in result:
            pattern = ''
            for i in arr:
                if i == 5:pattern += '('
                else: pattern += ')'
            finalResult.append(pattern)
        return finalResult
            
    def generateOptions(self, total, counterPos, counterNeg):
        if counterPos < self.n and total == 0: return [[5]]
        if counterPos < self.n and counterNeg < self.n: return[[5],[-5]]
        if counterPos >= self.n and counterNeg < self.n: return[[-5]]
        if counterNeg < self.n and counterPos > self.n :return [[5]]
        
    def generateHelp(self, total, counterPos, counterNeg, result):
        while True:
            tempResult = []
            for pattern in result:
                total = 0
                counterPos = counterNeg = 0
                for i in pattern:
                    total += i
                    if i > 0: counterPos += 1
                    elif i < 0: counterNeg += 1
                if counterPos >= self.n and counterNeg >= self.n: return result
                options = self.generateOptions(total, counterPos, counterNeg)
                for option in options:
                    tempResult.append(pattern + option)
            result = tempResult
        return result
#print Solution().generateParenthesis(2)
#['(())', '()()']
#print Solution().generateParenthesis(3)
#['((()))', '(()())', '(())()', '()(())', '()()()']
