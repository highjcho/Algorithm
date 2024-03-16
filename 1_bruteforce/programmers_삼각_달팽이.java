import java.util.*;

class Solution {
    public int[] solution(int n) {
        int[][] tmp = new int[n][];
        for (int i = 0; i < n; i++)
            tmp[i] = new int[i + 1];
        int cnt = 1, last = (n * (1 + n)) / 2, i = 0, j = 0; 
        while (cnt <= last) {
            while (i < n && tmp[i][j] == 0)
                tmp[i++][j] = cnt++;
            
            i--;
            j++;
            
            while (j < n && tmp[i][j] == 0)
                tmp[i][j++] = cnt++;
            
            i--;
            j -= 2;
            
            while (i > 0 && tmp[i][j] == 0)
                tmp[i--][j--] = cnt++;
            
            i += 2;
            j++;
        }
        return Arrays.stream(tmp).flatMapToInt(Arrays::stream).toArray();
    }
}