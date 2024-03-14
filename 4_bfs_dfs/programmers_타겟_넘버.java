import java.util.*;

// dfs
class Solution {
    int[] nums;
    int answer = 0;
    int len;
    
    public int solution(int[] numbers, int target) {
        nums = numbers;
        len = nums.length;
        dfs(0, 0, target);
        return answer;  
    }
    
    public void dfs(int i, int sum, int t) {
        if (i == len) {
            answer = sum == t ? answer + 1 : answer;
            return ;
        }
        dfs(i + 1, sum + nums[i], t);
        dfs(i + 1, sum - nums[i], t);
    }
}

// bfs
import java.util.*;

class Solution {
    static class Sum {
        int sum;
        int idx;
        public Sum(int sum, int idx) {
            this.sum = sum;
            this.idx = idx;
        }
    }
    
    public int solution(int[] numbers, int target) {
        int len = numbers.length;
		int answer = 0;
        Queue<Sum> q = new ArrayDeque<>();
        q.add(new Sum(numbers[0], 0));
        q.add(new Sum(-numbers[0], 0));
        
        while (!q.isEmpty()) {
            Sum n = q.poll();
            int idx = n.idx + 1;
            if (idx < len) {
                q.add(new Sum(n.sum + numbers[idx], idx));
                q.add(new Sum(n.sum - numbers[idx], idx));
            } else {
                if (n.sum == target)
                    answer += 1;
            }
        }
        return answer;  
    }
}