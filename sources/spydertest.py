# -*- coding: utf-8 -*-
"""
Spyder Editor

Test: Jupyter-Zellen in Spyder
"""

# %% 

msg = "Hallo Jörg"
print(msg)

# %%

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()