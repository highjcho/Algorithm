import java.util.*;

class Solution {
    static class Tired {
        int dia;
        int iron;
        int stone;
        
        public Tired(int dia, int iron, int stone) {
            this.dia = dia;
            this.iron = iron;
            this.stone = stone;
        }
    }

    public int solution(int[] picks, String[] minerals) {
        int totalPicks = Arrays.stream(picks).sum();
        int answer = 0;
        List<Tired> tireds = new ArrayList<>();
        int len = minerals.length;
        int i = 0;
        while (i < len && totalPicks > 0) {
            int j = i, dia = 0, iron = 0, stone = 0;
            while (j < len && j < i + 5) {
                String m = minerals[j++];
                dia += 1;
                if (m.equals("diamond")) {
                    iron += 5;
                    stone += 25;
                } else {
                    iron += 1;
                    stone = m.equals("iron") ? stone + 5 : stone + 1;
                }
            }
            i += 5;
            totalPicks--;
            tireds.add(new Tired(dia, iron, stone));
        }
        Collections.sort(tireds, ((o1, o2) -> o2.stone - o1.stone));
        for (Tired t : tireds) {
            if (picks[0] > 0) {
                answer += t.dia;
                picks[0]--;
            } else if (picks[1] > 0) {
                answer += t.iron;
                picks[1]--;
            } else {
                answer += t.stone;
            }
        }
        return answer;
    }
}