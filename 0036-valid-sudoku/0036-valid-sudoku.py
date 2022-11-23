class Solution(object):
    def isValidSudoku(self, board):
        def valid():
            for line in board:                     
                line = list(filter(lambda x: x.isdigit(), line))
                if len(line) != len(set(line)): return False
            return True
        if not valid(): 
            return False
        board = list(chain(zip(*board)))
        if not valid(): 
            return False

        board = [list(chain(*[board[i  ][j:j+3],
                              board[i+1][j:j+3],
                              board[i+2][j:j+3]]))
                 for i in [0,3,6] for j in [0,3,6]] 
        if not valid(): 
            return False                                
        return True
