import cv2
import numpy as np
image_path = "lena.png"

image = cv2.imread(image_path)
# image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
print(f"Image shape: {image.shape}")

image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image = np.random.randint(0, 255, (600, 600, 3))


cv2.imshow("image", image)
cv2.waitKey()
# y0 = 20, y1 =  100, x0= 200, x1 = 400
# numpy
# Get pixel color
# Get box (crop image)
# Get channel as gray
# Get channel as colored

# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.COLOR_BGR2GRAY
# cv2.COLOR_BGR2RGB
# cv2.COLOR_BGR2YUV
# cv2.COLOR_BGR2HSV
# print(f"Image shape after color change: {image.shape}")

# image = np.zeros((600, 600, 3), dtype=np.uint8)
# image[:, :, 2] = 255
