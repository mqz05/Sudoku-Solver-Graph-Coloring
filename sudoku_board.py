from sudoku_connections import SudokuConnections

class SudokuBoard : 
    def __init__(self, value =9) :
        
        self.value = value

        self.board = self.getBoard()

        self.sudokuGraph = SudokuConnections(value=value)
        self.mappedGrid = self.__getMappedMatrix()

    def __getMappedMatrix(self) : 
        matrix = [[0 for cols in range(self.value)] 
        for rows in range(self.value)]

        count = 1
        for rows in range(self.value) : 
            for cols in range(self.value):
                matrix[rows][cols] = count
                count+=1
        return matrix

    def getBoard(self) : 

        board = []
							
        if self.value == 9:
            board = [
                [0,0,0, 0,0,0, 0,8,2],
                [6,0,0, 4,0,0, 0,0,0],
                [0,0,0, 0,0,0, 0,0,0],
                
                [4,0,0, 0,7,2, 0,0,0],
                [5,0,0, 0,0,0, 4,3,0],
                [0,0,0, 0,1,0, 0,0,0],

                [0,0,0, 8,0,0, 6,0,0],
                [0,8,1, 0,0,0, 0,0,0],
                [0,2,0, 0,0,0, 0,0,7]
            ]

            #    [8,0,0, 6,0,0, 4,0,0],
            #    [0,2,0, 0,9,0, 0,6,0],
            #    [3,0,0, 0,0,0, 8,0,0],
            #    
            #    [4,0,0, 0,0,0, 9,0,0],
            #    [0,7,0, 0,3,0, 0,5,0],
            #    [0,0,9, 0,0,0, 0,0,8],
            #
            #    [0,0,5, 0,0,0, 0,0,3],
            #    [0,1,0, 0,2,0, 0,9,0],
            #    [0,0,3, 0,0,1, 0,0,4]

        elif self.value == 4:
            board = [
                [1, 3, 2, 4],
                [4, 2, 0, 0],  
                [2, 4, 0, 0],
                [3, 1, 4, 2]
            ]
        
        return board
        
    def graphColoringInitializeColor(self):
        
        color = [0] * (self.sudokuGraph.graph.totalV+1)
        given = [] 
        for row in range(len(self.board)) : 
            for col in range(len(self.board[row])) : 
                if self.board[row][col] != 0 : 
                    
                    idx = self.mappedGrid[row][col]

                    color[idx] = self.board[row][col]
                    given.append(idx)
        return color, given

    def solveGraphColoring(self, m) : 
        
        color, given = self.graphColoringInitializeColor()
        if self.__graphColorUtility(m =m, color=color, v =1, given=given) is None :
            return False
        count = 1
        for row in range(self.value) : 
            for col in range(self.value) :
                self.board[row][col] = color[count]
                count += 1
        return color
    
    def __graphColorUtility(self, m, color, v, given) :
        
        if v == self.sudokuGraph.graph.totalV+1  : 
            return True
        for c in range(1, m+1) : 
            if self.__isSafe2Color(v, color, c, given) == True :
                color[v] = c
                if self.__graphColorUtility(m, color, v+1, given) : 
                    return True
            if v not in given : 
                color[v] = 0

    def __isSafe2Color(self, v, color, c, given) : 
        
        if v in given and color[v] == c: 
            return True
        elif v in given : 
            return False

        for i in range(1, self.sudokuGraph.graph.totalV+1) :
            if color[i] == c and self.sudokuGraph.graph.isNeighbour(v, i, value=self.value) :
                return False
        return True