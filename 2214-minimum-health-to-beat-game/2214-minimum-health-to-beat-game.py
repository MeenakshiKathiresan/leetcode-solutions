class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        # remove max below armor and sum the rest +1
        high = max(damage)
        if high > armor:
            reduce = armor
        else:
            reduce =  high
            
        print(reduce)
        return sum(damage) - reduce + 1