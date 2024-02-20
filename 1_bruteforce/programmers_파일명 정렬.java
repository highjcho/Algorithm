class Solution {
    static class FileName {
        String head;
        int num;
        int idx;

        public FileName(String head, int num, int idx) {
            this.head = head;
            this.num = num;
            this.idx = idx;
        }

        public int getIdx() {
            return this.idx;
        }
    }
    
    public String[] solution(String[] files) {

        String[] answer = new String[files.length];
        List<FileName> tmp = new ArrayList<>();
        for (int i = 0; i < files.length; i++) {
            int j = -1;
            while (!(0 <= files[i].charAt(++j) - '0' && files[i].charAt(j) - '0' <= 9))
                continue;
            int k = j;
            while (k < files[i].length() && (0 <= files[i].charAt(k) - '0' && files[i].charAt(k++) - '0' <= 9))
                continue;
            tmp.add(new FileName(files[i].substring(0, j).toLowerCase(), Integer.parseInt(files[i].substring(j, k)), i));
        }
        Collections.sort(tmp, Comparator
                         .comparing((FileName o) -> o.head)
                  .thenComparingInt(o -> o.num)
                  .thenComparingInt(o -> o.idx));

        
        for (int i = 0; i < files.length; i++) {
            answer[i] = files[tmp.get(i).getIdx()];
        }
        
        return answer;
    }


}

import java.util.*;

class Solution {
    public String[] solution(String[] files) {
         Arrays.sort(files, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                int s1_i = -1, s2_i = -1;
                while (!(0 <= s1.charAt(++s1_i) - '0' && s1.charAt(s1_i) - '0' <= 9));
                while (!(0 <= s2.charAt(++s2_i) - '0' && s2.charAt(s2_i) - '0' <= 9));
                
                String head1 = s1.substring(0, s1_i).toLowerCase();
                String head2 = s2.substring(0, s2_i).toLowerCase();
                
                if (!head1.equals(head2))
                    return head1.compareTo(head2);
                
                int s1_j = s1_i, s2_j = s2_i;
                while (s1_j < s1.length() && (0 <= s1.charAt(s1_j) - '0' && s1.charAt(s1_j++) - '0' <= 9));
                while (s2_j < s2.length() && (0 <= s2.charAt(s2_j) - '0' && s2.charAt(s2_j++) - '0' <= 9));
                
                
                int num1 = Integer.parseInt(s1.substring(s1_i, s1_j));
                int num2 = Integer.parseInt(s2.substring(s2_i, s2_j));

                return num1 - num2;
            }
        });
        return files;   
    }
}

import java.util.*;
import java.util.regex.*;

class Solution {
    public String[] solution(String[] files) {
        Pattern p = Pattern.compile("([a-z\\s.-]+)([0-9]{1,5})");

        Arrays.sort(files, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                Matcher m1 = p.matcher(s1.toLowerCase());
                Matcher m2 = p.matcher(s2.toLowerCase());
                m1.find();
                m2.find();

                if(!m1.group(1).equals(m2.group(1))) {
                    return m1.group(1).compareTo(m2.group(1));
                } else {
                    return Integer.parseInt(m1.group(2)) - Integer.parseInt(m2.group(2));
                }
            }
        });

        return files;
    }
}
