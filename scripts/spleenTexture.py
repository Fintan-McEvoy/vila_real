def spleenTexture(image_grey):

    PATCH_SIZE = 140

    #image = data.image()
    # select some patches from spleeny areas of the image
    spleen_locations = [(375, 350), (375, 450), (375, 550), (375, 750)]
    spleen_patches = []
    for loc in spleen_locations:
        spleen_patches.append(image_grey[loc[0]:loc[0] + PATCH_SIZE,
                                   loc[1]:loc[1] + PATCH_SIZE])

    # select some patches from adipose areas of the image
    adipose_locations = [(650, 250), (650, 350), (650, 450), (650, 550)]
    adipose_patches = []
    for loc in adipose_locations:
        adipose_patches.append(image_grey[loc[0]:loc[0] + PATCH_SIZE,
                                 loc[1]:loc[1] + PATCH_SIZE])
    # compute some GLCM properties each patch
    global us
    us = []
    global vs
    vs = []
    global ws
    ws = []
    global xs
    xs = []
    global ys
    ys = []
    global zs
    zs = []
    for i, patch in enumerate(spleen_patches + adipose_patches):
        glcm = greycomatrix(patch, [5], [0], 256, symmetric=True, normed=True)
    
        us.append(greycoprops(glcm, 'ASM')[0, 0])    
        vs.append(greycoprops(glcm, 'contrast')[0, 0])
        ws.append(greycoprops(glcm, 'energy')[0, 0])    
        xs.append(greycoprops(glcm, 'dissimilarity')[0, 0])
        ys.append(greycoprops(glcm, 'correlation')[0, 0])
        zs.append(greycoprops(glcm, 'homogeneity')[0, 0])

    # create the figure
    plt.figure(figsize=(12, 12))

    # display the image patches
    for i, patch in enumerate(spleen_patches):
        plt.subplot(3, len(spleen_patches), len(spleen_patches) * 1 + i + 1)
        plt.imshow(patch, cmap=plt.cm.gray, interpolation='nearest',
               vmin=0, vmax=255)
        plt.xlabel('Spleen %d' % (i + 1))

    for i, patch in enumerate(adipose_patches):
        plt.subplot(3, len(spleen_patches), len(spleen_patches) * 2 + i + 1)
        plt.imshow(patch, cmap=plt.cm.gray, interpolation='nearest',
                   vmin=0, vmax=255)
        plt.xlabel('Adipose %d' % (i + 1))

    # display original image with locations of patches
    plt.subplot(3, 2, 1)
    plt.imshow(image_grey, cmap=plt.cm.gray, interpolation='nearest',
               vmin=0, vmax=255)
    for (y, x) in spleen_locations:
        plt.plot(x + PATCH_SIZE / 2, y + PATCH_SIZE / 2, 'gs')
    for (y, x) in adipose_locations:
        plt.plot(x + PATCH_SIZE / 2, y + PATCH_SIZE / 2, 'bs')
    plt.xlabel('Original Image')
    plt.xticks([])
    plt.yticks([])
    plt.axis('image')

    # for each patch, plot (dissimilarity, correlation)
    plt.subplot(3, 2, 2)
    plt.plot(xs[:len(spleen_patches)], ys[:len(spleen_patches)], 'go',
             label='Spleen')
    plt.plot(xs[len(spleen_patches):], ys[len(spleen_patches):], 'bo',
             label='Adipose')
    plt.xlabel('GLCM Dissimilarity')
    plt.ylabel('GLVM Correlation')
    plt.legend()

    # display the patches and plot
    plt.suptitle('Grey level co-occurrence matrix features', fontsize=14)
    plt.show()
    #print(len(spleen_patches))
    



