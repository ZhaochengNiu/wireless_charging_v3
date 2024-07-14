import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_theme(context='notebook', style='whitegrid', palette='deep', font='sans-serif', font_scale=1.0, color_codes=True, rc=None)

Local10 = np.loadtxt('../result/LocalEnergyHarvestInEachSlotFilePath10.cache')
Nearest10 = np.loadtxt('../result/NearestEnergyHarvestInEachSlotFilePath10.cache')
Random10 = np.loadtxt('../result/RandomEnergyHarvestInEachSlotFilePath10.cache')
Match10 = np.loadtxt('../result/MatchEnergyHarvestInEachSlotFilePath10.cache')
Proposed10 = np.loadtxt('../result/ProposedEnergyHarvestInEachSlotFilePath10.cache')

Local20 = np.loadtxt('../result/LocalEnergyHarvestInEachSlotFilePath20.cache')
Nearest20 = np.loadtxt('../result/NearestEnergyHarvestInEachSlotFilePath20.cache')
Random20 = np.loadtxt('../result/RandomEnergyHarvestInEachSlotFilePath20.cache')
Match20 = np.loadtxt('../result/MatchEnergyHarvestInEachSlotFilePath20.cache')
Proposed20 = np.loadtxt('../result/ProposedEnergyHarvestInEachSlotFilePath20.cache')

Local30 = np.loadtxt('../result/LocalEnergyHarvestInEachSlotFilePath30.cache')
Nearest30 = np.loadtxt('../result/NearestEnergyHarvestInEachSlotFilePath30.cache')
Random30 = np.loadtxt('../result/RandomEnergyHarvestInEachSlotFilePath30.cache')
Match30 = np.loadtxt('../result/MatchEnergyHarvestInEachSlotFilePath30.cache')
Proposed30 = np.loadtxt('../result/ProposedEnergyHarvestInEachSlotFilePath30.cache')

Local40 = np.loadtxt('../result/LocalEnergyHarvestInEachSlotFilePath40.cache')
Nearest40 = np.loadtxt('../result/NearestEnergyHarvestInEachSlotFilePath40.cache')
Random40 = np.loadtxt('../result/RandomEnergyHarvestInEachSlotFilePath40.cache')
Match40 = np.loadtxt('../result/MatchEnergyHarvestInEachSlotFilePath40.cache')
Proposed40 = np.loadtxt('../result/ProposedEnergyHarvestInEachSlotFilePath40.cache')

Local50 = np.loadtxt('../result/LocalEnergyHarvestInEachSlotFilePath50.cache')
Nearest50 = np.loadtxt('../result/NearestEnergyHarvestInEachSlotFilePath50.cache')
Random50 = np.loadtxt('../result/RandomEnergyHarvestInEachSlotFilePath50.cache')
Match50 = np.loadtxt('../result/MatchEnergyHarvestInEachSlotFilePath50.cache')
Proposed50 = np.loadtxt('../result/ProposedEnergyHarvestInEachSlotFilePath50.cache')

Local10_harvest = sum(Local10)
Nearest10_harvest = sum(Nearest10)
Random10_harvest = sum(Random10)
Match10_harvest = sum(Match10)
Proposed10_harvest = sum(Proposed10)

Local20_harvest = sum(Local20)
Nearest20_harvest = sum(Nearest20)
Random20_harvest = sum(Random20)
Match20_harvest = sum(Match20)
Proposed20_harvest = sum(Proposed20)

Local30_harvest = sum(Local30)
Nearest30_harvest = sum(Nearest30)
Random30_harvest = sum(Random30)
Match30_harvest = sum(Match30)
Proposed30_harvest = sum(Proposed30)

Local40_harvest = sum(Local40)
Nearest40_harvest = sum(Nearest40)
Random40_harvest = sum(Random40)
Match40_harvest = sum(Match40)
Proposed40_harvest = sum(Proposed40)

Local50_harvest = sum(Local50)
Nearest50_harvest = sum(Nearest50)
Random50_harvest = sum(Random50)
Match50_harvest = sum(Match50)
Proposed50_harvest = sum(Proposed50)

# print(Local20_utility)
# print(Nearest20_utility)
# print(Random20_utility)
# print(Game20_utility)
# print(Proposed20_utility)

labels = ['10', '20', '30', '40', '50']
Local = []
Nearest = []
Random = []
Match = []
Proposed = []

Local.append(Local10_harvest)
Nearest.append(Nearest10_harvest)
Random.append(Random10_harvest)
Match.append(Match10_harvest)
Proposed.append(Proposed10_harvest)

Local.append(Local20_harvest)
Nearest.append(Nearest20_harvest)
Random.append(Random20_harvest)
Match.append(Match20_harvest)
Proposed.append(Proposed20_harvest)

Local.append(Local30_harvest)
Nearest.append(Nearest30_harvest)
Random.append(Random30_harvest)
Match.append(Match30_harvest)
Proposed.append(Proposed30_harvest)

Local.append(Local40_harvest)
Nearest.append(Nearest40_harvest)
Random.append(Random40_harvest)
Match.append(Match40_harvest)
Proposed.append(Proposed40_harvest)

Local.append(Local50_harvest)
Nearest.append(Nearest50_harvest)
Random.append(Random50_harvest)
Match.append(Match50_harvest)
Proposed.append(Proposed50_harvest)

x = np.arange(len(labels))  # the label locations
width = 0.1  # the width of the bars

# colors = ['#9999FF', '#58C9B9', '#CC33CC', '#D1B6E1', '#99FF99', '#FF6666']

# 填充颜色
colors = ['#706fd3', '#34ace0', '#33d9b2', '#ffb142', '#c56cf0','#f78fb3', '#ff4d4d']

fig, ax = plt.subplots()
Local = ax.bar(x - 2*width, Local, width=width, label='Local', edgecolor='black', color=colors[0], linewidth=.8, hatch='//')
Nearest = ax.bar(x - width, Nearest, width=width, label='Nearest', edgecolor='black', color=colors[1], linewidth=.8, hatch='//')
Random = ax.bar(x, Random, width=width, label='Random', edgecolor='black', color=colors[2], linewidth=.8, hatch='//')
Match = ax.bar(x + width, Match, width=width, label='Match', edgecolor='black', color=colors[3], linewidth=.8, hatch='//')
Proposed = ax.bar(x + 2*width, Proposed, width=width, label='Proposed', edgecolor='black', color=colors[4], linewidth=.8, hatch='//')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Number of devices')
ax.set_ylabel('Total energy harvest')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.savefig('./EnergyHarvestStackedBar.pdf', format='pdf', bbox_inches='tight')
plt.show()
