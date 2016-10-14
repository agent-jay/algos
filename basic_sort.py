import random

arr= [random.randint(-100,100) for i in range(10)]
print("Input array for bubble sort:\n", arr)
def bubble_sort(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-1-j):
            #print(j,i)
            if arr[i]> arr[i+1]:
                tmp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=tmp
    print("Sorted array:\n",arr)

bubble_sort(arr)

arr= [random.randint(-100,100) for i in range(10)]
print("\nInput array for insertion sort:\n", arr)
def insertion_sort(arr):
    for j in range(1,len(arr)):
        key=arr[j]
        i= j-1
        while (i >= 0) and (arr[i]>key):
            arr[i+1]=arr[i]
            i=i-1
        arr[i+1]=key
    print("Sorted array:\n",arr)

insertion_sort(arr)

arr= [random.randint(-100,100) for i in range(10)]
print"\nInput array for merge sort:\n", arr)

