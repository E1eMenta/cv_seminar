import cv2
import numpy as np

image1_path = "lena.png"
image2_path = "image2.jpg"

image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

h, w, _ = image1.shape
image2 = cv2.resize(image2, (w, h))
print(f"Image 1 shape: {image1.shape}")
print(f"Image 2 shape: {image2.shape}")


image2 = np.zeros((600, 600, 3))
image2[200:400, 100:150] = 255
result = np.uint8(0.5 * image1 + 0.8 * image2)

cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.imshow("result", result)
cv2.waitKey()

# 1
# h, w, _ = image1.shape
# image2 = cv2.resize(image2, (w, h))

# 2
# result = 0.5 * image1 + 0.5 * image2
# result = np.uint8(0.5 * image1 + 0.5 * image2)

# 3
# image2 = np.zeros((600, 600, 3), dtype=np.uint8)
# image2[200:500, 300:400] = 255

# 4
# result = np.uint8(image1 * 0.5 + 0.7 * image2)
# result = np.clip(np.uint8(image1 * 0.5 + image2 * 0.7))
