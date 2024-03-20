import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] A) {
        Arrays.sort(A);
        int len = A.length;
        int max = A[len - 1] * A[len - 2] * A[len - 3];
        if (A[1] < 0) {
            int tmp = A[0] * A[1] * A[len - 1];
            max = tmp > max ? tmp : max;
        }
        return max;
    }
}