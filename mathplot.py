import matplotlib.pyplot as plt
import numpy as np
for style in plt.style.available:
    plt.style.use(style)
    plt.figure(style)
    data = np.arange(10)
    plt.plot(data)
    plt.show()
