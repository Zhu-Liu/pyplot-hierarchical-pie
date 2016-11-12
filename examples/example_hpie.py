#!/usr/bin/env python3

import matplotlib.pyplot as plt
from hpie import HierarchicalPie, Path
import random
import sys

fig, ax = plt.subplots()

# set up some data

paths = [Path(tuple(a)) for a in "1 2 12 13 111 112 113 121 122 211 221 222 "
                                 "1111 1112 1121".split(" ")]
pathvalues = {path: random.uniform(1, 100) for path in paths}

# do the magic

hp = HierarchicalPie(pathvalues, ax)

# set plot attributes

hp.plot()
ax.autoscale()
ax.set_aspect("equal")
ax.autoscale_view(True, True, True)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.margins(x=0.1, y=0.1)
ax.set_title('Example HPie')

# a few command line options to display plot/save figure/do nothing:

if "debug" in sys.argv[1:]:
    pass
if "save" in sys.argv[1:]:
    fig.savefig("{}.png".format(__file__), dpi=100, bbox_inches='tight')
if len(sys.argv) == 1:
    plt.show()