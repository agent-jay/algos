def merge(arr, p, q, r):
    i,j=p,q+1
    tmp=[]
    while i<=q and j<=r:
        if arr[i]<arr[j]:
            tmp.append(arr[i])
            i+=1
        else:
            tmp.append(arr[j])
            j+=1
    while(i<=q):
        tmp.append(arr[i])
        i+=1
    while(j<=r):
        tmp.append(arr[j])
        j+=1
    print(tmp)
    for i,val in enumerate(tmp):
        arr[p+i]=val

def merge_sort(arr, p, r):
    q= (p+r)//2
    if p<r:
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        print('\n',p,q,r)
        print("before",arr)
        merge(arr, p, q, r)
        print("after",arr)

arr=[6263,-235, 23,1,345, -1244,-2432, 2,1,20]

print('THIS IS THE ARRAY',arr)
merge_sort(arr,0,len(arr)-1)
print('SORTED ARRAY',arr)

