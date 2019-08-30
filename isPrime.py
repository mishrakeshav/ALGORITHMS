#ALGORITHM : To check if a number is prime or not
#Input: A positive integer
#Output: True- If number is prime, False - If number is not prime
#This is the most efficient algorithm 
def isPrime(n):
	for i in range(2,int(n**0.5)+1): #Checks only till square root of n
		if n%i==0:
			return False
	return True

n = int(input("Enter number : "));
print(isPrime(n))