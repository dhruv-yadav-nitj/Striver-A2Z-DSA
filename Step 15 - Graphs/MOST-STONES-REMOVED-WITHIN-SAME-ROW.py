class DisjointSet:
    def __init__(self, n):
        self.size = [1] * n
        self.parent = list(range(n))

    def find_parent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u, v):
        pu = self.find_parent(u)
        pv = self.find_parent(v)

        # If both nodes have the same parent, they are already connected
        if pu == pv:
            return

        # Connect the smaller tree to the larger one
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]

    def is_same_component(self, u, v):
        return self.find_parent(u) == self.find_parent(v)


class Solution:
    def removeStones(self, stones):
        n = len(stones)
        # Find the maximum row and column indices in the stones list
        maxi_row = max(stone[0] for stone in stones)
        maxi_col = max(stone[1] for stone in stones)

        # Initialize the disjoint set
        ds = DisjointSet(maxi_row + maxi_col + 2)

        # A dictionary to mark where stones are placed
        stone_map = {}

        # Union rows and columns
        for stone in stones:
            u, v = stone[0], stone[1] + maxi_row + 1
            ds.union_by_size(u, v)
            stone_map[u] = 1
            stone_map[v] = 1

        # Calculate the maximum number of stones that can be removed
        ans = n
        for i in range(maxi_row + maxi_col + 2):
            if i in stone_map:
                if ds.find_parent(i) == i:
                    ans -= 1

        return ans
