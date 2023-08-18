class Solution:

    def __init__(self, nums: List[int]):
        self.graph = {}
        
        for i, num in enumerate(nums):
            if num not in self.graph:
                self.graph[num] = []
                
            self.graph[num].append(i)
            

    def pick(self, target: int) -> int:
        return random.choice(self.graph[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)