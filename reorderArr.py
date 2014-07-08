# Given  [0, 1, 2, 0, 1, 1, 2, 0, 2, 2, 0]
# Return [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2]
def swapArr(arr):
    front = 0
    back = len(arr) - 1
    while front <= back:
        if arr[front] == 1:
            temp = front + 1
            while temp < len(arr) and arr[temp] != 0:
                temp += 1
            if temp < len(arr):
                swap(arr, front, temp)
            front += 1
        elif arr[front] == 2:
            temp = back
            while temp > front and arr[temp] == 2:
                temp -= 1
            if temp > front:
                swap(arr, front, temp)
            back -= 1
        else: front += 1

def swap(arr, front, temp):
    arrTemp = arr[front]
    arr[front] = arr[temp]
    arr[temp] = arrTemp
arr = [2, 2, 1, 1]
swapArr( arr )
print arr
#[2,1,2,2,2,2,2,2,1,1,1,1]