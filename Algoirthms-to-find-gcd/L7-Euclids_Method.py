#Euclid's method to find gcd
def gcd(m, n):
	#Assume m>=n
	if m<n:
		(m,n) = (n, m)
	if m%n == 0:
		return n
	else:
		return gcd(n, m%n) # m%n < n , always!
			
	
print("Enter two numbers to find gcd:")
m = int(input("Enter first number: "))
n = int(input("Enter second number: "))
print("GCD: "+str(gcd(m, n)))