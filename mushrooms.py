def prefix_sums(A):
	n = len(A)
	P = [0] * (n+1)
	for k in range(1,n+1):
		P[k] = P[k-1] + A[k-1]
	return P

result =  prefix_sums([2,3,7,5,1,3,9,10])

print(result)
