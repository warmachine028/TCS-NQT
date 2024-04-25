def solution(string: str) -> str:
    result: str = ""
    for c in string:
        result += chr(ord(c) + 1) if c != "z" else "a"
    return result


print(solution("abcdxyz"))
