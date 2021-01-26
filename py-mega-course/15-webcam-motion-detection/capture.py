# this file needs to be run from the system terminal (not atom terminal)
# because it needs the correct permissions to access the camera


# TODO: instead of rectangle around the moving object draw the outline?

import cv2, time

first_frame = None

video = cv2.VideoCapture( 0 )
time.sleep(2) # it takes a couple seconds for the camera to start going

while True:
    check, frame = video.read()
    status = 0

    gray_frame = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY )
    gray_frame = cv2.GaussianBlur( gray_frame, ( 21, 21 ), 0 ) # removes noise

    if first_frame is None:
        first_frame = gray_frame
        continue # to the beginning of the While loop

    delta_frame = cv2.absdiff( first_frame, gray_frame )

    thresh_frame = cv2.threshold( delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate( thresh_frame, None, iterations = 2)

    ( cnts,_ ) = cv2.findContours(
        thresh_frame.copy(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE )

    for contour in cnts:
        if cv2.contourArea( contour ) < 1000: # filter out small contours
            continue
        status = 1
        ( x, y, w, h ) = cv2.boundingRect( contour )
        cv2.rectangle( frame, (x, y), ( x+w, y+h), (0, 255, 0), 3)

    # cv2.imshow( "Gray Frame", gray_frame )
    # cv2.imshow( "Delta Frame", delta_frame)
    # cv2.imshow( "Threshold Frame", thresh_frame )
    # cv2.imshow( "Background", first_frame
    cv2.imshow( "Capturing", frame )

    key = cv2.waitKey(1)
    if key == ord( 'q' ):
        break

video.release()
cv2.destroyAllWindows()
