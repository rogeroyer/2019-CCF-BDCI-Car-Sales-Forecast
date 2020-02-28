import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_path = './data/'
train_sales_data = pd.read_csv(data_path + 'train_sales_data.csv', encoding='utf-8')
train_search_data = pd.read_csv(data_path + 'train_search_data.csv', encoding='utf-8')
train_sales_data = train_sales_data.merge(train_search_data, on=['regYear', 'regMonth', 'model', 'province', 'adcode'], how='left')
train_sales_data['index'] = train_sales_data.index

df = train_sales_data

# print(df[df['salesVolume'] > df['popularity']])
print(df)

x = df['index']
y1 = df['salesVolume']
y2 = df['popularity']

# Plot Line1 (Left Y Axis)
fig, ax1 = plt.subplots(1,1,figsize=(16,9), dpi= 80)
ax1.plot(x, y1, color='tab:red')

# Plot Line2 (Right Y Axis)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.plot(x, y2, color='tab:blue')

# Decorations
# ax1 (left Y axis)
# ax1.set_xlabel('Sample Index', fontsize=20)

ax1.set_yticks([])
ax2.set_yticks([])

# ax1.tick_params(axis='x', rotation=0, labelsize=12)
ax1.set_ylabel('# salesVolume', color='tab:red', fontsize=20)
# ax1.tick_params(axis='y', rotation=0, labelcolor='tab:red' )
ax1.grid(alpha=.4)

# ax2 (right Y axis)
ax2.set_ylabel("# popularity", color='tab:blue', fontsize=20)
# ax2.tick_params(axis='y', labelcolor='tab:blue')
# ax2.set_xticks(np.arange(0, len(x), 60))
# ax2.set_xticklabels(x[::60], rotation=90, fontdict={'fontsize':10})
# ax2.set_title("The difference between salesVolume and popularity.", fontsize=22)

ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)

# ax1.spines['bottom'].set_visible(False)
# ax2.spines['bottom'].set_visible(False)

ax1.spines['left'].set_visible(False)
ax2.spines['left'].set_visible(False)

ax1.spines['right'].set_visible(False)
ax2.spines['right'].set_visible(False)

fig.tight_layout()

plt.show()
