class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # max loss should be the last stop
        # if by the end, you are at negative, means you cant make a circle

        lowest = float('inf')
        lowest_ind = -1
        sum = 0
        for i in range(len(gas)):
            curr_exp = gas[i] - cost[i]
            sum += curr_exp

            if sum < lowest:
                lowest_ind = i
                lowest = sum
        
        return (lowest_ind + 1) % len(gas) if sum >= 0 else -1


