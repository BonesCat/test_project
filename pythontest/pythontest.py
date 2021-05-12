import cv2 as cv

src = cv.imread(r"D:\data\512512unet_predict\testimage\PANCREAS_0066\076.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
cv.waitKey(0)
cv.destroyAllWindows()
print('this is python')