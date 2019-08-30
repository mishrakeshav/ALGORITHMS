#Inserion Sort
#Input: Array of size n and n
#Output: Sorted array
def insertionSort(A,n):
	for sliceEnd in range(n):
		pos = sliceEnd

		while pos > 0 and A[pos] < A[pos-1]:
			A[pos], A[pos-1] = A[pos -1], A[pos]
			pos -= 1
n = int(input("Enter number elements: "));
A = list(map(int, input("Enter elments: \n").split()))
insertionSort(A,n)
for i in A:
	print(i)
	