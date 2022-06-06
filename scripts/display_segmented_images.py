def display_images():
    fig = plt.figure()
    ax1 = fig.add_subplot(1,2,1)
    ax1.imshow(os.path.join(home,"/images/r_croped_image"), cmap='gray_r',vmin=0,vmax=1)
    ax2 = fig.add_subplot(1,2,2)
    ax2.imshow(os.path.join(home,"/images/l_croped_image"), cmap='gray_r',vmin=0,vmax=1)


    ax1.axes.get_xaxis().set_visible(False)
    ax1.axes.get_yaxis().set_visible(False)
    ax1.axes.set_title('Right')

    ax2.axes.get_xaxis().set_visible(False)
    ax2.axes.get_yaxis().set_visible(False)
    ax2.axes.set_title('Left')


