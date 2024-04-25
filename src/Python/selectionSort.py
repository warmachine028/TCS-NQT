def selectionSort(arr: list[int]):
    for i in range(len(arr)):
        idx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]

A = [2, 1, 4, 3, -1]
selectionSort(A)
print(A)
