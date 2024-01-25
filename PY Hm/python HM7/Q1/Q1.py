from PIL import Image
import numpy as np
pixel_mat = np.array(Image.open('bird.jpg'))

pixel_mat.sort()
img1 = Image.fromarray(pixel_mat)
img1.show()

img2 = Image.fromarray(pixel_mat.transpose((0,1,2)))
img2.show()

img3 = Image.fromarray(255 - pixel_mat)
img3.show()
