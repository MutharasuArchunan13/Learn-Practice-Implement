from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not( len(board) == 9  or len(board[0]) == 9):
            print(len(board),len(board[0]))
            return False
        flag = False
        for row in range(8):
            #validate the row
            for value in board[row]:
                temp = []
                if str(value).isdigit():
                    
                    flag = (lambda value:True 
                            if value not  in board[row] and value <10 and value > 0 else False)
                    temp.append(int(value))
            if len(temp)== 0:
                flag = False
            #validate the column
            for index3 in range(8):
                value = board[row][index3]
                temp = []
                if str(value).isdigit():
                    
                    flag = (lambda value:True if value not in board[row] and value <10 and value > 0 else False )
                    temp.append(int(value))
        
        for value in range(len(board),3):
            for index in range(value,3):
                temp = []
                if str(board[0][index]).isdigit():
                    flag = (lambda value:True if value not in board[row] and value <10 and value > 0 else False )
                    temp.append(int(value))
            
            
        return flag


        
classobj = Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."],
                                     ["6",".",".","1","9","5",".",".","."],
                                     [".","9","8",".",".",".",".","6","."],
                                     ["8",".",".",".","6",".",".",".","3"],
                                     ["4",".",".","8",".","3",".",".","1"],
                                     ["7",".",".",".","2",".",".",".","6"],
                                     [".","6",".",".",".",".","2","8","."],
                                     [".",".",".","4","1","9",".",".","5"],
                                     [".",".",".",".","8",".",".","7","9"]])