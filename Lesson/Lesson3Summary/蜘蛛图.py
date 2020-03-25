import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

labels = np.array([u"推进", "KDA", u"生存",u"团战", u"发育", u"输出"])
stats = [76, 58, 67, 97, 86, 58]

angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)

stats = np.concatenate((stats, [stats[0]]))
angles = np.concatenate((angles, [angles[0]]))

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, stats, 'o-', linewidth=2)
ax.fill(angles,stats,alpha=0.25)
font = font_manager.FontProperties(fname=r'/System/Library/Fonts/STHeiti Medium.ttc')
ax.set_thetagrids(angles * 180/np.pi, labels, FontProperties=font)
plt.show()
