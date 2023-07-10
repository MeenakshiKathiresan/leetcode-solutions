import math

class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        arr.sort()
        
        pairs = {}
        mod = 10**9 + 7
        
        for n in arr:
            pairs[n] = 1
            
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0 and arr[i] // arr[j] in pairs:
                    pairs[arr[i]] += pairs[arr[j]] * pairs[arr[i] // arr[j]]
                    pairs[arr[i]] %= mod
        
        return sum(pairs.values()) % mod
