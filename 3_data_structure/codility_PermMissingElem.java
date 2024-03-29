import java.util.*;

class Solution {
    public int solution(int[] A) {
        int len = A.length;

        if (len == 0)
            return 1;
        else if (len == 1)
            return A[0] != 1 ? 1 : 2;
        
        Arrays.sort(A);
        int left = 0, right = len - 1;

        while (left <= right) {
            int mid = (left + right) / 2;
            if (A[mid] != mid + 1)
                right = mid - 1;
            else
                left = mid + 1;
        }
        return left + 1;
    }
}

class Solution {
    public int solution(int[] A) {
        long n = A.length + 1;
        long sum = n * (n + 1) / 2;
        
        for (int i = 0; i < n - 1; i++)
            sum -= A[i];

        return (int) sum;
    }
}