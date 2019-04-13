import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
import math
print("Hello")
image=cv2.imread('ProjectExp.png')
#cv2.imshow("images", image)
#cv2.waitKey(0)
# define the list of boundaries
boundaries = [
    ([0, 0, 100], [50, 56, 255])]
# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
    
    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)
        

# show the images
    cv2.imshow("images",mask)
    cv2.waitKey(0)
    out=cv2.findNonZero(mask)
    boundaries1 = [
            ([0,242,255],[200,242,255])]
    for (lower1,upper1) in boundaries1:
            lower1=np.array(lower1,dtype="uint8")
            upper1=np.array(upper1,dtype="uint8")

            
        #cv2.imshow("images", output)
        #cv2.imshow("imahes", output)
        #cv2.waitKey(0)
            mask1=cv2.inRange(image,lower1,upper1)
            output1=cv2.bitwise_and(image,image,mask=mask1)
            cv2.imshow("image2",mask1)
            cv2.waitKey(0)
            out=cv2.findNonZero(mask)
            out1=cv2.findNonZero(mask1)
            coords=random.choice(out)
            coords1=random.choice(out1)
            x,y=coords.ravel()
            a,b=coords1.ravel()
            cv2.line(image,(x,y),(a,b),(255,255,255),1)
            cv2.imshow("Final",image)
            cv2.waitKey(0)
            
            cv2.destroyAllWindows()
            ds1=(x-a)**2
            ds2=(y-b)**2
            dist=math.sqrt(ds1+ds2)
            print(dist)
#cv2.imshow("BlackHole",img)
#cv2.waitKey(0)
#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.plot([50,100],[80,100],'c',linewidth=5)
#plt.show()
