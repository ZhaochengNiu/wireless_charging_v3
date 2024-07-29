import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_theme(context='notebook', style='whitegrid', palette='deep', font='sans-serif', font_scale=1.0, color_codes=True, rc=None)

Local10 = np.loadtxt('../result/LocalEnergyConsumptionInEachSlotFilePath10.cache')
Nearest10 = np.loadtxt('../result/NearestEnergyConsumptionInEachSlotFilePath10.cache')
Random10 = np.loadtxt('../result/RandomEnergyConsumptionInEachSlotFilePath10.cache')
Match10 = np.loadtxt('../result/MatchEnergyConsumptionInEachSlotFilePath10.cache')
Dot10 = np.loadtxt('../result/DotEnergyConsumptionInEachSlotFilePath10.cache')
Proposed10 = np.loadtxt('../result/ProposedEnergyConsumptionInEachSlotFilePath10.cache')

Local20 = np.loadtxt('../result/LocalEnergyConsumptionInEachSlotFilePath20.cache')
Nearest20 = np.loadtxt('../result/NearestEnergyConsumptionInEachSlotFilePath20.cache')
Random20 = np.loadtxt('../result/RandomEnergyConsumptionInEachSlotFilePath20.cache')
Match20 = np.loadtxt('../result/MatchEnergyConsumptionInEachSlotFilePath20.cache')
Dot20 = np.loadtxt('../result/DotEnergyConsumptionInEachSlotFilePath20.cache')
Proposed20 = np.loadtxt('../result/ProposedEnergyConsumptionInEachSlotFilePath20.cache')

Local30 = np.loadtxt('../result/LocalEnergyConsumptionInEachSlotFilePath30.cache')
Nearest30 = np.loadtxt('../result/NearestEnergyConsumptionInEachSlotFilePath30.cache')
Random30 = np.loadtxt('../result/RandomEnergyConsumptionInEachSlotFilePath30.cache')
Match30 = np.loadtxt('../result/MatchEnergyConsumptionInEachSlotFilePath30.cache')
Dot30 = np.loadtxt('../result/DotEnergyConsumptionInEachSlotFilePath30.cache')
Proposed30 = np.loadtxt('../result/ProposedEnergyConsumptionInEachSlotFilePath30.cache')

Local40 = np.loadtxt('../result/LocalEnergyConsumptionInEachSlotFilePath40.cache')
Nearest40 = np.loadtxt('../result/NearestEnergyConsumptionInEachSlotFilePath40.cache')
Random40 = np.loadtxt('../result/RandomEnergyConsumptionInEachSlotFilePath40.cache')
Match40 = np.loadtxt('../result/MatchEnergyConsumptionInEachSlotFilePath40.cache')
Dot40 = np.loadtxt('../result/DotEnergyConsumptionInEachSlotFilePath40.cache')
Proposed40 = np.loadtxt('../result/ProposedEnergyConsumptionInEachSlotFilePath40.cache')

Local50 = np.loadtxt('../result/LocalEnergyConsumptionInEachSlotFilePath50.cache')
Nearest50 = np.loadtxt('../result/NearestEnergyConsumptionInEachSlotFilePath50.cache')
Random50 = np.loadtxt('../result/RandomEnergyConsumptionInEachSlotFilePath50.cache')
Match50 = np.loadtxt('../result/MatchEnergyConsumptionInEachSlotFilePath50.cache')
Dot50 = np.loadtxt('../result/DotEnergyConsumptionInEachSlotFilePath50.cache')
Proposed50 = np.loadtxt('../result/ProposedEnergyConsumptionInEachSlotFilePath50.cache')

Local10_consumption = sum(Local10)
Nearest10_consumption = sum(Nearest10)
Random10_consumption = sum(Random10)
Match10_consumption = sum(Match10)
Dot10_consumption = sum(Dot10)
Proposed10_consumption = sum(Proposed10)

Local20_consumption = sum(Local20)
Nearest20_consumption = sum(Nearest20)
Random20_consumption = sum(Random20)
Match20_consumption = sum(Match20)
Dot20_consumption = sum(Dot20)
Proposed20_consumption = sum(Proposed20)

Local30_consumption = sum(Local30)
Nearest30_consumption = sum(Nearest30)
Random30_consumption = sum(Random30)
Match30_consumption = sum(Match30)
Dot30_consumption = sum(Dot30)
Proposed30_consumption = sum(Proposed30)

Local40_consumption = sum(Local40)
Nearest40_consumption = sum(Nearest40)
Random40_consumption = sum(Random40)
Match40_consumption = sum(Match40)
Dot40_consumption = sum(Dot40)
Proposed40_consumption = sum(Proposed40)

Local50_consumption = sum(Local50)
Nearest50_consumption = sum(Nearest50)
Random50_consumption = sum(Random50)
Match50_consumption = sum(Match50)
Dot50_consumption = sum(Dot50)
Proposed50_consumption = sum(Proposed50)

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
Dot = []
Proposed = []

Local.append(Local10_consumption)
Nearest.append(Nearest10_consumption)
Random.append(Random10_consumption)
Match.append(Match10_consumption)
Dot.append(Dot10_consumption)
Proposed.append(Proposed10_consumption)

Local.append(Local20_consumption)
Nearest.append(Nearest20_consumption)
Random.append(Random20_consumption)
Match.append(Match20_consumption)
Dot.append(Dot20_consumption)
Proposed.append(Proposed20_consumption)

Local.append(Local30_consumption)
Nearest.append(Nearest30_consumption)
Random.append(Random30_consumption)
Match.append(Match30_consumption)
Dot.append(Dot30_consumption)
Proposed.append(Proposed30_consumption)

Local.append(Local40_consumption)
Nearest.append(Nearest40_consumption)
Random.append(Random40_consumption)
Match.append(Match40_consumption)
Dot.append(Dot40_consumption)
Proposed.append(Proposed40_consumption)

Local.append(Local50_consumption)
Nearest.append(Nearest50_consumption)
Random.append(Random50_consumption)
Match.append(Match50_consumption)
Dot.append(Dot50_consumption)
Proposed.append(Proposed50_consumption)

x = np.arange(len(labels))  # the label locations
width = 0.1  # the width of the bars

# colors = ['#9999FF', '#58C9B9', '#CC33CC', '#D1B6E1', '#99FF99', '#FF6666']

# 填充颜色
colors = ['#706fd3', '#34ace0', '#33d9b2', '#ffb142', '#c56cf0','#f78fb3', '#ff4d4d']

fig, ax = plt.subplots()
Local = ax.bar(x - 5*width/2, Local, width=width, label='Local', edgecolor='black', color=colors[0], linewidth=.8, hatch='//')
Nearest = ax.bar(x - 3*width/2, Nearest, width=width, label='Nearest', edgecolor='black', color=colors[1], linewidth=.8, hatch='//')
Random = ax.bar(x - width/2, Random, width=width, label='Random', edgecolor='black', color=colors[2], linewidth=.8, hatch='//')
Match = ax.bar(x + width/2, Match, width=width, label='Match', edgecolor='black', color=colors[3], linewidth=.8, hatch='//')
Dot = ax.bar(x + 3*width/2, Dot, width=width, label='Dot', edgecolor='black', color=colors[4], linewidth=.8, hatch='//')
Proposed = ax.bar(x + 5*width/2, Proposed, width=width, label='Proposed', edgecolor='black', color=colors[5], linewidth=.8, hatch='//')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Number of devices')
ax.set_ylabel('Total energy consumption')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.savefig('./EnergyConsumptionStackedBar.pdf', format='pdf', bbox_inches='tight')
plt.show()
