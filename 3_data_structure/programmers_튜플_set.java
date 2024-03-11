import java.util.*;

class Solution {
    public int[] solution(String s) {
        String[] tuple = s.replaceAll("\\{\\{|\\}\\}", "").split("},\\{");
        Arrays.sort(tuple, (s1, s2) -> s1.length() - s2.length());
        int len = tuple.length;
        int[] answer = new int[len];
        Set<String> set = new HashSet<>();
        for (int i = 0; i < len; i++) {
            String[] elem = tuple[i].split(",");
            for (String e : elem) {
                if (set.add(e)) {
                    answer[i] = Integer.parseInt(e);
                    break;
                }
            }
        }
        return answer;
    }
}