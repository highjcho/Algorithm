import java.util.*;

class Solution {
    int h;
    int w;
    int[][] visit;
    public int solution(int[][] maps) {
        Queue<int[]> q = new ArrayDeque<>();
        h = maps.length;
        w = maps[0].length;
        visit = new int[h][w];
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        q.add(new int[]{0, 0});
        visit[0][0] = 1;
        visit[h - 1][w - 1] = -1;
        while (!q.isEmpty()) {
            int[] now = q.poll();
            int cx = now[0], cy = now[1];
            if (cx == h - 1 && cy == w - 1)
                break;
            for (int d = 0; d < 4; d++) {
                int nx = cx + dx[d];
                int ny = cy + dy[d];
                if (isPossible(nx, ny) && maps[nx][ny] == 1) {
                    q.add(new int[]{nx, ny});
                    visit[nx][ny] = visit[cx][cy] + 1;
                }
            }
        }
        return visit[h - 1][w - 1];
    }
    
    private boolean isPossible(int x, int y) {
        if (0 <= x && x < h && 0 <= y && y < w && visit[x][y] <= 0)
            return true;
        return false;
    }
}