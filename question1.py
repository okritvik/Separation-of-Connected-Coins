"""
Created on Tue Mar 15 19:23:54 2022

@author: okritvik
"""

import cv2
import numpy as np

# Kernel for morphology
kernel = np.ones((10, 10), np.uint8)

# Reading the image    
img = cv2.imread("./images/Q1image.png")
copied_image = img.copy()

#converting to binary
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# Creating a structural Element
ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (33,33))

# Applying morphology operator
cls_image = cv2.morphologyEx(img, cv2.MORPH_OPEN, ellipse)

cv2.imshow("MORPH",cls_image)
cv2.imwrite("Q1_Separated_Coins.png",cls_image)
# Detecting the circles
circles = cv2.HoughCircles(cls_image,cv2.HOUGH_GRADIENT,1,50, param1=60,param2=30,minRadius=0,maxRadius=0)
# circles = np.uint16(np.around(circles))
cls_image = cv2.cvtColor(cls_image,cv2.COLOR_GRAY2BGR)
# Drawing the circles on the image
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cls_image,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cls_image,(i[0],i[1]),2,(0,0,255),3)


print("Number of coins: ",len(circles[0]))
cv2.imshow("Detected Circles",cls_image)
cv2.imwrite("Q1_Coins.png",cls_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
