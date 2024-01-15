import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        Arrays.fill(answer, -1);
        Stack<Integer> idx = new Stack<>();
        
        for (int i = 0; i < numbers.length; i++) {
            while (!idx.empty() && numbers[idx.peek()] < numbers[i])
                answer[idx.pop()] = numbers[i];
            idx.push(i);
        }
        return answer;
    }
}