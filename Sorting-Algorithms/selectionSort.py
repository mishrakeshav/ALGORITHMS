#Selection sort
#Input: array/list of size n 
#Output: Sorted array

def selectionSort(A):
    for start in range(0, len(A) - 1):
        minpos = start
        for i in range(start + 1, len(A)):
            if A[i] < A[minpos]:
                minpos = i
        A[start], A[minpos] = A[minpos], A[start]

n = int(input("Enter the length of the array: "))
A = []
for i in range(n): 
	A.append(int(input("Enter element: ")))
#Sorting the array/list
selectionSort(A)
print(A)



