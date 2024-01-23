import java.util.*;

class Solution {
    public int solution(int n, int k, int[] enemy) {
        int answer = 0;
        int len = enemy.length;
        PriorityQueue<Integer> e_max = new PriorityQueue<>((x, y) -> y - x);
        if (k >= len)
            return len;
        int i;
        for (i = 0; i < len; i++) {
            if (k == 0 && n < enemy[i])
                break;
            e_max.add(enemy[i]);
            if (n < enemy[i]) {
                k--;
                n += e_max.poll();
            }
            n -= enemy[i];
        }
        return i;
    }
}