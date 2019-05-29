import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('Simple.jpg')
imgplot = plt.imshow(img)
plt.scatter([500, 278, 467, 167], [645, 12, 572, 167])
plt.show()
