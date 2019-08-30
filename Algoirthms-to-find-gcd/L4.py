def gcd(m, n):
	
	i = min(m, n)
	while i>0 :
		if m%i == 0 and n%i == 0:
			return (i)
		else :
			i -= 1
			
	
print("Enter two numbers to find gcd:")
m = int(input("Enter first number: "))
n = int(input("Enter second number: "))
print("GCD: "+str(gcd(m, n)))