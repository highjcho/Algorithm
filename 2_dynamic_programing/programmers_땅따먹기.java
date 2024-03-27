class Solution {
    int solution(int[][] land) {
        int len = land.length - 1;
        
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < 4; j++)
                land[i + 1][j] = Math.max(Math.max(land[i][(j + 1) % 4], land[i][(j + 2) % 4]),
                                          land[i][(j + 3) % 4]) + land[i + 1][j]; 
        }
        int tmp1 = Math.max(land[len][0], land[len][1]);
        int tmp2 = Math.max(land[len][2], land[len][3]);
        return tmp1 > tmp2 ? tmp1 : tmp2;
    }
}