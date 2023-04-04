class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        high = max(damage)
        if high > armor:
            reduce = armor
        else:
            reduce =  high
            
        return sum(damage) - reduce + 1