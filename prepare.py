import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

def create_viable(df):
    df['is_viable'] = df['quality']>5

    return df

def split_wine(df):
    '''
    This function performs split on WineQT data, stratify quality.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.quality)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.quality)
    return train, validate, test