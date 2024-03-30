import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('bug.jpg')
print(img)

plt.imshow(img)
