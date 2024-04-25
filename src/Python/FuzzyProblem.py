def solution(weight):
    if weight == 0: return 0
    if 1 <= weight <= 2000: return 25
    if 2001 <= weight <= 4000: return 35
    if 4001 <= weight <= 7000: return 45

def main():
    weight = int(input())
    if weight < 0: return print("INVALID INPUT")
    if weight > 7000: return print("OVERLOADED")
    print(f"Time Extimated: {solution(weight)} minuites")

if __name__ == "__main__": 
    main()
