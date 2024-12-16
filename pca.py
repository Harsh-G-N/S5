import pandas as pd
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


iris = load_iris()
X = iris.data[:, :4]
y = iris.target


pca = PCA(n_components=3)
col = pca.fit_transform(X)
df = pd.DataFrame(col, columns=['PC1', 'PC2', 'PC3'])
df['target'] = y


colors = ['yellow', 'green', 'blue']
markers = ['o', 's', '^']  # Circle, square, triangle


fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

for i in range(3): 
    ax.scatter(df.loc[y == i, 'PC1'], df.loc[y == i, 'PC2'], df.loc[y == i, 'PC3'],
               color=colors[i], marker=markers[i], 
               label=iris.target_names[i], alpha=0.7, edgecolor='k')


ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_zlabel('Principal Component 3')
ax.set_title('3D PCA of Iris Dataset')
ax.legend(title='Species')
plt.show()
