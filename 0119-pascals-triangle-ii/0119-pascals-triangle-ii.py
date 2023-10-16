class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rows = []
        for index in range(rowIndex+1):
            rows.append([])
            for i in range(index+1):
                if i == 0 or i == index:
                    rows[index].append(1)
                else:
                    no = rows[index-1][i-1] + rows[index-1][i]
                    rows[index].append(no)
        return rows[-1]