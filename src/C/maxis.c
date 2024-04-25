#include <stdio.h>

void findMax(int arr[], int low, int high, int *max1, int *max2) {
    if (low == high) {
        *max1 = arr[low], 
        *max2 = -1;
        return;
    }

    if (high - low == 1) {
        if (arr[low] > arr[high])
            *max1 = arr[low], 
            *max2 = arr[high];
        else
            *max1 = arr[high], 
            *max2 = arr[low];
        return;
    }

    int mid = (low + high) / 2;
    int leftMax1, leftMax2, rightMax1, rightMax2;

    // Recursively find maximum and second maximum in left half
    findMax(arr, low, mid, &leftMax1, &leftMax2);
    findMax(arr, mid + 1, high, &rightMax1, &rightMax2);

    if (leftMax1 > rightMax1)
        *max1 = leftMax1,
        *max2 = (leftMax2 > rightMax1) ? leftMax2 : rightMax1;

    else
        *max1 = rightMax1,
        *max2 = (rightMax2 > leftMax1) ? rightMax2 : leftMax1;
}


void main()
{
    int arr[] = {53, 111, 404, 515, 62, 20};
    int n = sizeof(arr) / sizeof(arr[0]);
    int max1, max2;

    findMax(arr, 0, n - 1, &max1, &max2);

    printf("First Maximum: %i\n", max1);
    printf("Second Maximum: %i\n", max2);
}
