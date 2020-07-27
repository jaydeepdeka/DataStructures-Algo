def factRecursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factRecursive(n-1)

def factIterative(n):
    result = 1
    for i in range(1,n+1):
        result = i*result
    return result
