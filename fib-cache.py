from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    if type(n) != int:
        raise TypeError("n is not a number")
    if n < 1:
        raise ValueError("n is less than 1")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci("hola")  
for n in range(1, 501):
    print(str(n)+" : "+str(fibonacci(n)))