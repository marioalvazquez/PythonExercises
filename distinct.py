def distinct(A):
	n = len(A)
	A.sort()
	result = 1
	for k in range(1, n):
		if A[k] != A[k-1]:
			result += 1
	return result

solution = distinct([1,1,2,1,2,1,4,2,7])
print(solution)
