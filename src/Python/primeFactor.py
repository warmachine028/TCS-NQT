def primefactor(n):
    array = []
    i = 2
    while n > 1:
        while n % i == 0:
            array.append(i)
            n /= i
        i += 1
    print(array)

primefactor(12)
primefactor(60)
