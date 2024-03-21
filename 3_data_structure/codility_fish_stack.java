import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] A, int[] B) {
        Stack<Integer> stack = new Stack<>();
        int len = A.length;
        int cnt = len;
        for (int i = 0; i < len; i++) {
            if (B[i] == 1)
                stack.add(A[i]);
            else {
                while (!stack.isEmpty()) {
                    cnt--;
                    if (stack.peek() > A[i])
                        break;
                    stack.pop();
                }
            }
        }
        return cnt;
    }
}

