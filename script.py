import cv2
print(cv2.__version__)


color_image = cv2.imread('messi.jpeg')

shape = color_image.shape
print(shape)
grayscale = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
binary = cv2.threshold(grayscale, 128, 255, cv2.THRESH_BINARY)
cv2.imshow('Grayscale image', grayscale)
cv2.waitKey(0)