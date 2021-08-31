import networkx as nx
import matplotlib.pyplot as plt


def create_graph(g: nx.Graph, nums: list, pos: dict, i: int, x=0, y=0, layer: int = 1) -> None:
    # cur 为堆当前索引

    val = nums[i]
    pos[val] = (x, y)

    i = 2 * i
    if i < len(nums):
        g.add_edge(val, nums[i])
        l_x = x - 1 / (2 ** layer)
        create_graph(g, nums, pos, i, l_x, y - 1, layer + 1)

    i += 1
    if i < len(nums):
        g.add_edge(val, nums[i])
        r_x = x + 1 / (2 ** layer)
        create_graph(g, nums, pos, i, r_x, y - 1, layer + 1)


def print_heap(nums: list):
    graph = nx.DiGraph()
    pos = {}
    create_graph(graph, nums, pos, 1)
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
