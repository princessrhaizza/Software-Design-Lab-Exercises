def multiply(m,n):
    if n==0:
        return 0
    else:
        return m+multiply(m,n-1)
print(multiply(8,30))