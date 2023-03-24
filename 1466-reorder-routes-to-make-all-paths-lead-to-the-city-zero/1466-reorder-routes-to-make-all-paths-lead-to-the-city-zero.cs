public class Solution {
    int count = 0;
    public void Dfs(int start, int parent, Dictionary<int, List<List<int>>> graph){
        
        if (!graph.ContainsKey(start)){
            return;
        }
        
        for (int i = 0; i < graph[start].Count; i++){
            int child = graph[start][i][0];
            int sign = graph[start][i][1];
            if (child != parent){
                count += sign;
                Dfs(child, start, graph);
            }
            
       
        }
        
    }
    public int MinReorder(int n, int[][] connections) {
        // destiny should be 0
        /*
        
        0: 1
        1: 3
        2: 3
        4: 0
        4: 5
        
        reverse {3, 1} 
        
        Whatever goes to reverse is correct
        
        correct {4}
        whatever comes out of correct is wrong
        
        
        */
        
        Dictionary<int, List<List<int>>> graph = new Dictionary<int, List<List<int>>>();
       
        
        for(int i = 0; i < connections.Length; i++){
            if (!graph.ContainsKey(connections[i][0])){
                graph.Add(connections[i][0], new List<List<int>>());
                
            }
            if (!graph.ContainsKey(connections[i][1])){
            graph.Add(connections[i][1], new List<List<int>>());
            }
            
            graph[connections[i][0]].Add(new List<int>{connections[i][1],1});
            graph[connections[i][1]].Add(new List<int>{connections[i][0],0});
            
        }
        
        Dfs(0,-1, graph);
        return count;
       
        
      
    }
}