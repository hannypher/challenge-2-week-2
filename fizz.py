def fizzbuzz(h, n):
    h=len(2,4,6,8,10)
    n=len(1,3,5,7,9)
    w=len(h)+len(n)
    if w % 3 == 0:
        return "fizz"
    elif w % 5 == 0:
        return "buzz"
    elif w % 3 == 0 and w % 5 == 0:
        return "fizzbuzz"
    else:
        return "w"
print(fizzbuzz([2,4,6,8,10], [1,3,5,7,9]))