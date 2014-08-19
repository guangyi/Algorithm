'''
Created on Jul 20, 2014

@author: zhouguangyi2009
'''
class Solution:
    # @return a string
    # intToRoman2 works faster
    # intToRoman works fine but exceed time limit for 3999 on LeetCode OJ
    # Greedy Algorithm
    def intToRoman(self, num):
        symbol = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        value =  [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        string = ''
        index = 0
        while num > 0:
            if num >= value[index]:
                string = string + symbol[index]
                num = num - value[index]
            else: index += 1
        return string
                
    '''               
    def intToRoman(self, num):
        dictR = {1:'|', 4:'|V', 5:'V', 9:'|X', 10:'X', 40:'XL', 50:'L',90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        string = ''
        while num > 0:
            if num in dictR: 
                string = string + dictR[num]
                return string
            else: 
                res = self.getNearestMaxNum(num)
                string = string + dictR[res]
                num = num - res
        return string
    
    def getNearestMaxNum(self, num):
        numStr = str(num)
        length = len(numStr)
        # 5 * pow(10, length-1) return5 or 50 or 500
        # to detect if the num is bigger than 5 or 50 or 500
        if numStr[0] == '9': return 9 * pow(10, length - 1)
        if numStr[0] == '5': return 5 * pow(10, length - 1)
        if numStr[0] == '4': return 4 * pow(10, length - 1)
        else: return 1 * pow(10, length-1)
    '''

print Solution().intToRoman(5)
print Solution().intToRoman2(5)
print Solution().intToRoman(44)
print Solution().intToRoman2(44)
print Solution().intToRoman(58)
print Solution().intToRoman2(58)
print Solution().intToRoman(105)
print Solution().intToRoman2(105)
print Solution().intToRoman(443)
print Solution().intToRoman2(443)
print Solution().intToRoman(589)
print Solution().intToRoman2(589)
print Solution().intToRoman(993)
print Solution().intToRoman2(993)
print Solution().intToRoman(3999)  
print Solution().intToRoman2(3999)