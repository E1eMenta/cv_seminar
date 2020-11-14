import cv2
import numpy as np

image_path = "lena.png"

image = cv2.imread(image_path)
h, w, _ = image.shape

pts1 = np.float32([[0, 0], [600, 0], [0, 600]])
pts2 = np.float32([[10, 200], [2000, -50], [300, 250]])

M = cv2.getAffineTransform(pts1, pts2)
result = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_LINEAR)

cv2.imshow("image", image)
cv2.imshow("image2", result)
cv2.waitKey()

# 1
#  image2 = image[::-2, ::-2]
