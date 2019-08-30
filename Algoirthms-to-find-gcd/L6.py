#Euclid's method to find gcd
def gcd(m, n):
	#Assume m>=n
	if m<n:
		(m,n) = (n, m)
	while m%n!=0:
		diff = m-n
		m, n = max(diff, n), min(diff, n)
	return n
			
	
print("Enter two numbers to find gcd:")
m = int(input("Enter first number: "))
n = int(input("Enter second number: "))
print("GCD: "+str(gcd(m, n)))