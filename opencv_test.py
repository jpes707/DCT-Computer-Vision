import cv2
import imutils
import numpy as np
from PIL import Image
import os


class CustomError(Exception):
    pass


def plot_point(x, y, color=(255, 255, 0)):
    if x < 0 or y < 0:
        raise CustomError('Graphing of negative point attempted')
    IMG.putpixel((x, y), color)


def get_relative_path(*args):
	return os.path.join(os.path.dirname(os.path.abspath(__file__)), *args)


def save_image(filename):
    IMG.save(get_relative_path(filename))


# load the image and compute the ratio of the old height
# to the new height, clone it, and resize it
image = cv2.imread("data/Track 10-22/60_4.png", cv2.IMREAD_COLOR)
ratio = image.shape[0] / 500.0
orig = image.copy()
# image = imutils.resize(image, height = 500)
print(np.argwhere(image > 250))

print(image)
IMG = Image.new('RGB', (image.shape[1], image.shape[0]), (255, 0, 0))
for i in range(image.shape[1]):
	for j in range(image.shape[0]):
		if image[j, i][0] > 100 and image[j, i][1] > 100 and image[j, i][2] > 100 and image[j, i][0] < 175 and image[j, i][1] < 175 and image[j, i][2] < 175:
			plot_point(i, j, (255, 255, 255))
		elif image[j, i][0] < 50 and image[j, i][1] < 50 and image[j, i][2] < 50:
			plot_point(i, j, (0, 0, 0))

save_image('Out.png')

exit()
# convert the image to grayscale, blur it, and find edges
# in the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)
# show the original image and the edge detected image
print("STEP 1: Edge Detection")
cv2.imshow("Image", image)
cv2.imshow("Edged", edged)

# find the contours in the edged image, keeping only the
# largest ones, and initialize the screen contour
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)#[:5]
# loop over the contours
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	# if our approximated contour has four points, then we
	# can assume that we have found our screen
	if len(approx) == 4:
		screenCnt = approx
		break
# show the contour (outline) of the piece of paper
print("STEP 2: Find contours of paper")
cv2.drawContours(image, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Outline", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
