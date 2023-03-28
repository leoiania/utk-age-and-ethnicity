# UTK Ethnicity and Age prediction

This project was done for the Deep Learning for AI course.
Starting from the UTK Face Dataset we created two different neural networks to predict the ethnicity and the age of the people in the dataset using their pictures.

The labels are written in the file name - there is also the sex label, but we didn't use it.

## Streamlit app - Published!

##### [Streamlit app link](https://leoiania-utk-age-and-ethnicity-app-l3szgo.streamlit.app/)

Some months after presenting this project for Deep Learning exam, I decided to use it for applying Streamlit knowledge for the creation of an interactive app that, given a picture uploaded by the user, returns the predicted age .

<img src="age_preds.gif" alt="gif" width="800" height="450">

## The metric problem in age regression

As you will see reading the age notebook, predicting a real (continuous) value for the age, instead of creating 100+ categories, lead to a problem: there are no reliable metrics to manage, during the training, to check the results.

This is why we decided to look at some "critical" percentiles of the predicted distribution, because we noticed that our model, in the first epochs and then after a lot of epochs, tended to return the same "average" value.
For this reason, we created a custom early-stopping metric, which was the sum of the absolute difference between the true percentiles values and the predicted ones, to make the training stop after reaching an enough similar distribution.


## Project Guide:

In notebooks, you can find a reasoning and the model training notebook (original) used for the exam. The age_regression notebook is the one the model comes from, but both the training was made using Google Colab.

In src there are the module defined by me in making the app

templates folder contains the html files needed for the **flask** app - the main file is app_flask (old)

the file `app.py` is the one that contains the Streamlit app code - is the one that I recommend to try

> NB: the model will be updated making it capable to obtain better results in age predictions


## In reading the projects, you should follow this order:

1. [Ethnicity classification](https://github.com/leoiania/utk-age-and-ethnicity/blob/master/notebooks/ethnicity_classification.ipynb)
2. [Age regression](https://github.com/leoiania/utk-age-and-ethnicity/blob/master/notebooks/age_regression.ipynb)
