'''
Created on Apr 6, 2014

@author: zhouguangyi2009
'''
import heapq

class kClosestPoint():
    
    def kClosest(self, originX, originY, pointList, k):
        heapList = []
        origin = Points(originX, originY)
        
        for point in pointList:
            newPoints = Points(point[0], point[1])
            distTuple = Distance(newPoints, origin).getPoint()
            heapq.heappush(heapList, distTuple)
            pointList = heapq.nsmallest(k, heapList)
        return pointList

class Points():
    __px = NotImplemented
    __py = NotImplemented
    
    def __init__(self, x, y):
        self.__px = x
        self.__py = y
        pass
    
    def getPx(self):
        return self.__px
        pass
    
    def getPy(self):
        return self.__py
        pass
        

class Distance():
    __dist = NotImplemented
    __x = __y = NotImplemented
    __dot = NotImplemented
    
    def __init__(self, dot, origin):
        self.__dot = dot
        self.__dist = (dot.getPx()-origin.getPx())**2 + (dot.getPy() - origin.getPy())**2
    
    def getDist(self):
        return self.__dist
    
    def getPoint(self):
        self.__x = self.__dot.getPx()
        self.__y = self.__dot.getPy()
        return (self.__dist, (self.__x, self.__y))

listp = kClosestPoint().kClosest(3,5,[(1,2),(3,6),(0,0),(3,7),(4,66),(44,66),(12,56),(1,3),(6,5),(32,5)], 5)
print listp
'''    
    def getDis(self):
        return self.__dis
        pass
    
    def calcDis(self, origin):
        if origin == NotImplemented:
            raise EOFError('Origin not implemented! ')
            pass
        self.__dis = (origin.getPx()-self.__px)**2+(origin.getPy()-self.__py)**2
        pass
'''    
    
        
            
        