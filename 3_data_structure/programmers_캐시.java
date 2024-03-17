import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        Set<String> cache = new HashSet<>();
        Queue<String> lru = new ArrayDeque<>();
 
        for (String city: cities) {
            city = city.toLowerCase();
            if (cache.contains(city)) {
                lru.remove(city);
                lru.add(city);
                answer += 1;
            } else {
                if (cacheSize != 0) {
                    if (cache.size() == cacheSize) {
                        String remove = lru.poll();
                        cache.remove(remove);
                    }
                    lru.add(city);
                    cache.add(city);     
                }
                answer += 5;
            }
        }
        return answer;
    }
}