import cv2
import numpy as np
import glob
 
img_array = []
for filename in glob.glob('/data/test/sinGAN/SinGAN_upgradeversion/generation/results/2022-01-14_00-48-45/s13/*.png'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
out = cv2.VideoWriter('gan_jubin.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()