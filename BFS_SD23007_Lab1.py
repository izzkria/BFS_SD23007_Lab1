import streamlit as st
from collections import deque

# Directed graph based on your picture
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'F': [],
    'G': ['F'],
    'H': ['G', 'F']
}

st.set_page_config(page_title="BFS Algorithm Visualization", layout="centered")
st.title("Breadth-First Search (BFS)")

st.image("LabReport_BSD2513_#1.jpg", caption="Directed Graph", use_container_width=True)

start = st.selectbox("Select Starting Node:", options=list(graph.keys()), index=0)

def bfs(node, graph):
    visited = []
    levels = {}
    path = []
    queue = deque()
    queue.append((node, 0))

    while queue:
        current, level = queue.popleft()

        if current not in visited:
            visited.append(current)
            levels[current] = level
            path.append(current)

            for neighbour in sorted(graph[current]):  # alphabet order
                if neighbour not in visited and neighbour not in [n[0] for n in queue]:
                    queue.append((neighbour, level + 1))

    return visited, levels, path

if st.button("Run BFS"):
    visited, levels, path = bfs(start, graph)
    
    st.subheader("Traversal Order:")
    st.write(" → ".join(path))
    
    st.subheader("Node Discovery Level:")
    for node in path:
        st.info(f"Level {levels[node]} → {node}")


