"""
Given a string str, written in a camel case. Your task is to put one space after every word and convert uppercase letter to lowercase.
"""


def solution(cstr: str) -> None:
    result = ""
    for c in cstr:
        if c.isupper(): result += " " + c.lower()
        else: result += c
    result = result[1:]
    print(result)


in1 = "ThisIsAnAutomationEra"  # this is an automation era.
solution(in1)
in2 = "HeyYou"  # hey you
solution(in2)
