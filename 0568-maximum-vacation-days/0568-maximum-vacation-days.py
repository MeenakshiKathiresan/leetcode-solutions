class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n = len(flights)
        k = len(days[0])
        dp = [[-1] * n for _ in range(k)]

        def getDays(week, city):
            if week == k:
                return 0

            if dp[week][city] != -1:
                return dp[week][city]

            max_vacation = 0

            for dest_city in range(n):
                if city == dest_city or flights[city][dest_city] == 1:
                    max_vacation = max(max_vacation, days[dest_city][week] + getDays(week + 1, dest_city))

            dp[week][city] = max_vacation
            return max_vacation

        return getDays(0, 0)
