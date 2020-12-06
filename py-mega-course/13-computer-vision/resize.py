'''
A script that resizes all the images in a given directory
to a maximum size of 100 x 100.
'''
import cv2, os
from glob import glob


#   set up global vars
_IMG_FOLDER = './img/'
_IMG_FORMAT = '.jpg'

images = glob( _IMG_FOLDER + '*' + _IMG_FORMAT )

for image in images:
    img = cv2.imread(image,0)
    re = cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite(image+"resized.jpg",re)
