#ALGORITHM: Merge sort
#Input: Array(list) of size n and n
#Output: Sorted array

def merge(L, R, A, k):
	i = 0; j = 0; 
	while i < len(L) and j < len(R):
		if(L[i]<R[j]):
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
		k += 1
	while i < len(L):
		A[k]=L[i]
		i+=1
		k+=1
	while j < len(R):
		A[k] = R[j]
		j += 1
		k += 1




def mergeSort(A):
	if(len(A)>1):
		mid = len(A)//2 #Midpoint of the array
		#Dividing the array elements into two halfs
		L = A[:mid] #left half
		R = A[mid:] #right half
		i = 0; j = 0; k=0
		mergeSort(L)   #sorting the left part
		mergeSort(R)   #sorting the right part
		merge(L, R, A, k)  #merging the left and the right part
		



if __name__ == '__main__':
	#A = []
	#n = int(input("Enter number of elements: "))
	#for i in range(n):
		#A.append(int(input("Enter element: ")))
	A = list(range(50,0,-1))
	mergeSort(A)
	print(A)

