import cv2

image = cv2.imread("lena.png")

cv2.imshow("image", image)
cv2.waitKey()

# Basic image transforms
#  image = cv2.flip(image) - Flip image
#  image = cv2.rotate(image, n) - Rotate image to 90 degrees n times

# Transform image using affine matrix
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html
# We need affine transform matrix (M) to calculate new coordinates for output image
# Then we apply M to the image

# Rotation on arbitrary amount of degrees
# M = cv2.getRotationMatrix2D((w / 2, h / 2), 90, 1)
# dst = cv2.warpAffine(image, M, (w, h))

# Shift image
# M = np.float32([[1, 0, 100], [0, 1, 50]])
# dst = cv2.warpAffine(image, M, (w, h))

# Calculate affine matrix from three pairs of point.
# Let's suppose you want add drawn eyeglasses on you photo. You need to transform glasses
# according to face position. Or set texture to the image.
#
# pts1 = np.float32([[50,50],[200,50],[50,200]])
# pts2 = np.float32([[10,100],[200,50],[100,250]])
# M = cv2.getAffineTransform(pts1,pts2)
# dst = cv2.warpAffine(img,M,(cols,rows))
