class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bit2 = False

        for bit in bits[:-1]:
            if bit2:
                bit2 = False
                continue
            if bit == 1:
                bit2 = True
        return not bit2
                