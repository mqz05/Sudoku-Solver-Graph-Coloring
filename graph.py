
class Node: 
    
    def __init__(self, idx, data = 0) : 
        
        self.id = idx
        self.data = data
        self.connectedTo = dict()

    def addNeighbour(self, neighbour , weight = 0) :

        if neighbour.id not in self.connectedTo.keys() :  
            self.connectedTo[neighbour.id] = weight


    def setData(self, data) : 
        self.data = data 


    def getConnections(self) : 
        return self.connectedTo.keys()

    def getID(self) : 
        return self.id
    
    def getData(self) : 
        return self.data

    def getWeight(self, neighbour) : 
        return self.connectedTo[neighbour.id]

    def __str__(self) : 
        return str(self.data) + " Connected to : "+ \
         str([x.data for x in self.connectedTo])

class Graph : 

    totalV = 0 
    
    def __init__(self) : 
        
        self.allNodes = dict()

    def addNode(self, idx) : 
        
        if idx in self.allNodes : 
            return None
        
        Graph.totalV += 1
        node = Node(idx=idx)
        self.allNodes[idx] = node
        return node

    def addNodeData(self, idx, data) : 
        
        if idx in self.allNodes : 
            node = self.allNodes[idx]
            node.setData(data)
        else : 
            print("No ID to add the data.")

    def addEdge(self, src, dst, wt = 0) : 
        
        self.allNodes[src].addNeighbour(self.allNodes[dst], wt)
        self.allNodes[dst].addNeighbour(self.allNodes[src], wt)
    
    def isNeighbour(self, u, v, value) : 
        
        if u >=1 and u <= (value * value) and v >=1 and v<= (value * value) and u !=v : 
            if v in self.allNodes[u].getConnections() : 
                return True
        return False



    # getter
    def getNode(self, idx) : 
        if idx in self.allNodes : 
            return self.allNodes[idx]
        return None

    def getAllNodesIds(self): 
        return self.allNodes.keys()

    # methods
    def DFS(self, start) :
        
        # STACK
        visited = [False]*Graph.totalV

        if start in self.allNodes.keys() : 
            self.__DFSUtility(node_id = start, visited=visited) 
        else : 
            print("Start Node not found")

    def __DFSUtility(self, node_id, visited) : 
        visited = self.__setVisitedTrue(visited=visited, node_id=node_id)
        
        print(self.allNodes[node_id].getID(), end = " ")

        #Recursive Stack
        for i in self.allNodes[node_id].getConnections() : 
            if visited[self.allNodes[i].getID()] == False : 
                self.__DFSUtility(node_id = self.allNodes[i].getID(), 
                visited=visited)

    def BFS(self, start) : 
        
        #Queue
        visited = [False]*Graph.totalV

        if start in self.allNodes.keys() : 
            self.__BFSUtility(node_id = start, visited=visited) 
        else : 
            print("Start Node not found")

    def __BFSUtility(self, node_id, visited) :
        queue = []
        visited = self.__setVisitedTrue(visited=visited, node_id=node_id)

        queue.append(node_id)

        while queue != [] : 
            x = queue.pop(0) 
            #print
            print(self.allNodes[x].getID(), end = " ")

            for i in self.allNodes[x].getConnections() : 
                idx = self.allNodes[i].getID()
                if visited[idx]  == False : 
                    queue.append(idx)
                    visited = self.__setVisitedTrue(visited=visited,
                     node_id=idx)
        


    def __setVisitedTrue(self, visited, node_id) : 
       
        visited[node_id] = True
        return visited

