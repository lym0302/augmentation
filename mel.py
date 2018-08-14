# coding = utf-8

import librosa as lb
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

Fs = 22050
N_OVERLAP = 1024
N_FFT = 2048
N_MELS = 128

i = 'blues.00001.au'
signal,sr = lb.load(i, sr=Fs)
melspect = lb.feature.melspectrogram(y=signal, sr=Fs, hop_length=N_OVERLAP, n_fft=N_FFT, n_mels=N_MELS)
print melspect.shape
melspect[melspect == 0] = 1e-6
fea = np.log(melspect)
fea = fea.T



datagen = ImageDataGenerator(
        rotation_range = 0.2,
        width_shift_range = 0.2,
        height_shift_range = 0.2,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True,
        fill_mode = 'nearest')

x = np.array(fea)
print x.shape, type(x)
#x = x.reshpae((1,) + x.shape )
#x = x.reshape((1,) + x.shape)
x = x.reshape(1,x.shape[0],128,1)
print x.shape, type(x)


i = 0
for batch in datagen.flow(x,batch_size = 1, save_to_dir = './', save_prefix = 'blue', save_format = 'jpg'):
    i += 1
    if i > 20:
        break
