def generalImageFile(input_image):
	if input_image[-3:]=='jpg':
		shutil.copy(os.path.join(cwd,"images",input_image),os.path.join(cwd,'demo/data/images',"activeImage.jpg"))
		shutil.copy(os.path.join(cwd,"images",input_image),os.path.join(cwd,'segment/data/images',"activeImage.jpg"))
	if input_image[-3:]== 'png':
		shutil.copy(os.path.join(cwd,"images",input_image),os.path.join(cwd,'demo/data/images',"activeImage.png"))
		shutil.copy(os.path.join(cwd,"images",input_image),os.path.join(cwd,'segment/data/images',"activeImage.png"))

		
	
	
