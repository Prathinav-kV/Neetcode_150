# Valid Sudoku
# You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

# Example 1:
    
# Input: board = 
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: true
# Example = 2
  
# Input: board = 
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: false

# Explanation: There are two 1's in the top-left 3x3 sub-box.

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            count = {}
            for j in i:
                if j != '.':
                    count[j] = 1 + count.get(j,0)

            if any( u > 1 for u in count.values()):
                return False 
        
        for i in range(9):
            count = {}
            for j in range(9):
                if board[j][i] != '.':
                    count[board[j][i]] = 1 + count.get(board[j][i],0)
            
            if any( u > 1 for u in count.values()):
                return False 

        counter = [[0,1,2],[3,4,5],[6,7,8]]

        for i in counter:
            for j in counter:
                d = {}
                for k in i:
                    for l in j:
                        if board[k][l] != '.':
                            d[board[k][l]] = 1 + d.get(board[k][l],0)

                if any(x > 1 for x in d.values()):
                    return False

        return True
