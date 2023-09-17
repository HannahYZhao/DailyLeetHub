/**
 * Sort algorithm, specifically Kahn's algorithm to solve this problem
 */
class Solution {
    // Create an empty adjacency list to represent the directed graph. Each node in the graph represents a course, and the edges represent the prerequisites.
    public boolean canFinish(int n, int[][] prerequisites) {
        // Initialization
        List<Integer>[] adj = new List[n];
        // Keep track of the number of incoming edges to each course
        int[] indegree = new int[n];
        // Create an empty ans vector to store the toplogical order of the courses
        List<Integer> ans = new ArrayList<>();

        // Building the Graph
        for(int[] pair: prerequisites) {
            int course = pair[0];
            int prerequistite = pair[1];
            if(adj[prerequistite] == null) {
                adj[prerequistite] = new ArrayList<>();
            }
            adj[prerequistite].add(course);
            indegree[course]++;
        }
        
        // Performing Toplogical Sort using Kahn's Algorithm
        Queue<Integer> queue = new LinkedList<>();
        // Iterate over all the courses (0 to n-1) and enqueue the courses with an indegree of 0 into the queue.
        for(int i = 0; i < n; i++) {
            // These courses have no prerequisites and can be started immediately.
            if(indegree[i] == 0) {
                queue.offer(i);
            }
        }

        while(!queue.isEmpty()) {
            int current = queue.poll();
            ans.add(current);

            if(adj[current] != null) {
                for(int next: adj[current]) {
                    // Decrement the indegree of x by 1 since we are removing the prerequisite t
                    indegree[next]--;
                    // If the indegree of x becomes 0, enqueue x into the queue. This means that all the prerequisites of course x have been completed
                    if(indegree[next] == 0) {
                        queue.offer(next);
                    }
                }
            }
        }
        // Checking the result
        // If they are equal, it means that all the courses can be finished without any cyclic dependencies. Return true
        return ans.size() == n;
    }
}