import os
cwd = os.getcwd()
import pandas as pd

pip install skimage

import skimage
from skimage.io import imread
from skimage import io

from skimage.feature import greycomatrix
from skimage.feature import greycoprops
#from skimage.feature import graycomatrix, graycoprops
#from skimage import data
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.decomposition import PCA

from scipy import signal
from scipy.signal import find_peaks


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from PIL import Image
import cv2

from pydub import AudioSegment

home = os.getcwd()

exec(open(cwd+'/scripts/spleenTexture.py').read())
exec(open(cwd+'/scripts/GCM.py').read())
exec(open(cwd+'/scripts/dataNorm.py').read())
exec(open(cwd+'/scripts/dataNorm.py').read())
exec(open(cwd+'/scripts/plotPCA.py').read())
exec(open(cwd+'/scripts/showVideo.py').read())
exec(open(cwd+'/scripts/powerSpectrum.py').read())
exec(open(cwd+'/scripts/plot_powerSpectrum.py').read())
