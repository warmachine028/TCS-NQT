import java.util.Arrays;
import java.util.Scanner;

public class SelectionSort {
    static void selectionSort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int min = i;
            for (int j = i; j < arr.length; j++)
                if (arr[j] < arr[min])
                    min = j;

            if (min == i)
                continue;

            arr[i] = arr[i] ^ arr[min];
            arr[min] = arr[i] ^ arr[min];
            arr[i] = arr[i] ^ arr[min];
        }
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            sc.nextLine();
            args = sc.nextLine().split(" ");
            int[] arr = new int[n];
            for (int i = 0; i < n; i++)
                arr[i] = Integer.parseInt(args[i]);
            selectionSort(arr);
            System.out.println(Arrays.toString(arr));
        }
    }
}
