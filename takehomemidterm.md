AI exam, 2018. 05. 11. 		 			
NAME: Hailey Lynn James
TOTAL POINTS:60 (minimum to pass: 24)			
NEPTUN ID:

1)	Suggest an admissible heuristic function for the Steiner tree problem (prove its admissibility).

 (15p)

I propose the following heuristic: for each multicast node not currently included in the tree, find the shortest edge connected to this node. Sum the lengths of all of these edges.

Proving admissibility:

First, we know that if we have reached the optimal solution, the heuristic function should return zero. This is consistent with my heuristic function, since all of the multicast nodes would be included in the tree, so the sum of shortest edges of multicast nodes not in the tree must be zero.

Second, the heuristic function should never overestimate the cost. We must use at least one edge to add a missing multicast node to the tree, and in the best case scenario, this is the shortest edge connected to the node. Certainly, the optimal solution might not include the shortest edge connected to every multicast node. However, if we don't use this edge, any edge we do use will be longer, so we have effectively constructed a lower bound, and the heuristic function will not overestimate the cost.



 start with empty graph, get to the minimal spanning tree, add edges? Heuristic: number of multicast nodes (not the best), use of minimal edge of each node (also not the best, not admissable, needs some work?).


Ideas:

-Start with a minimum weight spanning tree, and prune the steiner nodes we don’t need


-Slowly build a tree, finding the shortest path from the tree to the next multicast node




2)	Describe a first-order logic definition that a subgraph of a given graph could be a solution for the Steiner tree problem (i.e., it is the sub-tree connecting all the prespecified nodes, but ignore the minimality of its weight).
 (15p)

Convert code from second assignment to be using quantifiers, first-order logic.  (one line?) (something about should have been brute force search)

3)	Prove that the value of information is nonnegative (see AIMA: Section 16.6: The value of information).
 (15p)

 We seek to prove the following:

$∀e,E_j VPI_e(E_j)≥0$

I proceed with proof by contradiction.

Suppose

$\exists e, E_j VPI(E_j) < 0$

Using the definition of $VPI$.

$\exists e, E_j (\sum_k {P(E_j=e_{jk}|e)EU(\alpha_{e_{jk})}}|e,E_j=e_{jk})-EU(\alpha|e) < 0$

$(\sum_k {P(E_j=e_{jk}|e)EU(\alpha_{e_{jk})}}|e,E_j=e_{jk}) < EU(\alpha|e)$

By removing the sum, we preserve the nature of the inequality.

$\sum_k {P(E_j=e_{jk}|e)max_a\sum{P(RESULT(a) = s'|a,e,e_j)U(s')}} < max_a\sum P(RESULT(a)=s' |a,e)U(s')$

$max_a\sum{P(RESULT(a) = s'|a,e,e_j)U(s')} < max_a\sum P(RESULT(a)=s' |a,e)U(s')$

This states that that best action given the additional piece of evidence is less than the best action without the additional piece of evidence, which cannot be true. Thus we have a contradiction.

**use the other properties**

The value of the further information is irrespective of the ordering

What you gain from a given piece of information is incremental, as you know more and more, probably they will help less and less.

4)	For the Bayesian network in the 2nd major homework and following the data generation described in the 3rd major homework, apply the Steiner tree problem solver for the whole graph with edge weights defined by the pairwise mutual information. The learned tree for all the nodes/variables is a maximum weight spanning tree, where the weights are the mutual information. Give a formula for the entropy of your original network and the entropy of this tree-shaped Bayesian network. Calculate the entropy of this tree-shaped Bayesian network and discuss its relation to the entropy of your original network.
 (15p)

 Difference between the two matrices, one real the other based on independence. To get the other matrix, you use the same marginal distributions and multiply them. Then compare the difference between the matrices. Python probably has a function for this, but the equation is the KL equation. Once you have the mutual information between each of the nodes, use that mutual information as the edge weights for a steiner tree problem. At first, just get a minimum spanning tree. Don't forget to shift to be the maximum spanning tree (multiply by -1 or shift the edge weights). If you just want a polytree, then you are really just getting a maximum weight spanning tree, but if you have some evidences and a query then those can be your multicast nodes, and you can generate explanations (include only the factors that have an actual impact).

 You can calculate the polytree entropy (use the formula you took a pic of) but don't try to calculate the entropy of the original. The formula for the original is from the white board. "Conditional entropy"

 Entropy chain theorem
