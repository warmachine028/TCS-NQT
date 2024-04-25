def fib(n):
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)


def prime(n):
    result: int
    i = 2
    while n:
        prime = True
        for j in range(2, i // 2 + 1):
            if not i % j:
                prime = False
                break

        if prime:
            result = i
            n -= 1
        
        i += 1

    return result


def main():
    x = int(input())
    for n in range(1, x + 1):
        if n % 2:
            res = fib((n + 1) / 2)
        else:
            res = prime(n // 2)
        print(res, end=", ")


main()
