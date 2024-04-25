"""
Problem Statement: Given a geometric Progression (G.P) sequence with some inputs as:-

a, first term
r, common ratio
n, number of terms
 Write a program to find the sum of the geometric Progression Series.

"""

from dataclasses import dataclass


@dataclass
class Solution:
    a: int
    r: int
    n: int

    def solution(self):  # O(n)
        result = 0
        for i in range(self.n):
            result += self.a * self.r**i

        return result

    def solution1(self):  # O(1)
        return self.a * (self.r**self.n - 1) / (self.r - 1)


obj = Solution(1, 0.5, 3)
print(obj.solution(), obj.solution1())  # 1.5
obj = Solution(3, 5, 2)
print(obj.solution(), obj.solution1())  # 18
