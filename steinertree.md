Hailey James

**Steiner Tree Solution Write-Up**

**Algorithm:**

The algorithm proceeds by finding all minimum weight spanning trees using all  possible combinations of nodes. Specifically, we find the minimum weight  spanning tree using only terminal nodes (if possible) using Kruskal’s algorithm. Then we find the minimum weight spanning tree using the terminal nodes and one other node (attempting all non-terminal nodes as this possible extra node). We continue, using an additional two nodes for the minimum weight spanning tree. As we proceed, we keep track of  the current minimum weight spanning tree, which is initialized to infinity (or concretely, the sum of all the edges plus 1).Any time we are not able to reach  all the nodes, the weight of the spanning tree is assigned to infinity (or a very large number, which can be adapted in order to suit various test suites).

**Correctness:**

The algorithm proceeds by attempting every viable spanning tree. We know that  a viable spanning tree is a spanning tree that includes all the terminal nodes and may contain other nodes. Thus we don't attempt every spanning tree of the  graph, but rather only the spanning trees that meet this constraint. Attempting every viable spanning tree and keeping track of the smallest guarantees us to  carry the smallest spanning tree throughout the algorithm, if such a spanning tree exists.

**Runtime:**

Kruskal's algorithm takes $O(m log m)$ or $O(m log n)$ time. We run Kruskal's algorithm on all possible subgraphs of $G$, starting with only the terminal nodes and adding a node one at a time until we have attempted the complete graph. If T is the number of subgraphs is then\
$1 + {n \choose T + 1} + {n \choose T + 2} + {n \choose T + 3} + {n \choose T + 4} + . . . + {n \choose n} \leq {n \choose 1} + {n \choose 2} + {n \choose 3} + {n \choose 4} + . . . + {n \choose n}  = 2^n$

(https://math.stackexchange.com/questions/1125975/proving-sum-k-0n-n-choose-k-2n-with-newtons-binomial-theorem)

Thus we have $O(2^n)$ subgraphs on which we run Kruskal's algorithm, yielding overall $O(2^n * m log n) \in O(2^n)$.
