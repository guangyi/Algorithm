'''
Created on Mar 9, 2013

@author: zhouguangyi2009
'''
import sets
def step_count(n):
    dic = {}
    
    if n == 1:
        steps = ['1']
        dic[1] = steps
        return steps
    if n == 2:
        steps = ['11','2']
        dic[2] = steps
        return steps
    if n == 3:
        steps = ['111','12','21','3']
        dic[3] = steps
        return steps
    else:
        step_n = []
        for i in range(1,n):
            for step_i in step_count(i):
                for step_ni in step_count(n-i):
                    step_n.append(step_ni + step_i)
        dic[n] = sets.Set(step_n)
        print(dic[n]) 
        return sets.Set(step_n)
#step_count(5)

def count_path(x,y):
    m = 0
    n = 0
    step = 0
    if (x == 0) or (y == 0):
        step = 1
    else:
        while True:
            if (m == x) & (n == y):
                return step
            elif m == x :
                step = step + 1
                return step
            elif n == y:
                step = step + 1
                return step           
            else: 
                m = m + 1
                n = n + 1
                step = step + 2
    return step
a = count_path(2,4)   
print a     
                       
            
        