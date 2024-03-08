
import java.util.*;

class Solution {
    int h, w;
    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};

    public int solution(String[] board) {
        h = board.length;
        w = board[0].length();
        int[][] visit = new int[h][w];
        Queue<int[]> q = new ArrayDeque();

        for(int i = 0 ; i < h; ++i){
            String s = board[i];
            for(int j = 0 ; j < w; ++j){
                if(s.charAt(j) == 'R'){
                    q.add(new int[]{i, j});
                    visit[i][j] = 1;
                    break;
                }
            }
        }

        int answer = -1;
        while(!q.isEmpty()) {
            int[] cur = q.poll();
            int c_x = cur[0];
            int c_y = cur[1];
            if(board[c_x].charAt(c_y) == 'G') {
                answer = visit[c_x][c_y] - 1;
                break;
            }

            for(int d = 0; d < 4; ++d){
                int n_x = c_x + dx[d];
                int n_y = c_y + dy[d];
                while (true){
                    if(isPossible(n_x, n_y) && board[n_x].charAt(n_y) != 'D') {
                        n_x += dx[d];
                        n_y += dy[d];
                    } else {
                        n_x -= dx[d];
                        n_y -= dy[d];
                        break;
                    }
                }

                if(visit[n_x][n_y] == 0){
                    q.add(new int[]{n_x, n_y});
                    visit[n_x][n_y] = visit[c_x][c_y] + 1;
                }
            }
        }

        return answer;
    }

    public boolean isPossible(int x, int y) {
        if(0 <= x && x < h && 0 <= y && y < w)
            return true;
        return false;
    }
}