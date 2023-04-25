# Classification Project: Wine Quality

# Project Description
Wine Company wants to investigate drivers of wine quality and achieve actionable insights.

# Project Goal
- Discover drivers of wine quality in WineQT dataset.
- Use drivers to develop a machine learning model to classify wine as quality 3-5 or 6-8.
- A quality is the rating given by reviews of the wine.
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
| Churn | True or False, Churned customers have left the company |
| Multiple Lines | True or False, customer has phone service with multiple lines or not |
| Dependents | True or False, customer has dependents or not |
| Partner | True or False, customer has a partner or not |
| Senior Citizen | True or False, customer is a senior citizen or not |
| Internet Service | True or False, customer has internet service or not |
| Tenure | An integer that shows the number of months a customer has been with the company |

# Steps to Reproduce
1. Clone this repo
2. Acquire the data from SQL database
3. Place data in file containing the cloned repo
4. Run notebook

# Takeaways and Conclusions
- Churn occurs in 27% of customers
- Customers who do not have a partner have a 13% higher chance of churning
- Customer who do not have dependents have a 15% higher chance of churning
- Customers who are senior citizens have a 20% higher chance of churning
- Customers who do not have internet service have a 25% higher chance of churning
- Having multiple lines with phone service is a driver of churn with weak influence
- Model performs 6% higher than baseline predictions.

# Recommendations
- Possible limited time discounts to customers who are likely to churn within the featured demographics.
