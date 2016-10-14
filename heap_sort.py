heap=[]

class Heap():
    def __init__(self,arr):
        self.arr=arr
        self.heap_size= -1 
    def __str__(self):
        return str(self.arr)+' '+str(self.heap_size)


def swap(arr,pos1,pos2):
    tmp=arr[pos1]
    arr[pos1]=arr[pos2]
    arr[pos2]=tmp
 
def max_heapify(heap, i):
    left=2*i+1
    right=2*i+2
    largest=i
    if left< heap.heap_size and heap.arr[left]>heap.arr[i]:
        largest=left
    if right< heap.heap_size and heap.arr[right]>heap.arr[largest]:
        largest=right

    if largest!=i:
        swap(heap.arr, i, largest)
        max_heapify(heap,largest)

def build_maxheap(heap):
    heap.heap_size= len(heap.arr)
    for i in range(len(heap.arr)//2 -1, -1, -1):
        max_heapify(heap,i)

def heap_sort(heap):
    build_maxheap(heap)
    for i in range(len(heap.arr)-1, 0, -1):
        swap(heap.arr,0, i)
        heap.heap_size-=1
        max_heapify(heap,0)

heap= Heap([6263,-235, 23,1,345, -1244,-2432, 2,1,20])
#heap= Heap([1,8,9,7])
print('THIS IS THE ARRAY',heap)
#build_maxheap(heap)
heap_sort(heap)
print('SORTED ARRAY',heap)


