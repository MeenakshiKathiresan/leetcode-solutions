public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        Dictionary<int, int> freqMap = new Dictionary<int, int>();

        foreach(int num in nums){
            if(!freqMap.ContainsKey(num)){
                freqMap.Add(num, 0);
            }
            ++freqMap[num];
        }

        PriorityQueue<int, int> PQ = new PriorityQueue<int, int>();
        foreach(var kvp in freqMap){
            PQ.Enqueue(kvp.Key, kvp.Value);
            if (PQ.Count > k){
                PQ.Dequeue();
            }
        }

        return PQ.UnorderedItems.Select(el => el.Element).ToArray();
    }
}