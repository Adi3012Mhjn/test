#Arrays sorted in each row are placed in a matrix of m*n. you have to sort the matrix such that the Space Complexity remains the same.

def insertionSort(arr):
    for i in range(0,len(arr)):
        key=arr[i]
        while i>0 and arr[i-1]>key:
            arr[i]=arr[i-1]
            i=i-1
            arr[i]=key
    return arr
arr=[21,13,14,74,18,19,65,20,35,20]
print("Sorted array is:"%insertionSort(arr))
for i in range(len(arr)):
    print("%d " %arr[i])
