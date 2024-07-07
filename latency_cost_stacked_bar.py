import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_theme(context='notebook', style='whitegrid', palette='deep', font='sans-serif', font_scale=1.0, color_codes=True, rc=None)

Local10 = np.loadtxt('./result/LocalLatencyCostInEachSlotFilePath10.cache')
Nearest10 = np.loadtxt('./result/NearestLatencyCostInEachSlotFilePath10.cache')
Random10 = np.loadtxt('./result/RandomLatencyCostInEachSlotFilePath10.cache')
Match10 = np.loadtxt('./result/MatchLatencyCostInEachSlotFilePath10.cache')
Proposed10 = np.loadtxt('./result/ProposedLatencyCostInEachSlotFilePath10.cache')

Local20 = np.loadtxt('./result/LocalLatencyCostInEachSlotFilePath20.cache')
Nearest20 = np.loadtxt('./result/NearestLatencyCostInEachSlotFilePath20.cache')
Random20 = np.loadtxt('./result/RandomLatencyCostInEachSlotFilePath20.cache')
Match20 = np.loadtxt('./result/MatchLatencyCostInEachSlotFilePath20.cache')
Proposed20 = np.loadtxt('./result/ProposedLatencyCostInEachSlotFilePath20.cache')

Local30 = np.loadtxt('./result/LocalLatencyCostInEachSlotFilePath30.cache')
Nearest30 = np.loadtxt('./result/NearestLatencyCostInEachSlotFilePath30.cache')
Random30 = np.loadtxt('./result/RandomLatencyCostInEachSlotFilePath30.cache')
Match30 = np.loadtxt('./result/MatchLatencyCostInEachSlotFilePath30.cache')
Proposed30 = np.loadtxt('./result/ProposedLatencyCostInEachSlotFilePath30.cache')

Local40 = np.loadtxt('./result/LocalLatencyCostInEachSlotFilePath40.cache')
Nearest40 = np.loadtxt('./result/NearestLatencyCostInEachSlotFilePath40.cache')
Random40 = np.loadtxt('./result/RandomLatencyCostInEachSlotFilePath40.cache')
Match40 = np.loadtxt('./result/MatchLatencyCostInEachSlotFilePath40.cache')
Proposed40 = np.loadtxt('./result/ProposedLatencyCostInEachSlotFilePath40.cache')

Local50 = np.loadtxt('./result/LocalLatencyCostInEachSlotFilePath50.cache')
Nearest50 = np.loadtxt('./result/NearestLatencyCostInEachSlotFilePath50.cache')
Random50 = np.loadtxt('./result/RandomLatencyCostInEachSlotFilePath50.cache')
Match50 = np.loadtxt('./result/MatchLatencyCostInEachSlotFilePath50.cache')
Proposed50 = np.loadtxt('./result/ProposedLatencyCostInEachSlotFilePath50.cache')

Local10_cost = sum(Local10)
Nearest10_cost = sum(Nearest10)
Random10_cost = sum(Random10)
Match10_cost = sum(Match10)
Proposed10_cost = sum(Proposed10)

Local20_cost = sum(Local20)
Nearest20_cost = sum(Nearest20)
Random20_cost = sum(Random20)
Match20_cost = sum(Match20)
Proposed20_cost = sum(Proposed20)

Local30_cost = sum(Local30)
Nearest30_cost = sum(Nearest30)
Random30_cost = sum(Random30)
Match30_cost = sum(Match30)
Proposed30_cost = sum(Proposed30)

Local40_cost = sum(Local40)
Nearest40_cost = sum(Nearest40)
Random40_cost = sum(Random40)
Match40_cost = sum(Match40)
Proposed40_cost = sum(Proposed40)

Local50_cost = sum(Local50)
Nearest50_cost = sum(Nearest50)
Random50_cost = sum(Random50)
Match50_cost = sum(Match50)
Proposed50_cost = sum(Proposed50)

labels = ['10', '20', '30', '40', '50']
Local = []
Nearest = []
Random = []
Match = []
Proposed = []

Local.append(Local10_cost)
Nearest.append(Nearest10_cost)
Random.append(Random10_cost)
Match.append(Match10_cost)
Proposed.append(Proposed10_cost)

Local.append(Local20_cost)
Nearest.append(Nearest20_cost)
Random.append(Random20_cost)
Match.append(Match20_cost)
Proposed.append(Proposed20_cost)

Local.append(Local30_cost)
Nearest.append(Nearest30_cost)
Random.append(Random30_cost)
Match.append(Match30_cost)
Proposed.append(Proposed30_cost)

Local.append(Local40_cost)
Nearest.append(Nearest40_cost)
Random.append(Random40_cost)
Match.append(Match40_cost)
Proposed.append(Proposed40_cost)

Local.append(Local50_cost)
Nearest.append(Nearest50_cost)
Random.append(Random50_cost)
Match.append(Match50_cost)
Proposed.append(Proposed50_cost)

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
ax.set_ylabel('Total latency cost')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.savefig('./LatencyCostStackedBar.pdf', format='pdf')
plt.show()
