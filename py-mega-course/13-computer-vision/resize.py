'''
A script that resizes all the images in a given directory
to a maximum size of 100 x 100.
'''
import cv2, os

_folder_input = './input'
_folder_output = './output'

def isFolderStructureValid(
        folder_input = _folder_input,
        folder_output = _folder_output ):
    try:
        if os.path.exists( folder_input ) == True:
            pass
        else:
            raise Exception( 'No inputs folder' )
    except Exception as inst:
        print( inst.args )
    return None

isFolderStructureValid( folder_input = 'bananas')

img = cv2.imread( './input/galaxy.jpg', 0 )
    #   1 = RGB, 0 = B&W, -1 = RGB w transparency channel

resized_img = cv2.resize( img, ( int( img.shape[1] / 2 ),
    int( img.shape[0] / 2 ) ) )

cv2.imshow( 'Galaxy', resized_img )
cv2.imwrite( '../test/Galaxy_resized.jpg', resized_img )
cv2.waitKey( 2000 )
cv2.destroyAllWindows()

def resize( folder_input = _folder_input, folder_output = _folder_output ):
    return None
