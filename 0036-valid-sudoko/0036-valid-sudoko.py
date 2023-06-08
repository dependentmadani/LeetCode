def check_list_correct(line: List[str]) -> bool:
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                if (line[i] == line[j] and line[i] != '.'):
                    return True
        return False

class Solution:      
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check horizental line:
        for i in board:
            if (check_list_correct(i)):
                return False
        
        #check vertical line:
        for i in range(9):
            tmp = []
            for j in range(9):
                tmp.append(board[j][i])
            if (check_list_correct(tmp)):
                return False
        
        #check 3*3 box:
        for i in range(0, 9, 3):  # Iterate over rows of 3x3 boxes
            for j in range(0, 9, 3):  # Iterate over columns of 3x3 boxes
                box1 = [row[j:j+3] for row in board[i:i+3]]
                box = [item for sublist in box1 for item in sublist]
                if (check_list_correct(box)):
                    return False
        return True
