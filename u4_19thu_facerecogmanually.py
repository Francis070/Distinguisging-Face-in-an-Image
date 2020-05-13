# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:26:15 2019

@author: cttc
"""

import cv2
img = cv2.imread(r"C:\Users\cttc\Desktop\abhi\images.jpg")#oprn cv th4e img as bgr but matplotlib treats it as rgb


cv2.imshow("preview window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

re_img=cv2.resize(img,(600,400))
cv2.imshow("preview window", re_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(r"C:\Users\cttc\Desktop\abhi\modified.jpg",re_img)
cvt_img=cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.grid()
plt.imshow(cvt_img)
plt.show 

rec_img= cv2.rectangle(cvt_img,(79,6),(222,150),(59,159,16),1)
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.grid()
plt.imshow(rec_img)
plt.show 
import numpy as np
plt.xticks(np.linspace(0,img.shape[1],10))#here in the sq. bracket the value represents
                                          #the index no. of the tuple returned as 
                                          #the 0th index is height and 1 is width
plt.yticks(np.linspace(0,img.shape[0],10))
plt.show()
img = cv2.imread(r"C:\Users\cttc\Desktop\abhi\images.jpg")#oprn cv th4e img as bgr but matplotlib treats it as rgb
rec_img= cv2.rectangle(img,(79,6),(222,150),(59,159,16),1)
cv2.imshow("image",rec_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


rec_img=cv2.circle(img,(150,70),80,(0,0,0),1)
cv2.imshow("image",rec_img)
cv2.waitKey(0)
cv2.destroyAllWindows()






