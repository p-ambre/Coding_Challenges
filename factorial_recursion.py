def factorial(n):
    print ("fact of: ",+n)
    if (n == 0):
        return 1
    else:
        result = n * factorial(n-1)
        print("fact of:",+n ,"is",+result)
        return result
fact = factorial(5)
print(fact)
