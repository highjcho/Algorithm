class Solution {
    public int solution(int[] H) {
        Stack<Integer> s = new Stack<>();
        int ans = 0;
        for (int i = 1; i < H.length; ++i) {
            if (s.isEmpty() || s.peek() < H[i]) {
                ans++;
                s.add(H[i]);
            }
            else if (s.peek() > H[i]) {
                s.pop();
                i--;
            }
        }
        return ans;
    }
}