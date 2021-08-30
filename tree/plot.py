# https://zhuanlan.zhihu.com/p/35574577

import networkx as nx
import matplotlib.pyplot as plt


def create_graph(g: nx.Graph, node, pos=None, x=0, y=0, layer=1):
    if pos is None:
        pos = {}

    pos[node.val] = (x, y)
    if node.left:
        g.add_edge(node.val, node.left.val)
        l_x, l_y = x - 1 / 2 ** layer, y - 1
        l_layer = layer + 1
        create_graph(g, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
    if node.right:
        g.add_edge(node.val, node.right.val)
        r_x, r_y = x + 1 / 2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(g, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
    return g, pos


def print_tree(node):
    if not node:
        print("空树")
        return
    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node)
    fig, ax = plt.subplots(figsize=(8, 10))
    nx.draw_networkx(
        graph,
        pos,
        ax=ax,
        node_size=300,
        font_size=10,
        font_color="#fff",
        node_color="#000",
        arrows=False
    )
    plt.show()
