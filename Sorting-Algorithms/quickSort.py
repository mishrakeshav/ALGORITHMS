#ALGORITHM: QuickSort
#Input: Array(list) of size n and n
#Output: Sorted array
def partition(A, start, end):
	pivot = A[start]
	i = start + 1
	j = end - 1


	while  True:

		while(i<=j and A[i]<= pivot):
			i += 1
		while(i<=j and A[j]>=pivot):
			j -= 1

		if i<=j :
			A[i], A[j] = A[j], A[i]
		else:
			A[start], A[j] = A[j], A[start]
			return j;


def quickSort(A, start , end):

	if end - start >1:
		p = partition(A, start, end)
		quickSort(A, start, p)
		quickSort(A, p+1, end)



if __name__ == '__main__':
	n = int(input("Enter the number of elements: "))
	A = []
	for i in range(n):
		A.append(int(input("Enter element: ")))

	quickSort(A, 0, n-1)
	print(A)


	