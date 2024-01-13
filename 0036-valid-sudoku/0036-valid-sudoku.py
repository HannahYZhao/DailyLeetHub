class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        rows = [[] for _ in range(9)]  # Lists to store numbers in each row
        cols = [[] for _ in range(9)]  # Lists to store numbers in each column
        subgrids = [[] for _ in range(9)]  # Lists to store numbers in each 3x3 subgrid

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num in digits:
                    # Check for duplicates in the current row
                    if num in rows[i]:
                        return False
                    rows[i].append(num)

                    # Check for duplicates in the current column
                    if num in cols[j]:
                        return False
                    cols[j].append(num)

                    # Check for duplicates in the current subgrid
                    subgrid_idx = (i // 3) * 3 + (j // 3)
                    if num in subgrids[subgrid_idx]:
                        return False
                    subgrids[subgrid_idx].append(num)

        return True
