from sklearn import metrics
import pandas as pd
import itertools
import steinertree as ST

# metrics.adjusted_mutual_info_score(labels_true, labels_pred)

gv = pd.read_excel('generatedvalues.xlsx', 'test', index_col=None, na_values=['NA'])

vars = list(gv.columns)
print 'VARS:'
print vars
varpairs = list(itertools.combinations(vars, 2))
edges = []
for x_1,x_2 in varpairs:
    mi_weight = metrics.adjusted_mutual_info_score(gv[x_1], gv[x_2])
    edges.append([vars.index(x_1),vars.index(x_2),-1.0*float(mi_weight)])
print edges
    # get the mi of the pair, add the pairs and the edge weight to the list of edge_subgraph

learnedgraph = ST.Graph(len(vars),len(vars),edges).steinerTree();
