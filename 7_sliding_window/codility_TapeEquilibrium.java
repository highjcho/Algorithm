import java.util.*;

class Solution {
    public int solution(int[] A) {
        int len = A.length;
        int first = 0, ans = 2147483647;
        int second = Arrays.stream(A).sum();

        for (int i = 0; i < len - 1; i++) {
            first += A[i];
            second -= A[i];
            ans = getMin(first - second, ans);
        }
        return ans;
    }

    public int getMin(int a, int b) {
        a = a > 0 ? a : a * -1;
        return a < b ? a : b;
    }
}