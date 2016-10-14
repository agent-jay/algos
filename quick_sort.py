
def swap(arr,pos1,pos2):
    tmp=arr[pos1]
    arr[pos1]=arr[pos2]
    arr[pos2]=tmp
    

def partition(arr,p,r):
    q,j=p,p
    pivot=arr[r]
    while j<r:
        if arr[j]<=pivot:
            swap(arr,j,q)
            q+=1
        j+=1
    swap(arr,r,q)
    return q

def quick_sort(arr,p,r):
    if r-p>=1:
        q= partition(arr,p,r) 
        print(q)
        quick_sort(arr,p,q-1)
        quick_sort(arr,q+1,r)


arr=[6263,-235, 23,1,345, -1244,-2432, 2,1,20]

print('THIS IS THE ARRAY',arr)
quick_sort(arr,0,len(arr)-1)
print('SORTED ARRAY',arr)

