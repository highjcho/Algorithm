class Solution {
    public int[] solution(String S, int[] P, int[] Q) {
        int s_len = S.length(), len = P.length;
        int[][] dp = new int[3][s_len];
        int[] ans = new int[len];
        for (int i = 0; i < s_len; i++) {
            char c = S.charAt(i);
            int prev = i == 0? 0 : i - 1;
            if (c == 'A') {
                dp[0][i] = dp[0][prev] + 1;
                dp[1][i] = dp[1][prev];
                dp[2][i] = dp[2][prev];
            } else if (c == 'C') {
                dp[0][i] = dp[0][prev];
                dp[1][i] = dp[1][prev] + 1;
                dp[2][i] = dp[2][prev];
            } else if (c == 'G') {
                dp[0][i] = dp[0][prev];
                dp[1][i] = dp[1][prev];
                dp[2][i] = dp[2][prev] + 1;
            } else {
                dp[0][i] = dp[0][prev];
                dp[1][i] = dp[1][prev];
                dp[2][i] = dp[2][prev];
            }
        }
        
        for (int i = 0; i < len; i++) {
            int j = -1;
            while (++j < 3) {
                int comp = P[i] == 0 ? 0 : dp[j][P[i] - 1];
                if (comp < dp[j][Q[i]])
                    break;
            }
            ans[i] = j + 1;
        }
        return ans;
    }
}