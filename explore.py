#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats


# In[1]:


def get_countplot(train):
    sns.countplot(x=train.quality)


# In[2]:


def get_countplot_viable(train):
    sns.countplot(x=train.is_viable)


# In[3]:


def get_volatile_boxplot(train):
    sns.boxplot(data=train, x=train['quality'],y=train['volatile acidity'])


# In[5]:


def get_ttest_volatile(train):

    viable_sample=train[train.is_viable==True]['volatile acidity']
    not_viable_sample=train[train.is_viable==False]['volatile acidity']
    overall_mean = train['volatile acidity'].mean()

    t, p = stats.ttest_ind(not_viable_sample, viable_sample, equal_var=False)
    print(f't     = {t:.4f}')
    print(f'p     = {p:.4f}')


# In[6]:


def get_citric_boxplot(train):
    sns.boxplot(data=train, x=train['quality'],y=train['citric acid'])


# In[7]:


def get_ind_ttest_citric_acid(train):

    viable_sample=train[train.is_viable==True]['citric acid']
    not_viable_sample=train[train.is_viable==False]['citric acid']
    overall_mean = train['citric acid'].mean()

    t, p = stats.ttest_ind(not_viable_sample, viable_sample, equal_var=False)
    print(f't     = {t:.4f}')
    print(f'p     = {p:.4f}')


# In[8]:


def get_fixed_acid_boxplot(train):
    sns.boxplot(data=train, x=train['quality'],y=train['fixed acidity'])


# In[9]:


def get_ind_ttest_fixed_acid(train):

    viable_sample=train[train.is_viable==True]['fixed acidity']
    not_viable_sample=train[train.is_viable==False]['fixed acidity']
    overall_mean = train['fixed acidity'].mean()

    t, p = stats.ttest_ind(not_viable_sample, viable_sample, equal_var=False)
    print(f't     = {t:.4f}')
    print(f'p     = {p:.4f}')


# In[10]:


def get_pH_boxplot(train):
    sns.boxplot(data=train, x=train['quality'],y=train['pH'])


# In[11]:


def get_ind_ttest_ph(train):

    viable_sample=train[train.is_viable==True]['pH']
    not_viable_sample=train[train.is_viable==False]['pH']
    overall_mean = train['pH'].mean()

    t, p = stats.ttest_ind(not_viable_sample, viable_sample, equal_var=False)
    print(f't     = {t:.4f}')
    print(f'p     = {p:.4f}')


# In[12]:


def get_sulphates_boxplot(train):
    sns.boxplot(data=train, x=train['quality'],y=train['sulphates'])


# In[13]:


def get_ind_ttest_sulphates(train):

    viable_sample=train[train.is_viable==True]['sulphates']
    not_viable_sample=train[train.is_viable==False]['sulphates']
    overall_mean = train['sulphates'].mean()

    t, p = stats.ttest_ind(not_viable_sample, viable_sample, equal_var=False)
    print(f't     = {t:.4f}')
    print(f'p     = {p:.4f}')


# In[14]:


def get_alcohol_boxplot(train):
    sns.boxplot(data=train, x=train['quality'],y=train['alcohol'])


# In[15]:


def get_ind_ttest_alcohol(train):

    viable_sample=train[train.is_viable==True]['alcohol']
    not_viable_sample=train[train.is_viable==False]['alcohol']
    overall_mean = train['alcohol'].mean()

    t, p = stats.ttest_ind(not_viable_sample, viable_sample, equal_var=False)
    print(f't     = {t:.4f}')
    print(f'p     = {p:.4f}')


# In[16]:


def get_residual_sugar_boxplot(train):
    sns.boxplot(data=train, x=train['quality'],y=train['residual sugar'])


# In[17]:


def get_ind_ttest_residsugar(train):

    viable_sample=train[train.is_viable==True]['residual sugar']
    not_viable_sample=train[train.is_viable==False]['residual sugar']
    overall_mean = train['residual sugar'].mean()

    t, p = stats.ttest_ind(not_viable_sample, viable_sample, equal_var=False)
    print(f't     = {t:.4f}')
    print(f'p     = {p:.4f}')


# In[18]:


def get_ind_ttest_free_sulf_dio(train):

    viable_sample=train[train.is_viable==True]['free sulfur dioxide']
    not_viable_sample=train[train.is_viable==False]['free sulfur dioxide']
    overall_mean = train['free sulfur dioxide'].mean()

    t, p = stats.ttest_ind(not_viable_sample, viable_sample, equal_var=False)
    print(f't     = {t:.4f}')
    print(f'p     = {p:.4f}')


# In[ ]:




