import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
import random


#
# Insertar los datos iniciales del sudoku
#

tamaño_sudoku = 4
tamaño_cuadrante = 2

initial_data = [
    [1, 3, 2, 4],
    [4, 2, 0, 0],
    [2, 4, 0, 0],
    [3, 1, 4, 2]
]


# Grafos Networkx
grafo_sudoku = nx.Graph()

grafo_completo = nx.complete_graph(16)


# Definir los nodos
lista_nodos = list()

for i in range(len(initial_data)):
        for j in range(len(initial_data)):
            lista_nodos.append(str(i + 1) + ", " + str(j + 1))

lista_nodos = [lista_nodos[i:i+tamaño_sudoku] for i in range(0, len(lista_nodos), tamaño_sudoku)]

for i in range(len(lista_nodos)):
    for j in range(len(lista_nodos[i])):
        grafo_sudoku.add_node(lista_nodos[i][j])


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


# Calcular las aristas del grafo
for i in range(len(lista_nodos)):
    for j in range(len(lista_nodos[i])):
        nodosSeleccionados = comprobarConexionNodos(lista_nodos[i][j])
        vertices = []

        for z in range(len(nodosSeleccionados)):
            vertices.append((lista_nodos[i][j], nodosSeleccionados[z]))

        grafo_sudoku.add_edges_from(vertices)




# Creando el subgrafo obtenido al restar el grafo del sudoku a uno completo
def get_edges(G):
    edges = []

    for edge in G.edges():
        edges.append(edge)
    
    return edges

aristas_grafo_completo = get_edges(grafo_completo)
aristas_grafo_sudoku = get_edges(grafo_sudoku)

aristas_restantes = [a for a in aristas_grafo_completo if a not in aristas_grafo_sudoku]

grafo_restante = nx.Graph()

for n in grafo_sudoku.nodes():
    grafo_restante.add_node(n)

grafo_restante.add_edges_from(aristas_restantes)



# Creando el subgrafo simplificado del sudoku inicial (rellenando esos nodos que solo tienen 1 posibilidad)

def get_sudoku_simplificado(g):

    lista_restricciones = dict()

    def obtener_posible_valor(g, n, v, current_data):

        valores_posibles = [1, 2, 3, 4]

        for neighbor in g.neighbors(n):
            valor = current_data[calc_pos_y(neighbor)][calc_pos_x(neighbor)]
            
            if valor in valores_posibles:
                valores_posibles.remove(valor)
        
        if len(valores_posibles) == 1:
            return valores_posibles[0]
        else:
            return v

    def simplificar_sudoku(g, current_data):

        for i in range(tamaño_sudoku):
            for j in range(tamaño_sudoku):

                nodo = lista_nodos[i][j]
                valor = current_data[i][j]

                if valor == 0:
                    nuevo_valor = obtener_posible_valor(g=g, n=nodo, v=valor, current_data=current_data)
                    
                    if nuevo_valor != valor:
                        current_data[i][j] = nuevo_valor
                        simplificar_sudoku(g=g, current_data=current_data)

    def simplificar_profundamente_sudoku(g, current_data):

        lista_posibilidades = dict()

        def comprobar_valores(g, n, v, current_data):

            """
            comprobar_valores(g, n, v, current_data)[0] --> se obtienen los valores posibles
            comprobar_valores(g, n, v, current_data)[1] --> se obtienen los valores restringidos
            """

            valores_posibles = [1, 2, 3, 4]
            valores_restringidos = []

            for neighbor in g.neighbors(n):
                valor = current_data[calc_pos_y(neighbor)][calc_pos_x(neighbor)]
                
                if valor in valores_posibles:
                    valores_posibles.remove(valor)
                    valores_restringidos.append(valor)
            
            return (valores_posibles, valores_restringidos)

        for i in range(tamaño_sudoku):
            for j in range(tamaño_sudoku):

                nodo = lista_nodos[i][j]
                valor = current_data[i][j]

                if valor == 0:
                    lista_posibilidades[nodo] = comprobar_valores(g=g, n=nodo, v=valor, current_data=current_data)[0]
                    lista_restricciones[nodo] = comprobar_valores(g=g, n=nodo, v=valor, current_data=current_data)[1]

        cuenta_1 = (0, "")
        cuenta_2 = (0, "")
        cuenta_3 = (0, "")
        cuenta_4 = (0, "")
        
        for k in lista_posibilidades.keys():
            if 1 in lista_posibilidades[k]:
                if cuenta_1[0] == 0:
                    cuenta_1 = (cuenta_1[0], str(k))
                cuenta_1 = (cuenta_1[0] + 1, cuenta_1[1])

            if 2 in lista_posibilidades[k]:
                if cuenta_2[0] == 0:
                    cuenta_2 = (cuenta_2[0], str(k))
                cuenta_2 = (cuenta_2[0] + 1, cuenta_2[1])

            if 3 in lista_posibilidades[k]:
                if cuenta_3[0] == 0:
                    cuenta_3 = (cuenta_3[0], str(k))
                cuenta_3 = (cuenta_3[0] + 1, cuenta_3[1])

            if 4 in lista_posibilidades[k]:
                if cuenta_4[0] == 0:
                    cuenta_4 = (cuenta_4[0], str(k))
                cuenta_4 = (cuenta_4[0] + 1, cuenta_4[1])

            
        if cuenta_1[0] == 1:
            current_data[calc_pos_y(cuenta_1[1])][calc_pos_x(cuenta_1[1])] = 1
        if cuenta_2[0] == 1:
            current_data[calc_pos_y(cuenta_2[1])][calc_pos_x(cuenta_2[1])] = 2
        if cuenta_3[0] == 1:
            current_data[calc_pos_y(cuenta_3[1])][calc_pos_x(cuenta_3[1])] = 3
        if cuenta_4[0] == 1:
            current_data[calc_pos_y(cuenta_4[1])][calc_pos_x(cuenta_4[1])] = 4

    
    current_data = initial_data[:]

    simplificar_sudoku(g=g, current_data=current_data)
    simplificar_profundamente_sudoku(g=g, current_data=current_data)

    return (current_data, lista_restricciones)


sudoku_simplificado = get_sudoku_simplificado(g=grafo_sudoku)[0]
lista_restricciones_original = get_sudoku_simplificado(g=grafo_sudoku)[1]


# Simplificar el sudoku
print("El sudoku simplificado es:")
print("")
for i in range(len(sudoku_simplificado)):
    print(sudoku_simplificado[i])



# Creando el subgrafo de los nodos vacíos del subgrafo inicial simplificado
grafo_simplificado_vacio = grafo_sudoku.copy()

nodos_no_vacios = list(str(i + 1) + ", " + str(j + 1) for j in range(len(sudoku_simplificado[i])) for i in range(len(sudoku_simplificado)) if sudoku_simplificado[i][j]!=0)

grafo_simplificado_vacio.remove_nodes_from(nodos_no_vacios)





main_chromatic_polynomial = np.poly1d([0])

grafos_para_descomponer = list()
grafos_completados = list()




# Chromatic Polynomial

# Subgraph chromatic polynomial calculator
def calcular_polinomio_cromatico(g, restriction_list):

    chromatic_polynomial = None

    def add_to_polinomial(value, chromatic_polynomial):
        new_chromatic_pol = None
        if chromatic_polynomial == None:
            new_chromatic_pol = value
        else:
            new_chromatic_pol = chromatic_polynomial * value
        return new_chromatic_pol

    def get_simple_polynomial_value(value):
        return np.poly1d([1, -value])
    
    # Single nodes
    for n in g.nodes():
        if len(list(g.neighbors(n))) == 0:
            chromatic_polynomial = add_to_polinomial(value=get_simple_polynomial_value(value=len(restriction_list[n])), chromatic_polynomial=chromatic_polynomial)
    
    # Edged nodes
    def get_bigger_list(list1, list2):
        if len(list1) > len(list2):
            return (list1, list2)
        elif len(list1) < len(list2):
            return (list2, list1)
        else:
            return (list1, list2)

    aristas = get_edges(g)

    if len(aristas) == 1:

        list1 = restriction_list[aristas[0][0]]
        list2 = restriction_list[aristas[0][1]]

        ordered_lists = get_bigger_list(list1=list1, list2=list2)

        # Adding the bigger list polinomial
        chromatic_polynomial = add_to_polinomial(value=get_simple_polynomial_value(value=len(ordered_lists[0])), chromatic_polynomial=chromatic_polynomial)

        # Adding the smaller
        missing_larger_list = [item for item in [1,2,3,4] if item not in ordered_lists[0]]

        if any(item in missing_larger_list for item in ordered_lists[1]): #********#
            chromatic_polynomial = add_to_polinomial(value=get_simple_polynomial_value(value=len(ordered_lists[1])), chromatic_polynomial=chromatic_polynomial)
        else:
            chromatic_polynomial = add_to_polinomial(value=get_simple_polynomial_value(value=len(ordered_lists[1]) + 1 ), chromatic_polynomial=chromatic_polynomial)
        
        if len(ordered_lists[0]) == 2 and len(ordered_lists[1]) == 2: 
            if (ordered_lists[1][0] in missing_larger_list) and (ordered_lists[1][1] in ordered_lists[0]):
                chromatic_polynomial = chromatic_polynomial - 1
                
            elif (ordered_lists[1][0] in ordered_lists[0]) and (ordered_lists[1][1] in missing_larger_list):
                chromatic_polynomial = chromatic_polynomial - 1
                
                
        elif (len(ordered_lists[0]) == 2 and len(ordered_lists[1]) == 1):
            if not ordered_lists[1][0] in ordered_lists[0]:
                chromatic_polynomial = chromatic_polynomial + 1


    return chromatic_polynomial




# Teorema de la descomposición o reducción-contracción de grafos
def decompose_graph(g, lisst, sign):

    grafos_para_descomponer.remove((g, lisst, sign))

    global main_chromatic_polynomial

    def get_nodos_adyacentes(nodos):
        for nodo in nodos:
            nodos_adyacentes_totales = list(g.neighbors(nodo))
            if len(nodos_adyacentes_totales) != 0:
                return (nodo, nodos_adyacentes_totales[random.randint(0, len(nodos_adyacentes_totales) - 1)])
        

    nodos_adyacentes = get_nodos_adyacentes(nodos=g.nodes())
    

    # Subgrafo eliminando
    grafo_eliminando = g.copy()
    grafo_eliminando.remove_edge(nodos_adyacentes[0], nodos_adyacentes[1])

    if len(get_edges(grafo_eliminando)) == 1:
        #calcular el polinomio cromatico y añadirlo a la principal
        if sign == "+":
            nuevo_polinomio = calcular_polinomio_cromatico(g=grafo_eliminando, restriction_list=lisst)
            main_chromatic_polynomial = main_chromatic_polynomial + nuevo_polinomio

            grafos_completados.append((grafo_eliminando, lisst, ("+", nuevo_polinomio)))
            
        else:
            nuevo_polinomio = calcular_polinomio_cromatico(g=grafo_eliminando, restriction_list=lisst)
            main_chromatic_polynomial = main_chromatic_polynomial - nuevo_polinomio

            grafos_completados.append((grafo_eliminando, lisst, ("-", nuevo_polinomio)))   
        
    else: 
        #seguir descomponiendo
        new_sign = "" 
        if sign == "-":
            new_sign = "-" 
        else: 
            new_sign = "+"
        grafos_para_descomponer.append((grafo_eliminando, lisst, new_sign))



    # Subgrafo contrayendo
    grafo_contrayendo = nx.contracted_nodes(g.copy(), nodos_adyacentes[0], nodos_adyacentes[1], self_loops=False)

    # Actualizando la lista de las restricciones
    nueva_lista = lisst.copy()
    nuevo_valor = list(set(nueva_lista[nodos_adyacentes[0]] + nueva_lista[nodos_adyacentes[1]]))
    nueva_lista[nodos_adyacentes[0]] = nuevo_valor
    del nueva_lista[nodos_adyacentes[1]]

    if len(get_edges(grafo_contrayendo)) == 1:
        #calcular el pol cromatico y añadirlo a la principal
        if sign == "+":
            nuevo_polinomio = calcular_polinomio_cromatico(g=grafo_contrayendo, restriction_list=nueva_lista)
            main_chromatic_polynomial = main_chromatic_polynomial - nuevo_polinomio

            grafos_completados.append((grafo_contrayendo, nueva_lista, ("-", nuevo_polinomio)))
        else:
            nuevo_polinomio = calcular_polinomio_cromatico(g=grafo_contrayendo, restriction_list=nueva_lista)
            main_chromatic_polynomial = main_chromatic_polynomial + nuevo_polinomio

            grafos_completados.append((grafo_contrayendo, nueva_lista, ("+", nuevo_polinomio)))
    
    else: 
        #seguir descomponiendo
        new_sign = ""
        if sign == "-":
            new_sign = "+" 
        else: 
            new_sign = "-"
        grafos_para_descomponer.append((grafo_contrayendo, nueva_lista, new_sign))




copia_grafo_simplificado_vacio = grafo_simplificado_vacio.copy()

if len(copia_grafo_simplificado_vacio.nodes()) != 0 :
    grafos_para_descomponer.append((copia_grafo_simplificado_vacio, lista_restricciones_original, "+"))

    decompose_graph(copia_grafo_simplificado_vacio, lista_restricciones_original, "+")

    while len(grafos_para_descomponer) != 0:
        decompose_graph(grafos_para_descomponer[0][0], grafos_para_descomponer[0][1], grafos_para_descomponer[0][2])

else:
    main_chromatic_polynomial = np.poly1d([1])



# Polinomio Cromático
print("\n Polinomio cromatico: ")
print(main_chromatic_polynomial)

# Número de soluciones (Polinomio cromático evaluado en 4)
print("\n Numero de soluciones posibles: " + str(int(main_chromatic_polynomial(4))))


