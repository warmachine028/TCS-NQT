"""
A car co. has recorded its profit or loss (a[i]) for the next N days. The company wants to rearrange the order of these
records in such a way that the overall income is never equal to zero.

The rearranged values should be in non-increasing order.

If such a rearrangement is'nt possible print "IMPOSSIBLE" else print "POSSIBLE" along with the rearranged values for the N days.

INP

7
2 3 1 4 5 -9 8

"""

def solution(incomes: list[int]) -> None:
    if (sum(incomes) <= 0): return print("Impossible")

    print("Possible")
    print(sorted(incomes, reverse=True))

n = int("7")
income1 = list(map(int, "2 3 1 4 5 -9 8".split()))
solution(income1)
