def LCM(a, b):
    greater = max(a, b)  # 10
    lesser = min(a, b)  # 5
    for i in range(greater, a * b + 1, greater): 
        # 10, 51, 10
        if not i % lesser:
            return i

if __name__ == "__main__": 
    print(LCM(4,8))
    print(LCM(12, 2))
    print(LCM(5, 2))
    print(LCM(1, 2))
    print(LCM(144, 120))
    print(LCM(27, 9))
    print(LCM(LCM(3, 27), 5))