class Solution:
    class Parent:
        def __init__(self, parent, index):
            self.parent = parent
            self.index = index

    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        hierarchy = {}

        for region in regions:
            for i, sub_region in enumerate(region):
                if i == 0:
                    if sub_region not in hierarchy:
                        hierarchy[sub_region] = Solution.Parent(None, 0)
                else:
                    hierarchy[sub_region] = Solution.Parent(region[0], hierarchy[region[0]].index + 1)

        index1 = hierarchy[region1].index
        index2 = hierarchy[region2].index

        while index1 > index2:
            region1 = hierarchy[region1].parent
            index1 -= 1

        while index2 > index1:
            region2 = hierarchy[region2].parent
            index2 -= 1

        while region1 != region2:
            region1 = hierarchy[region1].parent
            region2 = hierarchy[region2].parent

        return region1