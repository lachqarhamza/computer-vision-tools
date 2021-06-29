from sklearn.decomposition import PCA

# compute a PCA (eigenfaces) on the olivetti dataset

# dimensionality reduction
n_components = 150

pca = PCA(n_components = n_components, svd_solver = 'randomized',
        whiten = true).fit(Xtrain)
