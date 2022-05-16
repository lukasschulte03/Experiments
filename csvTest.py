import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('distances.csv', index_col=0)
ax = sns.heatmap(df)
plt.show()


