import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_path = './data/'
train_sales_data = pd.read_csv(data_path + 'train_sales_data.csv', encoding='utf-8')
train_search_data = pd.read_csv(data_path + 'train_search_data.csv', encoding='utf-8')
train_sales_data = train_sales_data.merge(train_search_data, on=['regYear', 'regMonth', 'model', 'province'], how='left')
train_sales_data['index'] = train_sales_data.index

# Import Data
df = train_sales_data.copy()

# Prepare Data
x = df['index'].values.tolist()
y1 = df['salesVolume'].values.tolist()
y2 = df['popularity'].values.tolist()

mycolors = ['tab:blue', 'tab:red', 'tab:green', 'tab:orange', 'tab:red', 'tab:brown', 'tab:grey', 'tab:pink', 'tab:olive']      
columns = ['salesVolume', 'popularity']

# Draw Plot 
fig, ax = plt.subplots(1, 1, figsize=(16,9), dpi= 80)
ax.fill_between(x, y1=y1, y2=0, label=columns[0], alpha=0.5, color=mycolors[0], linewidth=2)
# ax.fill_between(x, y1=y2, y2=0, label=columns[1], alpha=0.5, color=mycolors[1], linewidth=2)

# Decorations
ax.set_title('Personal Savings Rate vs Median Duration of Unemployment', fontsize=18)
ax.set(ylim=[1, 15320])
ax.legend(loc='best', fontsize=12)
# plt.xticks(x, fontsize=10, horizontalalignment='center')
plt.yticks(np.arange(0, 15320, 2000), fontsize=10)
plt.xlim(0, x[-1])

# Draw Tick lines  
for y in np.arange(0, 15320, 2000):    
    plt.hlines(y, xmin=0, xmax=len(x), colors='black', alpha=0.3, linestyles="--", lw=0.5)

# Lighten borders
plt.gca().spines["top"].set_alpha(0)
plt.gca().spines["bottom"].set_alpha(.3)
plt.gca().spines["right"].set_alpha(0)
plt.gca().spines["left"].set_alpha(.3)
plt.show()
