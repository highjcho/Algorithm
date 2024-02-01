import java.util.*;

class Solution {
    public int solution(int x, int y, int n) {
        int z = y + 1;
        int dp[] = new int[z];
        Arrays.fill(dp, z);
        dp[x] = 0;
        for (int i = x; i < z; i++) {
            if (dp[i] == z)
                continue;
            if (i * 2 < z)
                dp[i * 2] = Math.min(dp[i] + 1, dp[i * 2]);
            if (i * 3 < z)
                dp[i * 3] = Math.min(dp[i] + 1, dp[i * 3]);
            if (i + n < z)
                dp[i + n] = Math.min(dp[i] + 1, dp[i + n]);
        }
        return dp[y] != z ? dp[y] : -1;
    }
}