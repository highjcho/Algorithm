public class Solution {
    public long solution(int[] weights) {

        Long answer = Long.valueOf(0);
        
        int[] w = new int[1001];
        int[] wd = new int[4001];

        for(int i = 0; i < weights.length; i++)
        {
            int d2 = weights[i]*2;
            int d3 = weights[i]*3;
            int d4 = weights[i]*4;

            answer += wd[d2];
            answer += wd[d3];
            answer += wd[d4];

            if(w[weights[i]] > 0)
                answer -= w[weights[i]] * 2;

            w[weights[i]]++;
            wd[d2]++;
            wd[d3]++;
            wd[d4]++;
        }
        return answer;
    }
}