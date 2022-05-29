#ádsa%%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
print("Kích thước mặc định khung vẽ: ", plt.rcParams["figure.figsize"])
plt.rcParams["figure.figsize"] = (20, 10)
print("Kích thước khung vẽ sau thiết lập: ", plt.rcParams["figure.figsize"])
my_colors = 'rgbkymc'

#addsda
data = pd.read_csv('test.csv')
data.columns
pf = df = pd.DataFrame(data)

#%dá%
df.describe()

#ád %%
df.describe()
# dsa%%
grouped_slug = df.groupby('slug').agg({'sl': ['mean']})
print(grouped_slug)
ax = grouped_slug.plot.bar(rot=1)
#ádsa %%

