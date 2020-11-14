import cv2

image_path = "lena.png"

image = cv2.imread(image_path)
print(f"Image shape: {image.shape}")

resized = cv2.resize(image, (600, 300))

print(f"Image shape: {resized.shape}")

cv2.imshow("image", image)
cv2.imshow("resized", resized)
cv2.waitKey()

# resized = cv2.resize(image, (600, 100))
# resized = cv2.resize(image, (100, 600))
# resized = cv2.resize(image, (1000, 1000))
#
# image = cv2.resize(image, (300, 300))
# resized = cv2.resize(image, (1000, 1000))
#
# resized = cv2.resize(image, (300, 300), interpolation=cv2.INTER_LINEAR)
# resized = cv2.resize(image, (300, 300), interpolation=cv2.INTER_NEAREST)
# resized = cv2.resize(image, (300, 300), interpolation=cv2.INTER_CUBIC)
# resized = cv2.resize(image, (300, 300), interpolation=cv2.INTER_AREA)
# resized = cv2.resize(image, (300, 300), interpolation=cv2.INTER_LANCZOS4)
# Linear, bilinear, trilinear
