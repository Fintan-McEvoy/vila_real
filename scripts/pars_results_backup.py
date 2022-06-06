def im_segment(im_name, YOLO_result_file):
	pwd=os.getcwd()
	print(pwd)
	path = Path(pwd)
	segmented_image_path=(path.parent.absolute())
	im_name=os.path.join(pwd,im_name)
	print(os.path.join(pwd,"result.txt"))
	df=pd.read_table(os.path.join(pwd,"result.txt"), delim_whitespace=False, header=None, skipinitialspace=True)

	r_center_x=float(df.loc[2,0][0:6])
	r_center_y=float(df.loc[2,0][9:15])
	r_width=float(df.loc[2,0][18:24])
	r_height=float(df.loc[2,0][27:33])
	
	
	l_center_x=float(df.loc[4,0][0:6])
	l_center_y=float(df.loc[4,0][9:15])
	l_width=float(df.loc[4,0][18:24])
	l_height=float(df.loc[4,0][27:33])
	
	if r_center_x > l_center_x:

		l_center_x=df.loc[2,0][0:6]
		l_center_y=df.loc[2,0][9:15]
		l_width=df.loc[2,0][18:24]
		l_height=df.loc[2,0][27:33]


		r_center_x=df.loc[4,0][0:6]
		r_center_y=df.loc[4,0][9:15]
		r_width=df.loc[4,0][18:24]
		r_height=df.loc[4,0][27:33]
	

	img=cv2.imread(im_name)
	img_height, img_width, img_channel = np.shape(img)
	img_height=float(img_height)
	img_width=float(img_width)
    

	abs_r_center_x=(r_center_x)*(img_width)
	abs_r_center_y=(r_center_y)*(img_height)
	bb_width_r=float(r_width*img_width)
	bb_height_r=float(r_height*img_height)
	x_up = int(abs_r_center_x - (bb_width_r/2))
	y_up = int(abs_r_center_y - (bb_height_r/2))
	x_down = int(abs_r_center_x + (bb_width_r/2))
	y_down = int(abs_r_center_y + (bb_height_r/2))
	croped_image = img[y_up:y_down, x_up:x_down]
#cv2.imwrite(os.path.join(pwd+'/darknet/data/croped_r_images/'+file), cropped_image)
	cv2.imwrite(os.path.join(segmented_image_path,'score/data/images/r_croped_image.png'), croped_image)
 
	abs_l_center_x=(l_center_x)*(img_width)
	abs_l_center_y=(l_center_y)*(img_height)
	bb_width_l=float(l_width*img_width)
	bb_height_l=float(l_height*img_height)
#print(bb_height_l)
	x_up = int(abs_l_center_x - (bb_width_l/2))
	y_up = int(abs_l_center_y - (bb_height_l/2))
	x_down = int(abs_l_center_x + (bb_width_l/2))
	y_down = int(abs_l_center_y + (bb_height_l/2))
	croped_image = img[y_up:y_down, x_up:x_down]
#cv2.imwrite(os.path.join('/run/media/czv164/886F-127B/croped_l_images/'+file), cropped_image)
	cv2.imwrite(os.path.join(segmented_image_path,'score/data/images/l_croped_image.png'), croped_image) 



#im_segment('predictions.jpg', 'result.txt')

           

