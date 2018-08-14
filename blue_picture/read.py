# coding=utf-8

from skimage import io
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
import sys,os 

#img=io.imread('./blue_0_1005.jpg')
for file in sys.argv[1]:
    
    print img.shape
    print img

    img_2 = mpimg.imread('./blue_0_1005.jpg')
    print img_2.shape
    print img_2

    print(img == img_2)
