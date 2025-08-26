class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiagonal = -1
        bestArea = -1

        for length, width in dimensions:
            diagonal = math.sqrt(length**2 + width**2)

            area = length * width

            if diagonal > maxDiagonal:
                maxDiagonal = diagonal
                bestArea = area
            elif diagonal == maxDiagonal:
                bestArea = max(bestArea, area)

        return bestArea