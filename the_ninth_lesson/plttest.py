import numpy as np
import matplotlib.pyplot as plt


# plt.figure(figsize= (8,4), facecolor= None)
# plt.subplot(324)
# plt.show()

from scipy.interpolate import interp1d
import numpy as np
xs = np.arange(10)
ys = 2*xs + 1
interp_func = interp1d(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)