from sudoku_board import SudokuBoard

import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.font_manager import FontProperties
import networkx as nx
import math
import time


#
# MARK: Datos del sudoku
#

sudoku_datos_iniciales_9x9 = SudokuBoard(value=9).getBoard()

sudoku_datos_solucion_9x9 = SudokuBoard(value=9)
start_time = time.time()
sudoku_datos_solucion_9x9.solveGraphColoring(m=9)
print("9x9: --- %s seconds ---" % (time.time() - start_time))



#
# MARK: Funciones
#

# Obtener datos iniciales
def get_initial_data(value, sudoku_type):

    sudoku = sudoku_datos_iniciales_9x9 if sudoku_type == "9x9" else sudoku_datos_iniciales_4x4

    colores_nodos = list()

    initial_values_positions_colors = dict()

    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                colores_nodos.append("gray")
            elif sudoku[i][j] == 1:
                colores_nodos.append("#32CBFF")
                initial_values_positions_colors[str(i) + ", " + str(j)] = "#32CBFF"
            elif sudoku[i][j] == 2:
                colores_nodos.append("#F18F01")
                initial_values_positions_colors[str(i) + ", " + str(j)] = "#F18F01"
            elif sudoku[i][j] == 3:
                colores_nodos.append("#89A1EF")
                initial_values_positions_colors[str(i) + ", " + str(j)] = "#89A1EF"
            elif sudoku[i][j] == 4:
                colores_nodos.append("#EF9CDA")
                initial_values_positions_colors[str(i) + ", " + str(j)] = "#EF9CDA"
            elif sudoku[i][j] == 5:
                colores_nodos.append("#A41623")
                initial_values_positions_colors[str(i) + ", " + str(j)] = "#A41623"
            elif sudoku[i][j] == 6:
                colores_nodos.append("#6AB547")
                initial_values_positions_colors[str(i) + ", " + str(j)] = "#6AB547"
            elif sudoku[i][j] == 7:
                colores_nodos.append("#EDD83D")
                initial_values_positions_colors[str(i) + ", " + str(j)] = "#EDD83D"
            elif sudoku[i][j] == 8:
                colores_nodos.append("#E76B74") 
                initial_values_positions_colors[str(i) + ", " + str(j)] = "#E76B74"
            elif sudoku[i][j] == 9:
                colores_nodos.append("#735CDD")
                initial_values_positions_colors[str(i) + ", " + str(j)] = "#735CDD"

    if value == "positions":
        return initial_values_positions_colors
    elif value == "color":
        return colores_nodos


# Obtener datos solución
def get_solution_data(value, sudoku_type):

    sudoku = sudoku_datos_solucion_9x9.board if sudoku_type == "9x9" else sudoku_datos_solucion_4x4.board

    colores_nodos = list()

    solution_values_positions_colors = dict()

    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                colores_nodos.append("gray")
            elif sudoku[i][j] == 1:
                colores_nodos.append("#32CBFF")
                solution_values_positions_colors[str(i) + ", " + str(j)] = "#32CBFF"
            elif sudoku[i][j] == 2:
                colores_nodos.append("#F18F01")
                solution_values_positions_colors[str(i) + ", " + str(j)] = "#F18F01"
            elif sudoku[i][j] == 3:
                colores_nodos.append("#89A1EF")
                solution_values_positions_colors[str(i) + ", " + str(j)] = "#89A1EF"
            elif sudoku[i][j] == 4:
                colores_nodos.append("#EF9CDA")
                solution_values_positions_colors[str(i) + ", " + str(j)] = "#EF9CDA"
            elif sudoku[i][j] == 5:
                colores_nodos.append("#A41623")
                solution_values_positions_colors[str(i) + ", " + str(j)] = "#A41623"
            elif sudoku[i][j] == 6:
                colores_nodos.append("#6AB547")
                solution_values_positions_colors[str(i) + ", " + str(j)] = "#6AB547"
            elif sudoku[i][j] == 7:
                colores_nodos.append("#EDD83D")
                solution_values_positions_colors[str(i) + ", " + str(j)] = "#EDD83D"
            elif sudoku[i][j] == 8:
                colores_nodos.append("#E76B74") 
                solution_values_positions_colors[str(i) + ", " + str(j)] = "#E76B74"
            elif sudoku[i][j] == 9:
                colores_nodos.append("#735CDD")
                solution_values_positions_colors[str(i) + ", " + str(j)] = "#735CDD"

    if value == "positions":
        return solution_values_positions_colors
    elif value == "color":
        return colores_nodos


# Crear sudoku completo
def set_up_sudoku_full(axis, valores_tabla, sudoku_type):

    # Reemplazando "0" por huecos vacios
    for i in range(len(valores_tabla)):
        for j, v in enumerate(valores_tabla[i]):
            if v == "0": 
                valores_tabla[i].pop(j)
                valores_tabla[i].insert(j, " ")
    

    # Representacion de la tabla
    sudoku = axis[0].table(
        colWidths=[.1] * len(valores_tabla),
        cellText = valores_tabla,
        cellLoc ='center',
        loc ='center'
    )


    # Ajustar parámetros custom
    initial_data = get_initial_data("positions", sudoku_type=sudoku_type)

    for (row, col), cell in sudoku.get_celld().items():
        
        # Ajustar los valores iniciales en negrita
        current_position = str(row) + ", " + str(col)
        
        if current_position in initial_data:
            cell.set_text_props(fontproperties=FontProperties(weight='heavy', size=16))
        else:
            cell.set_text_props(fontproperties=FontProperties(size=16))
        
        # Colores del fondo de las celdas
        if sudoku_type == "9x9":
            if (0 <= row <= 2) and (0 <= col <= 2):
                cell.set(facecolor="lightgray")
            elif (6 <= row <= 8) and (0 <= col <= 2):
                cell.set(facecolor="lightgray")
            elif (3 <= row <= 5) and (3 <= col <= 5):
                cell.set(facecolor="lightgray")
            elif (0 <= row <= 2) and (6 <= col <= 8):
                cell.set(facecolor="lightgray")
            elif (6 <= row <= 8) and (6 <= col <= 8):
                cell.set(facecolor="lightgray")
        
        elif sudoku_type == "4x4":
            if (0 <= row <= 1) and (0 <= col <= 1):
                cell.set(facecolor="lightgray")
            elif (2 <= row <= 3) and (2 <= col <= 3):
                cell.set(facecolor="lightgray")

    sudoku.scale(1.25, 2.25)

    # Título
    axis[0].set_title("Sudoku " + str(len(valores_tabla)) + "x" + str(len(valores_tabla)), fontsize=24, fontweight ="bold")
    

# Crear sudoku reducido
def set_up_sudoku_reducido(axis, color_values, valores_tabla, sudoku_type):
    
    # Modificando y añadiendo los ejes x e y (con numeros del 1..9)
    eje_x = [str(1), str(2), str(3), str(4), str(5), str(6), str(7), str(8), str(9)] if sudoku_type == "9x9" else [str(1), str(2), str(3), str(4)]
    valores_tabla.insert(0, eje_x)
    for i in range(len(valores_tabla)):
        valores_tabla[i].insert(0, str(i))

    # Reemplazando "0" por huecos vacios
    for i in range(len(valores_tabla)):
        for j, v in enumerate(valores_tabla[i]):
            if v == "0": 
                valores_tabla[i].pop(j)
                valores_tabla[i].insert(j, " ")

    # Representacion de la tabla
    sudoku = axis[0].table(
        colWidths=[.1] * len(valores_tabla),
        cellText = valores_tabla,
        cellLoc ='center',
        loc ='center'
    )

    # Ajustar parámetros custom
    initial_data = get_initial_data("positions", sudoku_type=sudoku_type)

    for (row, col), cell in sudoku.get_celld().items():

        # Quitar celdas de los numeros en los ejers x e y (1...9) & configurar los textos en negrita
        if row == 0 or col == 0:
            cell.visible_edges = "open"
            cell.set_text_props(fontproperties=FontProperties(size=16))
        

        # Ajustar los valores iniciales en negrita
        current_position = str(row - 1) + ", " + str(col -1)

        if current_position in initial_data:
            cell.set_text_props(fontproperties=FontProperties(weight='heavy', size=16))
        else:
            cell.set_text_props(fontproperties=FontProperties(size=16))

        # Colores del fondo de las celdas
        if sudoku_type == "9x9":
            if (1 <= row <= 3) and (1 <= col <= 3):
                cell.set(facecolor="lightgray")
            elif (7 <= row <= 9) and (1 <= col <= 3):
                cell.set(facecolor="lightgray")
            elif (4 <= row <= 6) and (4 <= col <= 6):
                cell.set(facecolor="lightgray")
            elif (1 <= row <= 3) and (7 <= col <= 9):
                cell.set(facecolor="lightgray")
            elif (7 <= row <= 9) and (7 <= col <= 9):
                cell.set(facecolor="lightgray")
        
        elif sudoku_type == "4x4":
            if (1 <= row <= 2) and (1 <= col <= 2):
                cell.set(facecolor="lightgray")
            elif (3 <= row <= 4) and (3 <= col <= 4):
                cell.set(facecolor="lightgray")

        # Colorear los valores con su respectivo color en el grafo
        for c in list(color_values.keys()):
            x, y = int(c[0]) + 1, int(c[3]) + 1

            if row == x and col == y:
                cell.get_text().set_color(color_values[c])
            

    sudoku.scale(1.75, 1.5)
    
    # Título
    axis[0].set_title("Sudoku " + str(len(valores_tabla)-1) + "x" + str(len(valores_tabla)-1), fontsize=22, fontweight ="heavy")
  


# Crear grafo
def set_up_grafo(axis, colores_nodos, tamaño_sudoku, tamaño_cuadrante):

    # Creación de la lista de nodos
    lista_nodos = list()
    
    # Crear la lista de nodos con las coords relativas a su posicion en el sudoku
    for i in range(tamaño_sudoku):
        for j in range(tamaño_sudoku):
            lista_nodos.append(str(i + 1) + ", " + str(j + 1))

    # Creación de la tabla
    # Ordenar los elementos
    lista_nodos = [lista_nodos[i:i+tamaño_sudoku] for i in range(0, len(lista_nodos), tamaño_sudoku)]

    # Creación del grafo
    grafo = nx.Graph()

    # Definir los nodos en el grafo
    for i in range(len(lista_nodos)):
        for j in range(len(lista_nodos[i])):
            grafo.add_node(lista_nodos[i][j])

    
    def calc_pos_x(nodo):
        for i in range(len(lista_nodos)):
            for j in range(len(lista_nodos[i])):
                if lista_nodos[i][j] == nodo:
                    return j

    def calc_pos_y(nodo):
        for i in range(len(lista_nodos)):
            for j in range(len(lista_nodos[i])):
                if lista_nodos[i][j] == nodo:
                    return i
    
    # Definir los vertices
    def calcularCuadrante(posicion):
        p = posicion + 1

        division_p = p/tamaño_cuadrante

        if p%tamaño_cuadrante == 0:
            return division_p

        elif math.ceil(division_p) == math.floor((division_p) + 1):
            return math.ceil(division_p)


      
    def comprobarConexionNodos(nodo):

        nodos_conectados = []

        for i in range(len(lista_nodos)):
            
            for j in range(len(lista_nodos[i])):
                nodo_comparacion = lista_nodos[i][j]

                nodo_eje_x = calc_pos_x(nodo=nodo)
                nodo_eje_y = calc_pos_y(nodo=nodo)

                nodo_comparacion_eje_x = calc_pos_x(nodo=nodo_comparacion)
                nodo_comparacion_eje_y = calc_pos_y(nodo=nodo_comparacion)

                if not nodo_comparacion == nodo:

                    # Si cumple la condicion 1 (mismo eje X)
                    if nodo_eje_x == nodo_comparacion_eje_x:
                        #print("ejeX. Nodo principal:" + str(nodo) + "||  Nodo comparacion:" + str(nodo_comparacion))
                        nodos_conectados.append(nodo_comparacion)
                        
                    # Si cumple la condicion 2 (mismo eje Y)
                    elif nodo_eje_y == nodo_comparacion_eje_y:
                        #print("ejeY. Nodo principal:" + str(nodo) + "||  Nodo comparacion:" + str(nodo_comparacion))
                        nodos_conectados.append(nodo_comparacion)

                    # Si cumple la condicion 3 (mismo cuadrante)
                    elif (calcularCuadrante(nodo_eje_x) == calcularCuadrante(nodo_comparacion_eje_x)) and (calcularCuadrante(nodo_eje_y) == calcularCuadrante(nodo_comparacion_eje_y)):
                        #print("cuadrante. Nodo principal:" + str(nodo) + "||  Nodo comparacion:" + str(nodo_comparacion))
                        nodos_conectados.append(nodo_comparacion)

        return nodos_conectados

            

    def calcularVertices():

        for i in range(len(lista_nodos)):
            for j in range(len(lista_nodos[i])):
                nodosSeleccionados = comprobarConexionNodos(lista_nodos[i][j])
                vertices = []

                for z in range(len(nodosSeleccionados)):
                    vertices.append((lista_nodos[i][j], nodosSeleccionados[z]))

                grafo.add_edges_from(vertices)


    calcularVertices()
    
    axis[1] = plt.subplot2grid(shape=(1, 3), loc=(0, 1), rowspan=1, colspan=3)

    if tamaño_sudoku == 9:
        axis[1] = nx.draw_circular(grafo, node_color = colores_nodos, node_size = 250, width = 0.2, font_size=7, with_labels = True)
    elif tamaño_sudoku == 4:
        axis[1] = nx.draw_circular(grafo, node_color = colores_nodos, node_size = 650, width = 0.4, font_size=12, with_labels = True)



# Quitar bordes de los axis
def set_off_axis(axis, l):
    for i in range(l):
        axis[i].set_axis_off()




# 
#
#    Sudoku 9x9
#
#

#
# MARK: Pantalla del grafo resuelto (9x9)
#

def mostrar_grafo_resuelto_9x9(event):

    colored_solutionFigure, colored_solutionAxis = plt.subplots(1, 4)

    # Grafo
    set_up_grafo(axis=colored_solutionAxis, colores_nodos=get_solution_data(value="color", sudoku_type="9x9"), tamaño_sudoku=9, tamaño_cuadrante=3)
    
    # Tabla
    board = sudoku_datos_solucion_9x9.board
    valores_tabla = [[str(board[r][c]) for c in range(len(board))] for r in range(len(board))]
    
    set_up_sudoku_reducido(axis=colored_solutionAxis, color_values=get_solution_data("positions", sudoku_type="9x9"), valores_tabla=valores_tabla, sudoku_type="9x9")

    # Quitar bordes de los axis 
    set_off_axis(axis=colored_solutionAxis, l=1)

    plt.show()



#
# MARK: Pantalla del sudoku resuelto (9x9)
#

def solve_sudoku_9x9(event):
    
    solutionFigure, solutionAxis = plt.subplots(1, 2)
    
    # Tabla
    board = sudoku_datos_solucion_9x9.board
    valores_tabla = [[str(board[r][c]) for c in range(len(board))] for r in range(len(board))]

    set_up_sudoku_full(axis=solutionAxis, valores_tabla=valores_tabla, sudoku_type="9x9")
    
    # Boton colorear solucion
    axis_boton_grafo = plt.axes([0.65, 0.4, 0.15, 0.07])
    boton_grafo = Button(axis_boton_grafo, "Generar grafo resuelto", color="blue", hovercolor="green")
    boton_grafo.on_clicked(mostrar_grafo_resuelto_9x9)
    
    # Quitar bordes de los axis    
    set_off_axis(axis=solutionAxis, l=2)

    plt.show()



#
# MARK: Pantalla del grafo inicial (9x9)
#

def mostrar_grafo_inicial_9x9(event):

    grafoInicialFigure, grafoInicialAxis = plt.subplots(1, 4)

    # Grafo
    set_up_grafo(axis=grafoInicialAxis, colores_nodos=get_initial_data(value="color", sudoku_type="9x9"), tamaño_sudoku=9, tamaño_cuadrante=3)

    # Tabla
    board = sudoku_datos_iniciales_9x9[:]
    valores_tabla = [[str(board[r][c]) for c in range(len(board))] for r in range(len(board))]
    
    set_up_sudoku_reducido(axis=grafoInicialAxis, color_values=get_initial_data("positions", sudoku_type="9x9"), valores_tabla=valores_tabla, sudoku_type="9x9")

    # Quitar bordes de los axis    
    set_off_axis(axis=grafoInicialAxis, l=1)

    plt.show()



#
# MARK: Pantalla del sudoku inicial (9x9)
#

def load_initial_sudoku_9x9(event):

    initialFigures, initialAxis = plt.subplots(1, 2)

    # Tabla
    board = sudoku_datos_iniciales_9x9[:]
    valores_tabla = [[str(board[r][c]) for c in range(len(board))] for r in range(len(board))]
    
    set_up_sudoku_full(axis=initialAxis, valores_tabla=valores_tabla, sudoku_type="9x9")

    # Boton resolver
    axis_boton_resolver = plt.axes([0.65, 0.5, 0.15, 0.07])
    boton_resolver = Button(axis_boton_resolver, "Resolver", color="blue", hovercolor="green")
    boton_resolver.on_clicked(solve_sudoku_9x9)

    # Boton grafo inicial
    axis_boton_grafo = plt.axes([0.65, 0.4, 0.15, 0.07])
    boton_grafo = Button(axis_boton_grafo, "Generar grafo inicial", color="blue", hovercolor="green")
    boton_grafo.on_clicked(mostrar_grafo_inicial_9x9)

    # Quitar bordes de los axis
    set_off_axis(axis=initialAxis, l=2)
    
    plt.show()






# 
#
#    Sudoku 4x4
#
#



#
# MARK: Datos del sudoku
#

sudoku_datos_iniciales_4x4 = SudokuBoard(value=4).getBoard()

sudoku_datos_solucion_4x4 = SudokuBoard(value=4)
start_time2 = time.time()
sudoku_datos_solucion_4x4.solveGraphColoring(m=4)
print("4x4: --- %s seconds ---" % (time.time() - start_time2))



#
# MARK: Pantalla del grafo resuelto (4x4)
#

def mostrar_grafo_resuelto_4x4(event):

    colored_solutionFigure, colored_solutionAxis = plt.subplots(1, 4)

    # Grafo
    set_up_grafo(axis=colored_solutionAxis, colores_nodos=get_solution_data(value="color", sudoku_type="4x4"), tamaño_sudoku=4, tamaño_cuadrante=2)
    
    # Tabla
    board = sudoku_datos_solucion_4x4.board
    valores_tabla = [[str(board[r][c]) for c in range(len(board))] for r in range(len(board))]
    
    set_up_sudoku_reducido(axis=colored_solutionAxis, color_values=get_solution_data("positions", sudoku_type="4x4"), valores_tabla=valores_tabla, sudoku_type="4x4")

    # Quitar bordes de los axis 
    set_off_axis(axis=colored_solutionAxis, l=1)

    plt.show()



#
# MARK: Pantalla del sudoku resuelto (4x4)
#

def solve_sudoku_4x4(event):
    
    solutionFigure, solutionAxis = plt.subplots(1, 2)
    
    # Tabla
    board = sudoku_datos_solucion_4x4.board
    valores_tabla = [[str(board[r][c]) for c in range(len(board))] for r in range(len(board))]

    set_up_sudoku_full(axis=solutionAxis, valores_tabla=valores_tabla, sudoku_type="4x4")
    
    # Boton colorear solucion
    axis_boton_grafo = plt.axes([0.65, 0.4, 0.15, 0.07])
    boton_grafo = Button(axis_boton_grafo, "Generar grafo resuelto", color="blue", hovercolor="green")
    boton_grafo.on_clicked(mostrar_grafo_resuelto_4x4)
    
    # Quitar bordes de los axis    
    set_off_axis(axis=solutionAxis, l=2)

    plt.show()



#
# MARK: Pantalla del grafo inicial (4x4)
#

def mostrar_grafo_inicial_4x4(event):

    grafoInicialFigure, grafoInicialAxis = plt.subplots(1, 4)

    # Grafo
    set_up_grafo(axis=grafoInicialAxis, colores_nodos=get_initial_data(value="color", sudoku_type=sudoku_datos_iniciales_4x4), tamaño_sudoku=4, tamaño_cuadrante=2)

    # Tabla
    board = sudoku_datos_iniciales_4x4[:]
    valores_tabla = [[str(board[r][c]) for c in range(len(board))] for r in range(len(board))]
    
    set_up_sudoku_reducido(axis=grafoInicialAxis, color_values=get_initial_data("positions", sudoku_type="4x4"), valores_tabla=valores_tabla, sudoku_type="4x4")

    # Quitar bordes de los axis    
    set_off_axis(axis=grafoInicialAxis, l=1)

    plt.show()



#
# MARK: Pantalla del sudoku inicial (4x4)
#

def load_initial_sudoku_4x4(event):

    initialFigures, initialAxis = plt.subplots(1, 2)

    # Tabla
    board = sudoku_datos_iniciales_4x4[:]
    valores_tabla = [[str(board[r][c]) for c in range(len(board))] for r in range(len(board))]
    
    set_up_sudoku_full(axis=initialAxis, valores_tabla=valores_tabla, sudoku_type="4x4")

    # Boton resolver
    axis_boton_resolver = plt.axes([0.65, 0.5, 0.15, 0.07])
    boton_resolver = Button(axis_boton_resolver, "Resolver", color="blue", hovercolor="green")
    boton_resolver.on_clicked(solve_sudoku_4x4)

    # Boton grafo inicial
    axis_boton_grafo = plt.axes([0.65, 0.4, 0.15, 0.07])
    boton_grafo = Button(axis_boton_grafo, "Generar grafo inicial", color="blue", hovercolor="green")
    boton_grafo.on_clicked(mostrar_grafo_inicial_4x4)

    # Quitar bordes de los axis
    set_off_axis(axis=initialAxis, l=2)
    
    plt.show()






#
# MARK: Pantalla de carga
#

def main():

    # Sudoku 9x9
    axis_boton_9x9 = plt.axes([0.4, 0.55, 0.2, 0.15])
    boton_9x9 = Button(axis_boton_9x9, "Cargar sudoku 9x9", color="gray")
    boton_9x9.on_clicked(load_initial_sudoku_9x9)

    # Sudoku 4x4
    axis_boton_4x4 = plt.axes([0.4, 0.35, 0.2, 0.15])
    boton_4x4 = Button(axis_boton_4x4, "Cargar sudoku 4x4", color="gray")
    boton_4x4.on_clicked(load_initial_sudoku_4x4)

    plt.show()
    

# Main thread
if __name__ == "__main__" : 
    main()