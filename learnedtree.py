from sklearn import metrics
import pandas as pd
import itertools
import steinertree as ST

gv = pd.read_excel('generatedvalues.xlsx', 'test', index_col=None, na_values=['NA'])

# the variable from the network (InternationalIntervention, SouthChinaFisheryCollapse, etc)
vars = list(gv.columns)
# create a list of all the possible pairs of variables
varpairs = list(itertools.combinations(vars, 2))
edges = []
# get the mutual information from each pair, and add it as the edge weight of the network
for x_1,x_2 in varpairs:
    mi_weight = metrics.adjusted_mutual_info_score(gv[x_1], gv[x_2])
    edges.append([vars.index(x_1),vars.index(x_2),-1.0*float(mi_weight)])

# run the steinertree algorithm on the network, and return the result 
learnedgraph = ST.Graph(len(vars),len(vars),edges).steinerTree();
