import java.util.*;

class Solution {
    public int solution(int[] elements) {
        Set<Integer> answer = new HashSet<>();
        int len = elements.length;
        for (int i = 0; i < len; i++) {
            // for (int j = 1; j <= len; j++) {
                // int tmp = 0;
                // int l = i;
                // for (int k = 1; k <= j; k++) {
                //     tmp += elements[l % len];
                //     l++;
                // }
                // answer.add(tmp);
            int tmp = 0;
            for (int j = 0; j < len; j++) {
                tmp += elements[(i + j) % len];
                answer.add(tmp);
            }
        }
        return answer.size();
    }
}

class Solution {
    public int solution(int[] elements) {
        Set<Integer> answer = new HashSet<>();
        int len = elements.length;

        for (int i = 0; i < len; i++) {
            final int start = i;
            answer.add(IntStream.range(0, len)
                    .map(j -> elements[(start + j) % len])
                    .sum());
        }

        return answer.size();
    }
}