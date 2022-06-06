def PlotPCA(principal_texture_Df, df_norm):
    plt.figure()
    plt.figure(figsize=(10,10))
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=14)
    plt.xlabel('Principal Component - 1',fontsize=20)
    plt.ylabel('Principal Component - 2',fontsize=20)
    plt.title("Principal Component Analysis of Texture Dataset",fontsize=20)
    targets = ['spleen', 'adipose']
    colors = ['r', 'g']
    for target, color in zip(targets,colors):
        indicesToKeep = df_norm['label'] == target
        plt.scatter(principal_texture_Df.loc[indicesToKeep, 'principal component 1']
                   , principal_texture_Df.loc[indicesToKeep, 'principal component 2'], c = color, s = 50)

    plt.legend(targets,prop={'size': 15})
