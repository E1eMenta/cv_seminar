import cv2

image1 = cv2.imread("frame_24.png", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("frame_30.png", cv2.IMREAD_GRAYSCALE)

pts1 = cv2.goodFeaturesToTrack(image1, maxCorners=200, qualityLevel=0.02,
                               minDistance=15, blockSize=3)
pts2 = cv2.goodFeaturesToTrack(image2, maxCorners=200, qualityLevel=0.02,
                               minDistance=15, blockSize=3)

for point in pts1:
    x, y = point[0].astype(int)
    cv2.circle(image1, (x, y), 3, (0, 0, 255), -1)
for point in pts2:
    x, y = point[0].astype(int)
    cv2.circle(image2, (x, y), 3, (0, 0, 255), -1)

cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.waitKey()

# 1
# image1 = cv2.imread("pisa.png")
# image2 = cv2.imread("pisa_0.jpeg")

# features = cv2.SIFT_create()
#
# kp1, des1 = features.detectAndCompute(image, None)
# kp2, des2 = features.detectAndCompute(result, None)
# print(kp1, des1)

# 2
# for point in kp1:
#     x, y = int(point.pt[0]), int(point.pt[1])
#     cv2.circle(image, (x, y), 3, (0, 0, 255), -1)
# for point in kp2:
#     x, y = int(point.pt[0]), int(point.pt[1])
#     cv2.circle(result, (x, y), 3, (0, 0, 255), -1)


# 3
# How can we match descriptors from two images? The easiest way is:
# for each descriptor in dis1 find the nearest one in dis2. Choose 100 pairs
# with minimal euclidian distance. They are the matches.
# But this is a lot of code, that's why we will use standart functions
#
# lann = cv2.FlannBasedMatcher({"algorithm": 0, "trees": 5}, {"checks": 50})
# matches = flann.knnMatch(des1, des2, k=2)
#
# good = []
# for m, n in matches:
#     if m.distance < 0.7 * n.distance:
#         good.append(m)
#
# src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
# dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)


# Draw on one image
# h1, w1, _ = image1.shape
# h2, w2, _ = image2.shape
# max_h, max_w = max(h1, h2), max(w1, w2)
#
# combine = np.zeros((max_h, 2 * max_w, 3), dtype=np.uint8)
# combine[:h1, :w1] = image1
# combine[:h2, max_w:max_w + w2] = image2
#
# for src_pt, dst_pt in zip(src_pts, dst_pts):
#     x1, y1 = src_pt[0].astype(np.int)
#     x2, y2 = dst_pt[0].astype(np.int)
#     x2 += max_w
#     cv2.circle(combine, (x1, y1), 3, (0, 0, 255), -1)
#     cv2.circle(combine, (x2, y2), 3, (0, 0, 255), -1)
#     cv2.line(combine, (x1, y1), (x2, y2), (0, 255, 0), thickness=1)


# What if the same image
# rot_mat = cv2.getRotationMatrix2D((image1.shape[1] // 2, image1.shape[0] // 2), 45, 1.0)
# image2 = cv2.warpAffine(image1, rot_mat, image1.shape[1::-1], flags=cv2.INTER_LANCZOS4)


# Find transformation from one image to another
# M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
# transformed = cv2.warpPerspective(image1, M, (w1, h1))


# Optical flow
# image1 = cv2.imread("frame_24.png", cv2.IMREAD_GRAYSCALE)
# image2 = cv2.imread("frame_30.png", cv2.IMREAD_GRAYSCALE)
