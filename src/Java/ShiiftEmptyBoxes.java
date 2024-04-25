import java.util.Arrays;
import java.util.Scanner;

public class ShiiftEmptyBoxes {
    static void shiftBoxes(int[] array) {
        int count = 0;
        for (int i = 0; i < array.length; i++)
            if (array[i] != 0) {
                array[count++] = array[i];
            }
        while (count < array.length)
            array[count++] = 0;
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int[] array = new int[n];
            for (int i = 0; i < n; i++)
                array[i] = sc.nextInt();
            shiftBoxes(array);
            System.out.println(Arrays.toString(array));
        }
    }
}