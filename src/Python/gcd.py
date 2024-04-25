def gcd(a: int, b: int) -> int:
    return a if b == 0 else gcd(b, a % b)


print(gcd1 := gcd(64, 16))
print(gcd2 := gcd(4, 12))
print(gcd(gcd1, gcd2))
