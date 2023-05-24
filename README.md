# Classification Project: Wine Quality

# Project Description
Wine Company wants to investigate drivers of wine quality and achieve actionable insights.

# Project Goal
- Discover drivers of wine quality in WineQT dataset.
- Use drivers to develop a machine learning model to classify wine as a viable product or not a viable product.
- A quality is the rating given by reviews of the wine.
- For this project we will define a viable product as a wine with a quality of 6 or higher.
- Wines with quality 5 or below will not be viable products.
- This information could be used to reach a better understanding of why wines are rated high or low.

# Initial Thoughts
My initial hypothesis is that drivers of quality will likely be features that affect a wine's flavor, such as ph, alcohol percentage, and different acidities.

# Plan
- Acquire data from Kaggle

- Prepare data by encoding strings, renaming columns, dropping unnecessary columns

- Explore data in search of drivers of upsets and answer the following:

>Does acidity share a relationship with quality?

>Does residual sugar affect quality?

>Does sulfur dioxide affect quality?

>Does pH affect quality?

>Does amount of sulphates affect quality?

>Does alcohol content affect quality?

- Develop a model to predict if a win will be of quality 3-5 or 6-8
> Use drivers identified in explore to build predictive models

> Evaluation of models on train and validate data

> Select best model based on highest accuracy

> Evaluation of best model on test data

- Draw conclusions

# Data Dictionary
| Feature | Definition |
| :- | :- |
| quality | A numeric score based on reviews of the wine by consumers |
| fixed acidity | set of low volatility organic acids such as malic, lactic, tartaric or citric acids. |
| volatile acidity | a measure of the wine's volatile (or gaseous) acids. The primary volatile acid in wine is acetic acid, which is also the primary acid associated with the smell and taste of vinegar. |
| citric acid | a measure of acid that is often added to wines to increase acidity, complement a specific flavor or prevent ferric hazes. |
| residual sugar | sweetness in wine measured in grams per liter (g/L) of sugar. |
| chlorides | a measure of salts of mineral and organic acids that affects the saltiness of flavor in wine. |
| free sulfur dioxide | a measure of sulphur dioxide ions that are not chemically bound to other chemicals in solution and thus are free to react with substances |
| density | mass of a unit volume of a material substance (in this case, the wine) |
| pH | a figure expressing the acidity or alkalinity of a solution (in this case, the wine) |
| sulphites | continuous variable, measured in ppm (parts per million), naturally occurring compounds found in all wines; they act as a preservative by inhibiting microbial growth.  |
| alcohol | measurement of alcohol content in wine |

# Steps to Reproduce
1. Clone this repo
2. Acquire the data from csv saved in repo
3. Place data in file containing the cloned repo
4. Run notebook

# Takeaways and Conclusions
- Drivers of quality were found to be 
# Recommendations
- 
