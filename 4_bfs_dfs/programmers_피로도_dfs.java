import java.util.*;

class Solution {
    int[][] copy;
    int len;
    int max = 0;
    boolean[] visit;
    public int solution(int k, int[][] dungeons) {
        copy = dungeons;
        len = copy.length;
        visit = new boolean[len];
        dfs(k, 0, 0);
        return max;
    }
    
    public void dfs(int k, int cnt, int d) {
        max = cnt > max ? cnt : max;
        if (d == len || max == len)
            return ;
        for (int i = 0; i < len; i++) {
            if (!visit[i] && k >= copy[i][0]) {
                visit[i] = true;
                dfs(k - copy[i][1], cnt + 1, d + 1); 
                visit[i] = false;
            }
        }
    }
}