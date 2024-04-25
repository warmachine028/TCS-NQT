def shiftBoxes(boxes):
    count = 0
    for i in range(len(boxes)):
        if boxes[i] != 0:
            boxes[count] = boxes[i]
            count += 1
    while count < len(boxes):
        boxes[count] = 0
        count += 1


def main():
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    shiftBoxes(arr)
    print(arr)

main()