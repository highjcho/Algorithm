import java.util.*;

class Solution {
    Map<String, List<Integer>> map = new HashMap<>();
    
    public int[] solution(String[] info, String[] query) {
        int[] answer = new int[query.length];
        for (String i : info) {
            String[] applicant = i.split(" ");
            comb(applicant, "", 0);
        }
        
        for(String key : map.keySet())
            Collections.sort(map.get(key));
        
        for (int i = 0; i < query.length; i++) {
            query[i] = query[i].replaceAll(" and ", "");
            String[] c = query[i].split(" ");
            answer[i] = map.containsKey(c[0]) ? binSearch(c[0], Integer.parseInt(c[1])) : 0;
        }
        return answer;
    }
    
    public void comb(String[] applicant, String str, int cnt) {
        if (cnt == 4) {
            if (!map.containsKey(str))
                map.put(str, new ArrayList<Integer>());
            map.get(str).add(Integer.parseInt(applicant[4]));
            return;
        }
        comb(applicant, str + "-", cnt + 1);
        comb(applicant, str + applicant[cnt], cnt + 1);
    }

    public int binSearch(String k, int v) {
        List<Integer> list = map.get(k);
        int left = 0, right = list.size();
        while (left < right) {
            int mid = (left + right) / 2;
            if (v > list.get(mid))
                left = mid + 1;
            else
                right = mid;
        }
        return list.size() - left;
    }
}