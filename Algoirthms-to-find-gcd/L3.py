def gcd(m, n):
	
	for i in range(1, min(m, n)+1):
		if m%i==0 and n%i==0:
			mrcf = i #most recent common factor
			
	return(mrcf)
print("Enter two numbers to find gcd:")
m = int(input("Enter first number: "))
n = int(input("Enter second number: "))
print("GCD: "+str(gcd(m, n)))