import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        Queue<Integer> pq = new PriorityQueue<>();
        for (int s: scoville)
            pq.add(s);
        int cnt = 0;
        while (pq.peek() < K && pq.size() > 1) {
            int f1 = pq.poll();
            int f2 = pq.poll();
            pq.add(f1 + (f2 * 2));
            cnt++;
        }
        if (pq.peek() < K)
            return -1;
        return cnt;
    }
}