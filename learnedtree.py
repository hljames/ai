from sklearn import metrics
import pandas as pd
import itertools
import steinertree as ST
import scipy

# metrics.adjusted_mutual_info_score(labels_true, labels_pred)

gv = pd.read_excel('generatedvalues.xlsx', 'test', index_col=None, na_values=['NA'])

vars = list(gv.columns)
varpairs = list(itertools.combinations(vars, 2))
edges = []
for x_1,x_2 in varpairs:
    mi_weight = metrics.adjusted_mutual_info_score(gv[x_1], gv[x_2])
    edges.append((vars.index(x_1),vars.index(x_2),-1.0*float(mi_weight)))
    # get the mi of the pair, add the pairs and the edge weight to the list of edge_subgraph

learnedgraph = ST.Graph(len(vars),len(vars),edges).steinerTree();

# 2 -- 3 == -0.23618157090427994
# 1 -- 3 == -0.21132812643143897
# 0 -- 4 == -0.1906372331970533
# 3 -- 5 == -0.12619614871380164
# 2 -- 4 == -0.12601632527303563
# 5 -- 6 == -0.10846829470180964

# Calculate the entropy:

# From the learned tree, we have the following parent configuration

# 1 ->
# 2 -> 3 -> 5 -> 6
#   -> 4
# 0 ->
#
def calculate_entropy ():
    entropy = 0
    for var in vars:
        # calculate entropy of variable
        var_entropy = scipy.stats.entropy(gv[var])
        sum = 0
        for x_1,x_2,mi in learnedgraph:
            if x_2 == vars.index(var):
                sum += -1*mi - var_entropy
        entropy += sum
    return entropy

print ("ENTROPY: " + str(calculate_entropy()))
