import cv2

image = cv2.imread("lena.png")

cv2.imshow("image", image)
cv2.waitKey()

# Blur image
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# result = cv2.Blur(image, (11, 11))

# The same blur operation. Implemented as convolution operation with uniform kernel.
# kernel = np.ones((10, 10), np.float32) / 10 ** 2
# result = cv2.filter2D(image, -1, kernel)
# https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html

# Another blur kernel, gaussian for better blurring
# result = cv2.GaussianBlur(image, (11, 11), 0)

# Laplacian filter. Edge detector.
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# kernel = np.array(
#     [[0, 1, 0],
#      [1, -4, 1],
#      [0, 1, 0]],
#     dtype=np.float32
# )
# result = cv2.filter2D(image, -1, kernel)

# Image derivative across x axis. Horizontal edge detector.
# kernel_x = np.array([-1, 1], dtype=np.float32)

# Image derivative across y axis. Vertical edge detector.
# kernel_y = np.array([[-1], [1]], dtype=np.float32)
# result = cv2.filter2D(image, -1, kernel)

# Sobel x fiter. Better edge detector.
# kernel_x = np.array(
#     [[-1, 0, 1],
#      [-2, 0, 2],
#      [-1, 0, 1]],
#     dtype=np.float32
# )

# Sobel y filter.
# kernel_y = np.array(
#     [[-1, -2, -1],
#      [0, 0, 0],
#      [1, 2, 1]],
#     dtype=np.float32
# )
# result = cv2.filter2D(image, -1, kernel)

# Canny advanced edge detector. Base on sobel with postprocessing.
# result = cv2.Canny(image, 100, 200)
