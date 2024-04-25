def term(n):
    return (6 if n % 2 else 7) * (n // 2)


def main():
    print(term(int(input()) - 1))


if __name__ == "__main__":
    main()
