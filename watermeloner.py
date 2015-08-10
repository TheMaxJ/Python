import cv2
import sys
import Image
import cv2.cv as cv

def getWM():
        return Image.open("/Users/maxjohnson/python/watermeloner/watermelon.png") 

watermelon = getWM()
imagepath = sys.argv[1]
outputpath = sys.argv[2]
cascpath = "/Users/maxjohnson/python/watermeloner/haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascpath)

image = cv.LoadImage(imagepath)
gray = cv2.cvtColor(cv2.imread(imagepath), cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=float(sys.argv[3]),
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "Found {0} faces!".format(len(faces))
src = Image.open(imagepath)
# Draw a rectangle around the faces
for (x, y, w, h) in faces:
        maxsize = (w, h)
        watermelon.thumbnail(maxsize, Image.ANTIALIAS)

        wmpx = watermelon.load()
        srcpx = src.load()
        
        for i in range(watermelon.size[0]):    # for every pixel:
                for j in range(watermelon.size[1]):
                        if wmpx[i,j][3] != 0:
                                srcpx[x+i, y+j] = wmpx[i,j]
        watermelon = getWM()

src.show()
src.save(outputpath)
