import cv2

image_path = "lena.png"

image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

result = cv2.Canny(image, 100, 200)

cv2.imshow("image", image)
cv2.imshow("result", result)
cv2.waitKey()

# 1
# kernel = np.ones((10, 10), np.float32) / 10 ** 2
# result = cv2.filter2D(image, -1, kernel)
# https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html

# 2
# result = cv2.GaussianBlur(image, (11, 11), 0)

# 3
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# kernel = np.array(
#     [[0, 1, 0],
#      [1, -4, 1],
#      [0, 1, 0]],
#     dtype=np.float32
# )
# result = cv2.filter2D(image, -1, kernel)

# 4
# kernel_x = np.array([-1, 1], dtype=np.float32)

# kernel_y = np.array([[-1], [1]], dtype=np.float32)
# result = cv2.filter2D(image, -1, kernel)

# 5
# kernel_x = np.array(
#     [[-1, 0, 1],
#      [-2, 0, 2],
#      [-1, 0, 1]],
#     dtype=np.float32
# )

# kernel_y = np.array(
#     [[-1, -2, -1],
#      [0, 0, 0],
#      [1, 2, 1]],
#     dtype=np.float32
# )
# result = cv2.filter2D(image, -1, kernel)

# result = cv2.Canny(image, 100, 200)
