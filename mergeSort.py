class Solution:
    def mergeSort(self, arr):
        self.sort(arr, 0, len(arr) - 1)
    
    def sort(self, arr, start, end):
        if start >= end: return
        mid = start + (end - start) / 2
        self.sort(arr, start, mid)
        self.sort(arr, mid + 1, end)
        self.merge(arr, start, mid, end)
    
    def merge(self, arr, start, mid, end):
        newArr = arr + []
        low = start
        high = mid + 1
        for i in range(start, end + 1):
            if low > mid: 
                arr[i] = newArr[high]
                high += 1 
            elif high > end: 
                arr[i] = newArr[low]
                low += 1
            elif newArr[low] <= newArr[high]: 
                arr[i] = newArr[low]
                low += 1
            else: 
                arr[i] = newArr[high]
                high += 1
    def main(self):
        arr = [5,1,6,8,9,2,7,0,4,3]
        self.mergeSort(arr)
        print arr
Solution().main()