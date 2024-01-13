import java.util.*;

class Solution {
    public int solution(String[][] book_time) {
        Arrays.sort(book_time, (x, y) -> x[0].compareTo(y[0]));
        PriorityQueue<int[]> room = new PriorityQueue<>((x, y) -> x[1] - y[1]);
        
        for (String[] book : book_time) {
            String[] start = book[0].split(":");
            String[] end = book[1].split(":");
            
            int s_time = Integer.parseInt(start[0]) * 60 + Integer.parseInt(start[1]);
            int e_time = Integer.parseInt(end[0]) * 60 + Integer.parseInt(end[1]) + 10;
            
            if (!room.isEmpty() && room.peek()[1] <= s_time)
                room.poll();
            room.add(new int[]{s_time, e_time});
        }
        return room.size();
    }
}

class Solution {
    public int solution(String[][] book_time) {
        int j;
        Arrays.sort(book_time, (x, y) -> x[0].compareTo(y[0]));
        Map<Integer, Integer> room = new HashMap<>();
        
		for (int i = 0; i < book_time.length; i++) {
            String[] start = book_time[i][0].split(":");
            String[] end = book_time[i][1].split(":");
            
            int s_time = Integer.parseInt(start[0]) * 60 + Integer.parseInt(start[1]);
            int e_time = Integer.parseInt(end[0]) * 60 + Integer.parseInt(end[1]) + 10;
            
            for (j = 1; j <= room.size(); j++) { // 이렇게 맵을 다 뒤지지 않도록 우선순위큐를 사용했어야 했다.
                if (room.get(j) <= s_time)
                    break;
            }
            room.put(j, e_time);
        }
        return room.size();
    }
}