import cv2 as cv
image = cv.imread('2.jpg')



#cv.waitKey(0)
#this iimage is too large, let's rescale this image
def rescale(frame, scale=0.8):
                width = int(frame.shape[1]*scale)
                height = int(frame.shape[1]*scale)
                dimension = (width,height)
                return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
resized_image = rescale(image)
cv.imshow("this is resized image", resized_image)

blur = cv.GaussianBlur(resized_image,(7,7),cv.BORDER_DEFAULT)
cv.imshow("this is blured image",blur)
cv.waitKey(0)