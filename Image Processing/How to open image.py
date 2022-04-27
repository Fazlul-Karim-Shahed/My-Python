
# from PIL import Image
# import numpy as np
#
# img_1 = Image.open("C:\\Users\\fazlu\OneDrive\Pictures\IMG-20211003-WA0004.jpg")
# number_format_img = np.asarray(img_1)

# =====================================================================================

# import matplotlib.image as mpimg
# import matplotlib.pyplot as plt
#
# img_2 = mpimg.imread("C:\\Users\\fazlu\OneDrive\Pictures\IMG-20211003-WA0004.jpg")
# plt.imshow(img_2)
# plt.colorbar()
# plt.show()

#==========================================================================================

# from skimage import io, img_as_float
# import matplotlib.pyplot as plt
# import numpy as np
#
# image = io.imread("C:\\Users\\fazlu\OneDrive\Pictures\IMG-20211003-WA0004.jpg").astype(np.float)
# # float_image = img_as_float(image)
# print(image)

#===================================================================================================

# import cv2
# import matplotlib.pyplot as plt
#
# image_gray = cv2.imread('C:\\Users\\fazlu\OneDrive\Pictures\IMG-20211003-WA0004.jpg', 0)
# image_color = cv2.imread('C:\\Users\\fazlu\OneDrive\Pictures\IMG-20211003-WA0004.jpg', 1)
#
# plt.imshow(cv2.cvtColor(image_color, cv2.COLOR_BGRA2RGB))
# plt.show()

# cv2.imshow('Colorful Image', image_color)
# cv2.imshow('Gray Image', image_gray)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()