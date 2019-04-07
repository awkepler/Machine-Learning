# XGBoost Features

The library is laser focused on computational speed and model performance, as such there are few frills. 
Nevertheless, it does offer a number of advanced features.

## Model Features
The implementation of the model supports the features of the scikit-learn and R implementations, with new additions 
like regularization. Three main forms of gradient boosting are supported:

##### Gradient Boosting algorithm also called gradient boosting machine including the learning rate.
##### Stochastic Gradient Boosting with sub-sampling at the row, column and column per split levels.
##### Regularized Gradient Boosting with both L1 and L2 regularization.

## System Features
The library provides a system for use in a range of computing environments, not least:

##### Parallelization of tree construction using all of your CPU cores during training.
##### Distributed Computing for training very large models using a cluster of machines.
##### Out-of-Core Computing for very large datasets that don’t fit into memory.
##### Cache Optimization of data structures and algorithm to make best use of hardware.

## Algorithm Features
The implementation of the algorithm was engineered for efficiency of compute time and memory resources. A design goal was to make the best use of available resources to train the model. Some key algorithm implementation features include:

##### Sparse Aware implementation with automatic handling of missing data values.
##### Block Structure to support the parallelization of tree construction.
##### Continued Training so that you can further boost an already fitted model on new data.

# Why Use XGBoost?
The two reasons to use XGBoost are also the two goals of the project:

1. XGBoost Execution Speed
Generally, XGBoost is fast. Really fast when compared to other implementations of gradient boosting.

2. XGBoost Model Performance
XGBoost dominates structured or tabular datasets on classification and regression predictive modeling problems.

## How does it work?

Before moving on to the details of the algorithm, let’s set some basic definitions to make our life easier and get an intuitive and complete understanding of this popular tool.

First, let’s clarify the concept of boosting. This is an ensemble method that seeks to create a strong classifier (model) based on “weak” classifiers. In this context, weak and strong refer to a measure of how correlated are the learners to the actual target variable. By adding models on top of each other iteratively, the errors of the previous model are corrected by the next predictor, until the training data is accurately predicted or reproduced by the model. If you want to dig into boosting a bit more, check out information about a popular implementation called AdaBoost (Adaptive Boosting) here.

Now, gradient boosting also comprises an ensemble method that sequentially adds predictors and corrects previous models. However, instead of assigning different weights to the classifiers after every iteration, this method fits the new model to new residuals of the previous prediction and then minimizes the loss when adding the latest prediction. So, in the end, you are updating your model using gradient descent and hence the name, gradient boosting. This is supported for both regression and classification problems. XGBoost specifically, implements this algorithm for decision tree boosting with an additional custom regularization term in the objective function.
