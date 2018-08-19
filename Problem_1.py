def multipleof3and9(N):
    total_sum = 0
    for i in range(N):
        if i%3 == 0 or i%5 == 0:
            total_sum += i
    return total_sum

def multipleof3and9_optimized(N):
    # n*(n+1)/2 = sum of integers N

    div3 = (N-1)//3
    div5 = (N-1)//5
    div15 = (N-1)//15

    sum3 = int(3*(div3*(div3+1))/2)
    sum5 = int(5*(div5*(div5+1))/2)
    sum15 = int(15*(div15*(div15+1))/2)
    print(sum3)
    print(sum5)
    print(sum15)
    print((sum3+sum5)-sum15)

print(multipleof3and9(1000))
print(multipleof3and9_optimized(1000))
