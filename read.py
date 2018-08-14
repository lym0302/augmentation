# coding=utf-8

from skimage import io
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
import sys,os 

#img=io.imread('./blue_0_1005.jpg')
for path,pathname,filenames in os.walk(sys.argv[1]):
    for filename in filenames:
        with open(os.path.join(sys.argv[1],filename)) as f:
            if filename.endswith('jpg'):
                img = io.imread(f)
                print img.shape
                print img

                img_2 = mpimg.imread(f)
                print img_2.shape
                print img_2

                print(img == img_2)
