import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(context='notebook', style='whitegrid', palette='deep', font='sans-serif', font_scale=1.0, color_codes=True, rc=None)

Local = np.loadtxt('./result/LocalTotalCostInEachSlotFilePath10.cache')
Nearest = np.loadtxt('./result/NearestTotalCostInEachSlotFilePath10.cache')
Random = np.loadtxt('./result/RandomTotalCostInEachSlotFilePath10.cache')
Proposed = np.loadtxt('./result/ProposedTotalCostInEachSlotFilePath10.cache')

Local_utility = sum(Local)
Nearest_utility = sum(Nearest)
Random_utility = sum(Random)
Proposed_utility = sum(Proposed)

x_data = ['Local', 'Nearest', 'Random', 'Game']
y_data = [Local_utility, Nearest_utility, Random_utility, Proposed_utility]

colors = ['#9999FF', '#58C9B9', '#CC33CC', '#D1B6E1', '#99FF99', '#FF6666']

# hatch='//'
# hatch='xxx'

plt.figure(figsize=(5, 5))

for i in range(len(x_data)):
    plt.bar(x_data[i], y_data[i], edgecolor='black', color=colors[i], width=0.6, linewidth=.8, hatch='//')

# edgecolor：柱子边缘的颜色。颜色值或颜色值序列。
# linewidth：柱子边缘宽度。浮点数或类数组。如果为0，不绘制柱子边缘。
# width：柱子的宽度。浮点数或类数组结构。默认值为0.8。

plt.title('Total utility of different algorithm')

plt.xlabel('Algorithms')

plt.ylabel('System utility')

plt.savefig('./TotalUtility.pdf', format='pdf')

plt.show()

