import cv2

image_path = "lena.png"

image = cv2.imread(image_path)
print(f"Image shape: {image.shape}")

cv2.imshow("image", image)
cv2.waitKey()

# numpy
# Image is a numpy array with shape: [H, W, 3] - color, [H, W] - color

# Get pixel color
# pixel = image[y, x]

# Get box (crop image)
# crop = image[y0:y1, x0:x1]

# Get channel as gray
# channel = image[:, :, 0]

# Get channel as colored
# image[:, :, 0] = 0
# image[:, :, 0] = 1

# Different color spaces
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.COLOR_BGR2GRAY
# cv2.COLOR_BGR2RGB
# cv2.COLOR_BGR2YUV
# cv2.COLOR_BGR2HSV
# print(f"Image shape after color change: {image.shape}")

# Generate image
# image = np.zeros((600, 600, 3), dtype=np.uint8)
# image[:, :, 2] = 255
# image = np.random.randint(0, 255, (600, 600, 3))
