def countingSort(A,k):
	n = len(A)
	count = [0] * (k+1)
	for i in range(n):
		count[A[i]] += 1
		print(count[A[i]])
	p = 0
	for i in range(k+1):
		print("First loop")
		print(i)
		for j in range(count[i]):
			print("Second loop")
			print(j)
			A[p] = i
			p += 1
	return A

sorted = countingSort([0,9,0,0,12,0,4,8,10,4], 11)
print(sorted)
