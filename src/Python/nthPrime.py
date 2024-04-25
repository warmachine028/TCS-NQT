def prime(n):
    result: int
    num = 2
    while n:
        flag = True
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                flag = False
                break
        if flag:
            n -= 1
            result = num
        num += 1
    return result


def main():
    print(prime(int(input())))
    # for i in range(1, int(input()) + 1):
    #     print(prime(i), end=", ")


main()
