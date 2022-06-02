def maxmin(data,n):
    if n == 1:
        return data[0],data[0]

    else:
        x ,y= maxmin(data, n - 1)

        return data[n - 1] if (data[n - 1] > x) else x, data[n - 1] if (data[n - 1] <y) else y

data=[1,2,3,4,5,6,7,8,9,10]
m,n=maxmin(data,9)

print(m,n)