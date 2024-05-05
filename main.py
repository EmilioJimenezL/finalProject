import networkx as nx
import matplotlib.pyplot as plt
import random
from networkx.algorithms import traversal, tree

def crear_grafo_aleatorio():
    num_nodes = random.randint(3, 10)  # Al menos tres nodos para asegurar un grafo interesante
    g = nx.Graph()
    g.add_nodes_from(range(1, num_nodes + 1))
    for i in range(1, num_nodes):
        weight = random.randint(1, 10)
        g.add_edge(i, i + 1, weight=weight)
    for _ in range(num_nodes // 2):
        i, j = random.sample(range(1, num_nodes + 1), 2)
        weight = random.randint(1, 10)
        g.add_edge(i, j, weight=weight)
    return g

def mostrar_grafo(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=8, font_color='darkred')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

def obtener_grado_nodo(G, nodo):
    return G.degree(nodo)

def mostrar_matriz_adyacencia(G):
    print(nx.adjacency_matrix(G).todense())

def mostrar_lista_adyacencia(G):
    print(nx.adjacency_data(G))

def bfs_recursion(G, start_node):
    return list(traversal.bfs_tree(G, start_node))

def dfs_recursion(G, start_node):
    return list(traversal.dfs_tree(G, start_node))

def mostrar_orden_topologico(DG):
    try:
        return list(nx.topological_sort(DG))
    except nx.NetworkXUnfeasible:
        return "No se puede determinar un orden topológico debido a un ciclo."

def mst_prim(WG):
    return list(tree.minimum_spanning_tree(WG, algorithm='prim').edges(data=True))

def mst_kruskal(WG):
    return list(tree.minimum_spanning_tree(WG, algorithm='kruskal').edges(data=True))

def menu_principal():
    G = crear_grafo_aleatorio()
    while True:
        print("\nMenú Principal - Operaciones sobre Grafos")
        print("1. Mostrar Grafo Actual")
        print("2. Generar y Mostrar Nuevo Grafo Aleatorio")
        print("3. Mostrar Matriz de Adyacencia del Grafo")
        print("4. Mostrar Lista de Adyacencia del Grafo")
        print("5. Realizar y Mostrar BFS desde un Nodo")
        print("6. Realizar y Mostrar DFS desde un Nodo")
        print("7. Obtener el Grado de un Nodo")
        print("8. Mostrar Orden Topológico (DAG requerido)")
        print("9. Mostrar MST usando Prim")
        print("10. Mostrar MST usando Kruskal")
        print("11. Salir")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            mostrar_grafo(G)
        elif choice == '2':
            G = crear_grafo_aleatorio()
            mostrar_grafo(G)
        elif choice == '3':
            mostrar_matriz_adyacencia(G)
        elif choice == '4':
            mostrar_lista_adyacencia(G)
        elif choice == '5':
            nodo = int(input("Ingresa el nodo inicial para BFS: "))
            print("BFS Recorrido desde el nodo", nodo, ":", bfs_recursion(G, nodo))
        elif choice == '6':
            nodo = int(input("Ingresa el nodo inicial para DFS: "))
            print("DFS Recorrido desde el nodo", nodo, ":", dfs_recursion(G, nodo))
        elif choice == '7':
            nodo = int(input("Ingresa el nodo para obtener su grado: "))
            print(f"El grado del nodo {nodo} es {obtener_grado_nodo(G, nodo)}")
        elif choice == '8':
            DG = G.copy(as_view=False)
            DG = nx.DiGraph([(u, v, {'weight': d['weight']}) for u, v, d in G.edges(data=True)])
            print("Orden Topológico:", mostrar_orden_topologico(DG))
        elif choice == '9':
            print("MST con Prim:", mst_prim(G))
        elif choice == '10':
            print("MST con Kruskal:", mst_kruskal(G))
        elif choice == '11':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Para ejecutar el menú principal, descomente la siguiente línea:
menu_principal()