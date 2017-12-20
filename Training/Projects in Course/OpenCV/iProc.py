import cv2
import random
import numpy
import itertools
import pandas

ImgSource = cv2.imread("smallgray.png",1)               # Img reading as gray scale (0)
print(ImgSource,"\n")
print(ImgSource.shape,"\n")

ImgNew = []                                             # Img creation as gray scale

for i in range(64):
    ImgNew.append([])
    for j in range(64):
        ImgNew[i].append(random.randrange(255))

ImgNew = numpy.asarray(ImgNew)
print(ImgNew)
cv2.imwrite("NewGen.png",ImgNew)