class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = [set() for _ in range(9)]
        colset = [set() for _ in range(9)]
        gridset = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                gridno = (i//3) * 3 + (j//3)
                ispresinrow = board[i][j] in rowset[i]
                ispresentincol = board[i][j] in colset[j]
                ispresentingrid = board[i][j] in gridset[gridno]

                if ispresinrow or ispresentincol or ispresentingrid:
                    return False

                rowset[i].add(board[i][j])
                colset[j].add(board[i][j])
                gridset[gridno].add(board[i][j])
        return True
