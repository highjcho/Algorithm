import java.util.*;

class Solution {
    public static Map<String, Integer> menu = new HashMap<>();
    
    public String[] solution(String[] orders, int[] course) {
        List<String> answer = new ArrayList<>();
        
        for (int i = 0; i < orders.length; i++) {
            char[] arr = orders[i].toCharArray();
            Arrays.sort(arr);
            orders[i] = String.valueOf(arr);
        }
    
        for (int len : course) {
            for (String order : orders)
                comb(order, "", 0, len);
            int max = 0;
            if (!menu.isEmpty())
                max = Collections.max(menu.values());
            if (max < 2)
                continue;
            for (Map.Entry<String, Integer> entry : menu.entrySet()) {
                if (entry.getValue() == max)
                    answer.add(entry.getKey());
            }
            menu.clear();
        }
        
        return answer.stream().sorted().toArray(String[]::new);
    }
    
    public static void comb(String order, String s, int start, int len) {
        if (len == 0) {
            menu.put(s, menu.getOrDefault(s, 0) + 1);
            return;
        }
        for (int i = start; i < order.length(); i++) {
            comb(order, s + order.charAt(i), i + 1, len - 1);
        }
    }
}