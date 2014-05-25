'''
Created on Feb 16, 2013

@author: zhouguangyi2009
'''

def test(s):
    r = []
    result = []
    for i in range(0, len(s)):
        if i == 0:
            r.append(s[i])
        else:         
            if s[i] == s[i-1]:
                r.append(s[i])
            else:
                result.append(r[0])
                result.append(len(r))
                r=[]
    return result
print (test('ssbbbccddd'))