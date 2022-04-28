from PIL import Image
import cv2
from draw import getMap

w, h = 400, 400

map = getMap()

while True:
       
    # Get a numpy array to display from the simulation
    cv2.imshow('image', getMap())
    k = cv2.waitKey(1)
    if k == 27:         # If escape was pressed exit
        cv2.destroyAllWindows()
        break