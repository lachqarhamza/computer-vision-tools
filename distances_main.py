import cv2
path1 = ''
path2 = ''
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
# see if the images are correctly loaded
cv2.imshow('image 1', img1)
cv2.imshow('image 2', img2)
