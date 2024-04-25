#include <stdio.h>
#include <limits.h>

int findMax(int arr[], int low, int high) {
    if (low == high)
        return arr[low];

    if (high - low == 1)
        return (arr[low] > arr[high]) ? arr[low] : arr[high];
    
    int mid = (low + high) / 2;
    int leftMax = findMax(arr, low, mid);
    int rightMax = findMax(arr, mid + 1, high);
    return leftMax > rightMax ? leftMax : rightMax;
}

int findMin(int arr[], int low, int high) {
    if (low == high)
        return arr[low];
    
    if (high - low == 1)
        return (arr[low] < arr[high]) ? arr[low] : arr[high];

    int mid = (low + high) / 2;
    int leftMin = findMin(arr, low, mid);
    int rightMin = findMin(arr, mid + 1, high);
    return leftMin < rightMin ? leftMin : rightMin;
}

int findSecondMin(int arr[], int low, int high) {
    int min1 = findMin(arr, 0, high), min2 = INT_MAX;

    for (int i = low; i <= high; ++i)
        if (arr[i] != min1 && arr[i] < min2)
            min2 = arr[i];
    return min2;
}

void main() {
    int arr[] = {53, 111, 404, 515, 62, 20};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Maximum Number: %d\n", findMax(arr, 0, n - 1));
    printf("Second Minimum Number: %d\n", findSecondMin(arr, 0, n - 1));
}
