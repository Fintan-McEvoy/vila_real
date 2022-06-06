def GCM():
    #Generate df of greycomatrix parameters
    #create a list of columns names
    global column_values
    column_values = ['ASM', 'contrast','energy','dissimilarity', 'correlation', 'homogeneity']
    #create list of index values
    global index_values
    index_values = ['spleen_1','spleen_2','spleen_3','spleen_4','adipose_1','adipose_2','adipose_3','adipose_4']
    
    global array
    array=np.array([
        [us[0], vs[0], ws[0], xs[0], ys[0], zs[0]],
        [us[1], vs[1], ws[1], xs[1], ys[1], zs[1]],
        [us[2], vs[2], ws[2], xs[2], ys[2], zs[2]],
        [us[3], vs[3], ws[3], xs[3], ys[3], zs[3]],
        [us[4], vs[4], ws[4], xs[4], ys[4], zs[4]],
        [us[5], vs[5], ws[5], xs[5], ys[5], zs[5]],
        [us[6], vs[6], ws[6], xs[6], ys[6], zs[6]],
        [us[7], vs[7], ws[7], xs[7], ys[7], zs[7]]
        ])

    # creating the dataframe
    global df
    df = pd.DataFrame(data = array, index = index_values, columns = column_values)
    

    x = df.values #returns a numpy array
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)


   
  
  
    # displaying the dataframe
   
    return(df)

#def DataNorm():
 #   global x
#    x = df.values #returns a numpy array
#    min_max_scaler = preprocessing.MinMaxScaler()
#    x_scaled = min_max_scaler.fit_transform(x)
#
#   global df_norm
#    df_norm = pd.DataFrame(x_scaled,index = index_values, columns = column_values)
#    label = ['spleen', 'spleen', 'spleen', 'spleen', 'adipose','adipose','adipose','adipose']
 #   df_norm['label'] = label
 #   targets=['spleen','adipose']
 #   df_norm

