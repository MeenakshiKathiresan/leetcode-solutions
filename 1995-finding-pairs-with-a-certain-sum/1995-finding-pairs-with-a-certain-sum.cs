public class FindSumPairs {
    private int[] nums1;
    private int[] nums2;
    private Dictionary<int, int> freq1 = new();
    private Dictionary<int, int> freq2 = new();

    public FindSumPairs(int[] n1, int[] n2) {
        nums1 = n1;
        nums2 = n2;

        foreach (int num in nums1) {
            if (!freq1.ContainsKey(num))
                freq1[num] = 0;
            freq1[num]++;
        }

        foreach (int num in nums2) {
            if (!freq2.ContainsKey(num))
                freq2[num] = 0;
            freq2[num]++;
        }
    }

    public void Add(int index, int val) {
        int oldVal = nums2[index];
        int newVal = oldVal + val;

        freq2[oldVal]--;
        if (freq2[oldVal] == 0)
            freq2.Remove(oldVal);

        if (!freq2.ContainsKey(newVal))
            freq2[newVal] = 0;
        freq2[newVal]++;

        nums2[index] = newVal;
    }

    public int Count(int tot) {
        int res = 0;

        foreach (var kvp in freq1) {
            int a = kvp.Key;
            int freqA = kvp.Value;
            int b = tot - a;

            if (freq2.ContainsKey(b)) {
                res += freqA * freq2[b];
            }
        }

        return res;
    }
}
