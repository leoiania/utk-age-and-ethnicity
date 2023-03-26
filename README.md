# UTK Ethnicity and Age prediction

This project was done for the Deep Learning for AI course.
Starting from the UTK Face Dataset we created two different neural networks to predict the ethnicity and the age of the people in the dataset using their pictures.

The labels are written in the file name - there is also the sex label, but we didn't use it.

## The metric problem in age regression

As you will see reading the age notebook, predicting a real (continuous) value for the age, instead of creating 100+ categories, lead to a problem: there are no reliable metrics to manage, during the training, to check the results.

This is why we decided to look at some "critical" percentiles of the predicted distribution, because we noticed that our model, in the first epochs and then after a lot of epochs, tended to return the same "average" value.
For this reason, we created a custom early-stopping metric, which was the sum of the absolute difference between the true percentiles values and the predicted ones, to make the training stop after reaching an enough similar distribution.

## In reading the projects, you should follow this order:

1. [Ethnicity classification](https://github.com/leoiania/utk-age-and-ethnicity/blob/master/notebooks/ethnicity_classification.ipynb)
2. [Age regression](https://github.com/leoiania/utk-age-and-ethnicity/blob/master/notebooks/age_regression.ipynb)
