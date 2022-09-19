import apriltag
import cv2
import os
import numpy as np
from time import time
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# slide a window across the image
start_time = time()
def reader(detector, img, file_name):
    print(img.shape)
    tag_list = []
    global img2
    divisions = 12
    success = False
    while not success and divisions < 150:
        print(divisions)
        for y in range(0, img.shape[0], img.shape[0] // divisions):
            for x in range(0, img.shape[1], img.shape[1] // divisions):
                result, img2 = detector.detect(img[y:y + 325, x:x + 325], return_image=True)
                if (len(result) != 0) and all(result) not in tag_list:
                    tag_list.append(result)
                    cv2.imwrite("Outputs/"+file_name+".output.jpg", img2)
                    success = True
        divisions += 24
    return tag_list
if __name__ == '__main__':
    fail = []
    detector = apriltag.Detector()
    directory = './' # "data/Track 10-22/"
    for f in os.listdir(directory):
        print(str(f))
        if str(f) == '.DS_Store':
            continue
        if str(f) != 'large_sand.png':
            continue
        file = directory+f
        print(file)
        img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        tag_list = reader(detector, img, file)
        if(len(tag_list)==0):
            fail.append(file)
        print(tag_list)
    print('time', time() - start_time)
    cv2.destroyAllWindows()
    print(fail)
