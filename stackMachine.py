'''
Created on Apr 15, 2014

@author: zhouguangyi2009
'''
class Solution():
    
    def calcString(self, str):
        resultStack = []
        try:
            for char in str:
                #get single character in string
                if char =='+':# if + then pop previous two number and add
                    a = resultStack.pop()
                    b = resultStack.pop()
                    resultStack.append(a + b)
                   
                elif char == '*':
                    a = resultStack.pop()
                    b = resultStack.pop()
                    resultStack.append(a * b)
                
                elif char.isdigit():
                    resultStack.append(int(char))
                    
            if len(resultStack) == 1:
                return resultStack.pop()
            else:return -1
        except:return -1
                
stackMachine = Solution().calcString('445++77*+')                      
print stackMachine                     
                
                