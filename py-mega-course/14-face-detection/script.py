import cv2

CASCADE_FILE = 'haarcascade_frontalface_default.xml'
SUBJECT_IMAGE_FILE = 'news.jpg'

face_cascade = cv2.CascadeClassifier( CASCADE_FILE )

img = cv2.imread( SUBJECT_IMAGE_FILE )
img_grey = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )

faces = face_cascade.detectMultiScale(
    img_grey,
    scaleFactor = 1.1,
    minNeighbors = 5 )

for x, y, w, h in faces:
    img = cv2.rectangle( img, (x, y), ( int(x+w), int(y+h) ), ( 0, 255, 0 ), 3 )

resized = cv2.resize( img, ( int(img.shape[1]/2), int(img.shape[0]/2) ) )

cv2.imshow( 'Subject image', resized )
cv2.waitKey(0)
cv2.destroyAllWindows()
