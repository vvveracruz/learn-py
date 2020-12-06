import cv2, time

video = cv2.VideoCapture( 0 )

n = 1
while True:
    n += 1
    check, frame = video.read()

    cv2.imshow( "Capturing", frame )

    key = cv2.waitKey(50)

    if key == ord( 'q' ):
        break

video.release()
cv2.destroyAllWindows()
print(n)
