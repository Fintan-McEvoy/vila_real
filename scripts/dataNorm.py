def DataNorm():
    global x
    x = df.values #returns a numpy array
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)

    global df_norm
    df_norm = pd.DataFrame(x_scaled,index = index_values, columns = column_values)
    label = ['spleen', 'spleen', 'spleen', 'spleen', 'adipose','adipose','adipose','adipose']
    df_norm['label'] = label
    targets=['spleen','adipose']
    return(df_norm)

