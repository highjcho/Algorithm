import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        Map<String, Integer> bag = new HashMap<>();
        for (int i = 0; i < want.length; i++)
            bag.put(want[i], number[i]);
        for (int i = 0; i < 10; i++) {
			String obj = discount[i];
            if (bag.containsKey(obj))
                bag.put(obj, bag.get(obj) - 1);
        }
        if (Collections.max(bag.values()) <= 0)
            answer++;
        for (int i = 0, j = 10; j < discount.length; i++, j++) {
            String obj1 = discount[i], obj2 = discount[j];
            if (bag.containsKey(obj1))
                bag.put(obj1, bag.get(obj1) + 1);
            if (bag.containsKey(obj2))
                bag.put(obj2, bag.get(obj2) - 1);
            if (Collections.max(bag.values()) <= 0)
                answer++;
        }
        return answer;
    }
}