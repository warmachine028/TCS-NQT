"""
Express given number as Sum of Two Prime Numbers
"""


def prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5 + 1)):
        if not (n % i):
            return False
    return True


def solution(n: int) -> str:
    for i in range(1, n):
        if prime(i) and prime(n - i):
            return "Yes"
    return "No"


print(solution(11))  # No
print(solution(72))  # 5 67 Yes
print(solution(73))  # 71 2 Yes
print(solution(74))  # 71 3 Yes
