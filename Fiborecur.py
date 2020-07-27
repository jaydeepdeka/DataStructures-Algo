def FiboRecur(n):
    if n<2:
        return n
    return FiboRecur(n-1) + FiboRecur(n-2)
