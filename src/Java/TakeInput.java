
import java.util.Arrays;
import java.util.Scanner;

public class TakeInput {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            sc.nextLine();
            String arrS = sc.nextLine();
            int[] arr = new int[n];
            args = arrS.split(" ");
            for (int i = 0; i < n; i++)
                arr[i] = Integer.parseInt(args[i]);

            System.out.println(Arrays.toString(arr));
        }
    }
}
