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
