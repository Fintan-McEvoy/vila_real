%%capture

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import os.path
os.path.isfile('./segment/predictions.jpg')
os.chdir(cwd+'/segment/')
%ls

import numpy
from PIL import Image 



n = 8 # Number of possibly sharp edges
r = .7 # magnitude of the perturbation from the unit circle, 
# should be between 0 and 1
N = n*3+1 # number of points in the Path
# There is the initial point and 3 points per cubic bezier curve. Thus, the curve will only pass though n points, which will be the sharp edges, the other 2 modify the shape of the bezier curve

counter=0


angles = np.linspace(0,2*np.pi,N)
codes = np.full(N,Path.CURVE4)
codes[0] = Path.MOVETO

while os.path.isfile('predictions.jpg') == False and  counter <1000:
    counter=counter+1

    verts = np.stack((np.cos(angles),np.sin(angles))).T*(2*r*np.random.random(N)+1-r)[:,None]
    verts[-1,:] = verts[0,:] # Using this instad of Path.CLOSEPOLY avoids an innecessary straight line
    path = Path(verts, codes)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    patch = patches.PathPatch(path, facecolor='none', lw=2)
    ax.add_patch(patch)

    ax.set_xlim(np.min(verts)*1.1, np.max(verts)*1.1)
    ax.set_ylim(np.min(verts)*1.1, np.max(verts)*1.1)
    ax.axis('off') # removes the axis to leave only the shape


    plt.savefig("outRand.jpg")
    plt.show()
    
    !./darknet detect ./yolov3-tiny-obj.cfg ./yolov3-tiny-obj_final.weights 'outRand.jpg'>resultRand.txt;
    with open('resultRand.txt', 'r') as file:
        data = file.read().replace('\n', '')
        string1 = 'hip:'
  

        if string1 in data: 
            print('String', 'string1', 'Found In File');
        else: 
            print('String', 'string1' , 'Not Found');
            os.remove('predictions.jpg')
        print(counter)
  

