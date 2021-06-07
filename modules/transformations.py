def binarize(img, t): # t is the threshold
	M =
	N =
	for i in range (0, M, 1):
		for j in range (0, N, 1) :
			if img[i][j] >= t:
				img[i][j] = 0 else :
			img[i][j] = 1
	return (img)

