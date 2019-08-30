#Euclid's algorithm to find gcd
def gcd(m, n):
	#Assume m>=n
	if m<n:
		(m,n)=(n,m)
	if(m%n==0):
		return n
	diff = m-n
	#diff > n? Possible
	return gcd(max(diff,n), min(diff,n))
			
	
print("Enter two numbers to find gcd:")
m = int(input("Enter first number: "))
n = int(input("Enter second number: "))
print("GCD: "+str(gcd(m, n)))