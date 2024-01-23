import math

def get_cheapest_cost(rootNode):
    if not rootNode:
        return 0

    res = math.inf
    def dfs(node, cost):
        cost += node.cost
        if not node.children:
            res = min(res, cost)

        for n in node.children:
            dfs(n, cost)

    dfs(rootNode, 0)
    return res