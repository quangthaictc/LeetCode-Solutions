class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
    
        rows, cols = len(mat), len(mat[0])
        result = []
    
        for diag in range(rows + cols - 1):
            # Store elements on diagonal
            temp = []

            # Start row
            r = 0 if diag < cols else diag - cols + 1
            # Start column
            c = diag if diag < cols else cols - 1
        
            # Loop element diagonally
            while r < rows and c >= 0:
                temp.append(mat[r][c])
                r += 1
                c -= 1
        
            # If even => reverse
            if diag % 2 == 0:
                result.extend(temp[::-1])
            else:
                result.extend(temp)