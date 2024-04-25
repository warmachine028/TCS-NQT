/*
Considerthe peiow series:
1,2,1,3,2,5,3,7,5,11,8,13,13,17,
This series is a mixture of 2 series fail the odd terms in this series form a 
Fibonacci series and all the even terms are the prime numbers in ascending 
order
Write a program to find the Nth term in this series
The value N in a positive integer that should be read from mm. The Nth term 
that is calculated by the program should be written to STDOUT Otherthan the 
value of Nth term , no other characters / string or message should be written to 
STDOUT.
For example, when N:14, the 14th term in the series is 17 So only the value 17 
should be printed to STDOUT
Solution –

 */

import java.util.Scanner;

public class Series {
    static int prime(int n) {
        int prime = 0;
        for (int i = 2; n > 0; i++) {
            boolean flag = true;
            for (int j = 2; j <= i / 2; j++)
                if (i % j == 0) {
                    flag = false;
                    break;
                }
            if (flag) {
                n--;
                prime = i;
            }
        }
        return prime;
    }

    static int fib(int n) {
        return n <= 2 ? 1 : fib(n - 1) + fib(n - 2);
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            for (int i = 1; i <= n; i++) {
                int result;
                result = i % 2 > 0 ? fib((i + 1) / 2) : prime(i / 2);
                System.out.print(result + ", ");
            }
        }
    }
}