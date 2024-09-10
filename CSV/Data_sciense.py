import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

dataframe = pd.read_csv('jira_sample.csv')
df = dataframe[['Assignee', 'Reporter']]

G = nx.Graph()
G = nx.from_pandas_edgelist(df, 'Assignee', 'Reporter')

plt.figure(figsize=(10, 8))
nx.draw_shell(G, with_labels=True)

plt.show()