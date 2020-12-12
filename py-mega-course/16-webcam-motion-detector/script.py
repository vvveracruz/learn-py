import cv2, time

first_frame = None


video = cv2.VideoCapture( 0 )

while True:
    check, frame = video.read()
    grey = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY )
    cv2.imshow( "Capturing", grey )

    if first_frame == None:
        first_frame = grey


    key = cv2.waitKey( 1 )
    print( grey )

    if key == ord( 'q' ):
        break

print( a )
video.release()
cv2.destroyAllWindows()
