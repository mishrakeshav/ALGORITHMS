#Algorithm: Bubble Sort
#Input: An array(or List) of Size n and n
#Output: Sorted array 
#Complexity 0(n^2)

def bubbleSort(A, n):
	while(True):
		flag = 0
		for i in range(n-1):
			if A[i]>A[i+1]:
				temp = A[i]
				A[i] = A[i+1]
				A[i+1] = temp
				flag = 1
		if flag == 0:
			break
	return A

#getting input 
n = int(input("Enter number of elements: "))
A = list(map(int, input("Enter elements of array: ").split()))
print(bubbleSort(A, n))