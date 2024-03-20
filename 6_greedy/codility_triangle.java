// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] A) {
        Arrays.sort(A);
        int len = A.length;

        for (int i = 0; i < len - 2; i++) {
            if (A[i] > A[i + 2] - A[i + 1])
                return 1;
        }
        return 0;
    }
}