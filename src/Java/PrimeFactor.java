import java.util.ArrayList;
import java.util.List;

public class PrimeFactor {
    static void solution(int n) {
        List<Integer> primeFactor = new ArrayList<>();

        for (int factor = 2; n > 1; factor++)
            for (; n % factor == 0; n /= factor)
                primeFactor.add(factor);
        System.out.println(primeFactor);
    }

    public static void main(String[] args) {
        solution(12);
        solution(16);
        solution(120);
        solution(120);
    }
}