from math import sqrt
from graph import Graph

class SudokuConnections : 
    def __init__(self, value =9) : 

        self.graph = Graph() 

        self.value = value

        self.rows = value
        self.cols = value
        self.total_blocks = self.rows*self.cols 

        self.__generateGraph() 
        self.connectEdges() 

        self.allIds = self.graph.getAllNodesIds()

        

    def __generateGraph(self) : 
        for idx in range(1, self.total_blocks+1) : 
            _ = self.graph.addNode(idx)

    def connectEdges(self) : 
        
        matrix = self.__getGridMatrix()

        head_connections = dict() # head : connections

        for row in range(self.value) :
            for col in range(self.value) : 
                
                head = matrix[row][col] #id of the node
                connections = self.__whatToConnect(matrix, row, col)
                
                head_connections[head] = connections
        # connect all the edges

        self.__connectThose(head_connections=head_connections)
        
    def __connectThose(self, head_connections) : 
        for head in head_connections.keys() : #head is the start idx
            connections = head_connections[head]
            for key in connections :  #get list of all the connections
                for v in connections[key] : 
                    self.graph.addEdge(src=head, dst=v)

 
    def __whatToConnect(self, matrix, rows, cols) :
        connections = dict()

        row = []
        col = []
        block = []

        # ROWS
        for c in range(cols+1, self.value) : 
            row.append(matrix[rows][c])
        
        connections["rows"] = row

        # COLS 
        for r in range(rows+1, self.value):
            col.append(matrix[r][cols])
        
        connections["cols"] = col

        # BLOCKS 
        if rows%sqrt(self.value) == 0 : 

            if cols%sqrt(self.value) == 0 :

                if self.value == 9:
                    block.append(matrix[rows+1][cols+1])
                    block.append(matrix[rows+1][cols+2])
                    block.append(matrix[rows+2][cols+1])
                    block.append(matrix[rows+2][cols+2])

                elif self.value == 4:
                    block.append(matrix[rows+1][cols+1])

            elif cols%sqrt(self.value) == 1 :
                
                if self.value == 9:
                    block.append(matrix[rows+1][cols-1])
                    block.append(matrix[rows+1][cols+1])
                    block.append(matrix[rows+2][cols-1])
                    block.append(matrix[rows+2][cols+1])

                elif self.value == 4:
                    block.append(matrix[rows+1][cols-1])


            elif cols%sqrt(self.value) == 2 :
                
                block.append(matrix[rows+1][cols-2])
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+2][cols-2])
                block.append(matrix[rows+2][cols-1])

        elif rows%sqrt(self.value) == 1 :
            
            if cols%sqrt(self.value) == 0 :
                
                if self.value == 9:
                    block.append(matrix[rows-1][cols+1])
                    block.append(matrix[rows-1][cols+2])
                    block.append(matrix[rows+1][cols+1])
                    block.append(matrix[rows+1][cols+2])

                elif self.value == 4:
                    block.append(matrix[rows-1][cols+1])

            elif cols%sqrt(self.value) == 1 :
                
                if self.value == 9:
                    block.append(matrix[rows-1][cols-1])
                    block.append(matrix[rows-1][cols+1])
                    block.append(matrix[rows+1][cols-1])
                    block.append(matrix[rows+1][cols+1])

                elif self.value == 4:
                    block.append(matrix[rows-1][cols-1])
                
            elif cols%sqrt(self.value) == 2 :
                
                block.append(matrix[rows-1][cols-2])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows+1][cols-2])
                block.append(matrix[rows+1][cols-1])

        elif rows%sqrt(self.value) == 2 :
            
            if cols%sqrt(self.value) == 0 :
                
                block.append(matrix[rows-2][cols+1])
                block.append(matrix[rows-2][cols+2])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows-1][cols+2])

            elif cols%sqrt(self.value) == 1 :
                
                block.append(matrix[rows-2][cols-1])
                block.append(matrix[rows-2][cols+1])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows-1][cols+1])
                
            elif cols%sqrt(self.value) == 2 :
                
                block.append(matrix[rows-2][cols-2])
                block.append(matrix[rows-2][cols-1])
                block.append(matrix[rows-1][cols-2])
                block.append(matrix[rows-1][cols-1])
        
        connections["blocks"] = block
        return connections

    def __getGridMatrix(self) : 
        
        matrix = [[0 for cols in range(self.cols)] 
        for rows in range(self.rows)]

        count = 1
        for rows in range(self.value) :
            for cols in range(self.value):
                matrix[rows][cols] = count
                count+=1
        return matrix

