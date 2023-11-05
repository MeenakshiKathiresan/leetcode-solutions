class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        else:
            win_count = 0
            prev_winner = arr[0]
            
            for i, n in enumerate(arr[:-1]):
                
                if max(prev_winner, arr[i+1]) == prev_winner:
                    win_count += 1
                else:
                    win_count = 1
                
                prev_winner = max(prev_winner, arr[i+1])
                if win_count == k:
                    return prev_winner
        return max(arr)
                
                    
                
                