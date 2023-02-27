import matplotlib.pyplot as plt
import pydicom

img = pydicom.dcmread('image1.dcm')
plt.imshow(img.pixel_array, cmap=plt.cm.bone)
plt.show()