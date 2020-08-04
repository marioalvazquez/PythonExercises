fibonnaci_cache = {}

def fibonacci(n):
    if n in fibonnaci_cache:
        return fibonnaci_cache[n]
    #compute
    if n == 1 or n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)
        
    # Cache
    fibonnaci_cache[n] = value
    return value

for n in range(1, 1001):
    print (str(n) + " : " + str(fibonacci(n)))


