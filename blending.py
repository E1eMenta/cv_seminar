import cv2

image1_path = "lena.png"
image2_path = "image2.jpg"

image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.waitKey()

# To blend images we need to have the same resolution. Resize second image to the first image size.
# h, w, _ = image1.shape
# image2 = cv2.resize(image2, (w, h))

# Let's blend images
# result = 0.5 * image1 + 0.5 * image2  - bad results because "0.5 * image1" casts
# dtype from uint8 to float64
# result = np.uint8(0.5 * image1 + 0.5 * image2) - cast back to image standard dtype=uint8

# The second image could be mask to highlight some part of image
# image2 = np.zeros((600, 600, 3), dtype=np.uint8)
# image2[200:500, 300:400] = 255

# Overflow could happen if we cast to uint8 image, which contains elements < 0 or > 255. Need to clip first.
# result = np.uint8(image1 * 0.5 + 0.7 * image2)
# result = np.uint8(np.clip(image1 * 0.5 + image2 * 0.7))
