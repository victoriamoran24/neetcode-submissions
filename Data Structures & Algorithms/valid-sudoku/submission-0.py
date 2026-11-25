class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]

        def find_square(row, col): 
            if row <= 2: 
                if col <= 2: 
                    return 0
                elif col <= 5: 
                    return 1
                else: 
                    return 2
            elif row <= 5: 
                if col <= 2: 
                    return 3
                elif col <= 5: 
                    return 4
                else: 
                    return 5
            else: 
                if col <= 2: 
                    return 6
                elif col <= 5: 
                    return 7
                else: 
                    return 8


        for r in range(9): 
            for c in range(9): 
                num = board[r][c]
                if num == ".":
                    continue
                square = find_square(r, c)
                if num in rows[r] or num in cols[c] or num in squares[square]: 
                    return False
                    
                rows[r].add(num)
                cols[c].add(num)
                squares[square].add(num)

        return True


        