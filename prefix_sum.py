def prefix_sum(data,target):
    n=len(data)
    for i in range(n):
        for j in range(i+1,n):
            if data[i]+data[j]== target:
                return i, j
result=prefix_sum([1,2,3,4,5],9)
print(result)