# https://zhuanlan.zhihu.com/p/35574577

import networkx as nx
import matplotlib.pyplot as plt


def create_graph(g: nx.Graph, node, pos: dict, x=0, y=0, layer: int = 1) -> None:
    pos[node.val] = (x, y)
    if node.left:
        g.add_edge(node.val, node.left.val)
        l_x = x - 1 / (2 ** layer)
        create_graph(g, node.left, pos, l_x, y - 1, layer + 1)

    if node.right:
        g.add_edge(node.val, node.right.val)
        r_x = x + 1 / (2 ** layer)
        create_graph(g, node.right, pos, r_x, y - 1, layer + 1)


def print_tree(node):
    if not node:
        print("空树")
        return

    graph = nx.DiGraph()
    pos = {}
    create_graph(graph, node, pos)
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
