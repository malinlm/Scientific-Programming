def number_na(df):
    """
    Takes in a pandas dataframe and returns a pandas dataframe
    of the number and percentage of NaN values in each column of the df
    """
    
    import pandas as pd
    
    number_na = pd.DataFrame()
    number_na['Count of NaN'] = df.isna().sum()
    number_na['Percentage (%) of NaN'] = (df.isna().sum() / len(df)) * 100
    
    return number_na

def visualize_unique_values(df, col, dropna=False):
    
    """
    """
    
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    unique = df[col].value_counts(dropna=dropna)   
    unique_values = pd.DataFrame(unique)

    display(unique_values)
    plt.figure(figsize=(7,5))
    figure = sns.displot(df[col])
    
    return unique_values, figure

def trans_str_to_int(df, col):
    #make a list of mappings
    from sklearn.preprocessing import LabelEncoder

    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col])

    return df