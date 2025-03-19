# Basics
There are mainly two types of graph:
1. Directed Graph
    * Each edge can only represent one way connection.
    * Example: Streep Maps
2. Undirected Graph
    * Each edge represent two way connection.
    * Example: Social Network.

There are other types also though we will not got further deep.They are Cyclic vs Uncyclic,weighted vs unweighted.

## Graph Representations:
Graph can be represented by two ways:
    * Adjacent Matrix: A N*N matrix where a single value represents the presence of edge along with its weight.Example:
    Let suppose the nodes are A,B,C. B and C are connect while A is connected to B only.So the value at index (A,B)=1 and (A,C)=0
    Space Complexity: O(N^2)
    Lookpup Complexity: O(1)
    * Adjaceny linked list:
        Space Complexity: O(V+E)
        LookUp Complexity: O(V) 

# Algorithms

1. BFS (Breadth First Search)
A graph search algorithm which visits all the nodes present at a level before going to further nodes.Here we use Queue data structure to implement this algorithm.This algorithm is used to find shorted path in an undirected unweighted graph.

* Leetcode questions:
Easy:  https://leetcode.com/problems/keys-and-rooms/description/
Medium: https://leetcode.com/problems/number-of-islands/description/, https://leetcode.com/problems/course-schedule/description/
Hard:  https://leetcode.com/problems/word-ladder-ii/description/, https://leetcode.com/problems/minimum-height-trees/description/

2. DFS (Depth First Search)
A graph search algorith which visits all the neighbours of current node before visiting another node.This algorithm uses backtracking once we get at the end of neighbour for current code.

Use case examples:
- Compute a graph’s minimum spanning tree.
- Detect and find cycles in a graph.
- Check if a graph is bipartite.
- Find strongly connected components.
- Topologically sort the nodes of a graph.
- Find bridges and articulation points.
- Find augmenting paths in a flow network.
- Generate mazes.

### Traversel Example:
Here’s the consolidated Markdown text for the example:
### Graph Representation

We will use the following undirected graph:

```
      A
     / \
    B   C
   / \   \
  D   E   F
```

### Adjacency List

```
A: [B, C]
B: [A, D, E]
C: [A, F]
D: [B]
E: [B]
F: [C]
```

---

### DFS Traversal (starting from node A)

Steps:
1. Start at **A**.
2. Visit **B** (first neighbor of A).
3. Visit **D** (first neighbor of B).
4. Backtrack to **B** and visit **E** (next neighbor of B).
5. Backtrack to **A** and visit **C** (next neighbor of A).
6. Visit **F** (first neighbor of C).

**DFS Traversal Order:** A → B → D → E → C → F

---

### BFS Traversal (starting from node A)

Steps:
1. Start at **A** and visit all its neighbors (**B, C**).
2. Move to the next level and visit all neighbors of **B** (**D, E**).
3. Finally, visit neighbors of **C** (**F**).

**BFS Traversal Order:** A → B → C → D → E → F

3. Topological Sort (Kahn's Algorthm)
This algorithm is implemented using BFS and it is used to find cycle in a DAG(Directed Acyclic Graph).In simpler terms toloplogical sort is basically traversal of graph in topologic order(the order in which they are connected).
The complexity of topological sort is O(V+E)

### Example
     A → C
     ↓    ↓
     B → D → E
The topological sort order is:
A, B, C, D, E

4. Topological Sort (DFS)
This algorithm is implemented using reverse DFS.The logic is as follows:
If a G is {V,E} such that v1 -> v2 then topological sort of this graph will be basically as Post order traversal of G{V`,E`} such that v2 -> v1.The complexity is same.

Though BFS based topological sorting it more easy to implement.We should use DFS in case of dependency problems.As DFS based topological sort can be started from a given point.Hence can be easily used to find the dependencies of a give target recursively.

### BFS VS DFS:

### **Time and Space Complexity of BFS and DFS Traversals**

#### **1. Breadth-First Search (BFS)**

**Time Complexity:**
- BFS visits every node and its neighbors once. 
- If the graph has:
  - \(V\) nodes (vertices),
  - \(E\) edges (connections),
  the total time complexity is:
  \[
  O(V + E)
  \]
- For **grid-based problems** (e.g., matrix traversal), where rows = \(m\) and columns = \(n\), the graph has \(V = m \times n\) and at most \(E = 4 \times V\) (since each cell can connect to up to 4 neighbors):
  \[
  O(m \times n)
  \]

**Space Complexity:**
- BFS uses a queue to store nodes to visit and a visited set or array.
- The maximum number of nodes in the queue is the **width** of the graph (worst-case scenario when BFS explores nodes layer by layer).
  - For a **graph**, it’s \(O(V)\).
  - For a **grid**, the queue size is proportional to the boundary size, \(O(\min(m, n))\).
- The visited set adds another \(O(V)\).

\[
\text{Total Space: } O(V) \text{ (for both queue and visited set)}
\]

---

#### **2. Depth-First Search (DFS)**

**Time Complexity:**
- DFS visits every node and explores its neighbors, just like BFS. Hence, the time complexity is:
  \[
  O(V + E)
  \]
- For **grid-based problems**, it simplifies to:
  \[
  O(m \times n)
  \]

**Space Complexity:**
- DFS uses a stack for recursion or an explicit stack structure.
  - The stack size depends on the **depth** of the graph (or grid). In the worst case:
    - For a tree or grid, this could be \(O(V)\) (e.g., a single long chain).
    - For a balanced structure, the depth is proportional to \(O(\log(V))\).
- The visited set adds \(O(V)\).

\[
\text{Total Space: } O(V) \text{ (stack + visited set)}
\]

---

### **Comparison: BFS vs DFS**

| **Aspect**              | **BFS**                      | **DFS**                     |
|-------------------------|------------------------------|-----------------------------|
| **Time Complexity**      | \(O(V + E)\)                 | \(O(V + E)\)                |
| **Space Complexity**     | \(O(V)\)                     | \(O(V)\) (worst case)       |
| **Traversal Nature**     | Layer by layer (queue)       | Deeper first (recursion)    |
| **Use Case**             | Shortest path or level order | Connectivity, paths, etc.   |

---

### **Grid Example**

Consider a grid with \(m \times n\):
- **Time Complexity**: Both BFS and DFS take \(O(m \times n)\) to traverse every cell once.
- **Space Complexity**:
  - BFS: \(O(\min(m, n))\) for the queue.
  - DFS: \(O(m \times n)\) for the recursion stack in the worst case (when the grid is completely connected). 

---

Let me know if you'd like a deeper dive into specific examples!