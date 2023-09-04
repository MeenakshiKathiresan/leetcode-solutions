from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        n = len(board)

        def convert_num_to_indices(num):
            num -= 1
            i = n - 1 - num // n
            j = num % n if i % 2 != n % 2 else n - 1 - num % n
            return i, j

        def convert_indices_to_num(i, j):
            num = (n - i - 1) * n
            num += j if i % 2 != n % 2 else n - 1 - j
            return num + 1

        def get_neighbors(curr):
            i, j = convert_num_to_indices(curr)
            neighbors = []
            for step in range(1, 7):
                next_num = curr + step
                if next_num <= n * n:
                    ni, nj = convert_num_to_indices(next_num)
                    if board[ni][nj] != -1:
                        next_num = board[ni][nj]
                    neighbors.append(next_num)
            return neighbors

        queue = deque([(1, 0)]) 
        visited = set()

        while queue:
            curr, steps = queue.popleft()
            if curr == n * n:
                return steps

            if curr in visited:
                continue

            visited.add(curr)

            for neighbor in get_neighbors(curr):
                queue.append((neighbor, steps + 1))

        return -1
