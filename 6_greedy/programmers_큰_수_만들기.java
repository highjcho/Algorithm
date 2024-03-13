class Solution {
    public String solution(String number, int k) {
        String answer = "";
        int i = 0, pick = 0, cnt = 0, l = k, len = number.length(), n = len - k;
        
        
        while (i < l && cnt != n) {
            char max = 0;
            while (i <= l) {
                char now = number.charAt(i);
                if (now > max) {
                    max = now;
                    pick = i;
                }
                i++;
            }
            answer += max;
            cnt++;
            i = pick + 1;
            l = len > l + 1 ? l + 1 : l;
        }
        if (cnt != n)
            answer += number.substring(i, len);
        return answer;
    }
}

import java.util.Stack;

class Solution {
    public String solution(String number, int k) {
        String answer = "";
        Stack<Character> stack = new Stack<>();
        int i = -1, len = number.length(), ans_l = len - k;
        while (++i < len) {
            if (k < 0 && ans_l - stack.size() == len - i)
                break;
            char c = number.charAt(i);
            while (!stack.isEmpty() && stack.peek() < c && k-- > 0)
                stack.pop();
            if (stack.size() < ans_l)
                stack.push(c);
        }
        for (int j = 0; j < stack.size(); j++)
            answer += stack.get(j);
        if (answer.length() != ans_l)
            answer += number.substring(i, len);
        return answer;
    }
}