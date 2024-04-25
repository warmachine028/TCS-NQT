# 0, 0, 2, 1, 4, 2, 6, 3, 8, 4, 10, 5, 12, 6, 14, 7, 16, 8


def term(n):
    return n // 2 * 2 if n % 2 else n // 2 - 1


def main():
    print(term(int(input())))


if __name__ == "__main__":
    main()
