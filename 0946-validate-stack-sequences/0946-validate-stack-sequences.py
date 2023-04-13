class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        current = 0
        while pushed and popped and current < len(pushed):
            current = min(current, len(pushed) - 1)
            current = max(current, 0)
            if pushed[current] == popped[0]:
                pushed.pop(current)
                popped.pop(0)
                current -= 1
            else:
                current += 1
        return len(pushed) ==0