from sklearn import metrics
import pandas as pd
import itertools

# metrics.adjusted_mutual_info_score(labels_true, labels_pred)

gv = pd.read_excel('generatedvalues.xlsx', 'test', index_col=None, na_values=['NA'])

vars = gv.columns
varpairs = list(itertools.combinations(vars, 2))

# for x_1,x_2 in varpairs:
