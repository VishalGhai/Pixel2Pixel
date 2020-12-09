from cv2 import cv2 as cv
import os
def rescaling(frame,w,h):
    try:
        path = os.path.join("D:\\STUDY\\Django\\src\\project1",frame)
        cvimg = cv.imread(path)
        dimensions=(int(w),int(h))
        rescaled = cv.resize(cvimg,dimensions,interpolation=cv.INTER_AREA)
        filename = 'savedimage.jpg'
        cv.imwrite(os.path.join("D:\\STUDY\\Django\\src\\project1\\static\\project1",filename),rescaled)
    except Exception as e:
        print(str(e))