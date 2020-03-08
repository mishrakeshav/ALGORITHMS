def max_heapify(A,i,size):
    l = 2*i +1
    r = 2*i +2
    largest = i 
    if(l < size and A[l] > A[largest]):
        largest = l 
    
    if(r < size and A[r] > A[largest]):
        largest = r 
    if largest != i:
        A[largest],A[i] = A[i],A[largest]
        max_heapify(A,largest,size)


def build_max_heap(A):
    n = len(A)
    for i in range(n//2,-1,-1):
        max_heapify(A,i,n)

def heapSort(A):
    n = len(A) -1
    build_max_heap(A)
    while n>=0:
        A[0],A[n]=A[n],A[0]
        max_heapify(A,0,n)
        n -= 1
        
A = [1, 9, 10, 8, 6, 25, 19, 20, 22, 21]
heapSort(A)
print(A)

