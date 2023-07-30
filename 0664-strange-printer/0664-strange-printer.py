class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        state = [[0] * n for _ in range(n)]

        for i in range(n):
            state[i][i] = 1

        for i in range(n - 1, -1, -1):
            for dist in range(1, n - i):
                j = dist + i
                if dist == 1:
                    state[i][j] = 1 if s[i] == s[j] else 2
                    continue

                state[i][j] = float('inf')
                for k in range(i, j):
                    tmp = state[i][k] + state[k + 1][j]
                    state[i][j] = min(state[i][j], tmp)

                if s[i] == s[j]:
                    state[i][j] -= 1

        return state[0][n - 1]