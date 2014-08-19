class Solution:
    def quickSort(self, arr):
        self.sort(arr, 0, len(arr) - 1)
    def sort(self, arr, start, end):
        if start < end:
            p = self.partition(arr, start, end)
            self.sort(arr, start, p - 1)
            self.sort(arr, p + 1, end)
    def partition(self, arr, start, end):
        pivot = arr[start]
        low = start + 1
        high = end
        while low <= high:
            while low <= high and arr[low] < pivot:
                low += 1
            while arr[high] > pivot and high >= low:
                high -= 1
            if low < high: arr[low], arr[high] = arr[high], arr[low]
            else: arr[start], arr[high] = arr[high], arr[start]
        return high
    def main(self):
        arr = [5,1,6,8,9,2,7,0,4,3]
        self.quickSort(arr)
        print arr
        arr = [4, 3, 2, 1]
        self.quickSort(arr)
        print arr
Solution().main()