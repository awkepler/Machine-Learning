Diffrence Between PCA and Kernel PCA:

Kernel PCA just performs PCA in a new space. It uses Kernel trick to find principal components in different space (Possibly High Dimensional Space). PCA finds new directions based on covariance matrix of original variables. It can extract maximum P (number of features) eigen values.

PCA (as a dimensionality reduction technique) tries to find a low-dimensional linear subspace that the data are confined to. But it might be that the data are confined to low-dimensional nonlinear subspace. What will happen then?

Take a look at this Figure, taken from Bishop's "Pattern recognition and Machine Learning" textbook (Figure 12.16):

![alt text](https://github.com/awkepler/Machine_Learning_Adventure/blob/master/9%20-%20Dimensionality%20Reduction/D7vyt.png?raw=true)

kernel PCA from Bishop's ML book

The data points here (on the left) are located mostly along a curve in 2D. PCA cannot reduce the dimensionality from two to one, because the points are not located along a straight line. But still, the data are "obviously" located around a one-dimensional non-linear curve. So while PCA fails, there must be another way! And indeed, kernel PCA can find this non-linear manifold and discover that the data are in fact nearly one-dimensional.

It does so by mapping the data into a higher-dimensional space. This can indeed look like a contradiction (your question #2), but it is not. The data are mapped into a higher-dimensional space, but then turn out to lie on a lower dimensional subspace of it. So you increase the dimensionality in order to be able to decrease it.

The essence of the "kernel trick" is that one does not actually need to explicitly consider the higher-dimensional space, so this potentially confusing leap in dimensionality is performed entirely undercover. The idea, however, stays the same.
