# Computer vision project
from google.colab.patches import cv2_imshow
import cv2
import io
from PIL import Image
from google.colab import files

img=cv2.imread('pup.jpg')
 # pre-processing image
 # Converting to greyscale
Grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2_imshow(Grey_img)# to see grey image

grey_blur=cv2.medianBlur(Grey_img,5)# adds blur effect to image
cv2_imshow(grey_blur)#to see blur image
edges=cv2.Canny(grey_blur,100,200)#this will make the image black and will show only edges
cv2_imshow(edges)
edge=cv2.adaptiveThreshold(grey_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize=9,C=9)
cv2_imshow(edge)
# Original image
print("Original image")
cv2_imshow(img)# to see original image
#image turned cartoon
print("Cartoon image")
cartoon=cv2.bitwise_and(img,img,mask=edge)
cv2_imshow(cartoon)

# To save and download image
cv2.imwrite('cartoon.jpg',cartoon)
files.download('cartoon.jpg')