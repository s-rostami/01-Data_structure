from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def BFS(self, startNode):
        visited = set()
        st = []
        st.append(startNode)

        while st:

            curr = st.pop(0)

            if curr not in visited:
                print(curr, end=" ")
                visited.add(curr)

            for item in self.graph[curr]:
                if item not in visited:
                    st.append(item)


g = Graph()
g.insertEdge(2, 1)
g.insertEdge(2, 5)
g.insertEdge(5, 6)
g.insertEdge(5, 8)
g.insertEdge(6, 9)

g.BFS(2)
