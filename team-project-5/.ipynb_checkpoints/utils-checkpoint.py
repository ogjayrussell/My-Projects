import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
import math

def create_indices(df:pd.DataFrame):
  """Takes a pandas dataframe and returns two columns:
  1. an interaction term column
  2. an index to represent the metrics in the dataframe.
  The most recent time interval of this index is always a 100 baseline."""
  
  # Making a copy of the dataframe before mathematical operations
  df1 = df.copy()

  # Creating an interaction term
  df1['interaction_term'] = df1.prod(axis=1)

  # initializing index column
  df1['made_index'] = 100

  # Creating the "boundaries" of the index
  df1.loc[df1['made_index'] == 100, 'made_index'] = np.nan
  df1['made_index'].iloc[-1] = 100
  df1.loc[df1['interaction_term'] == df1['interaction_term'].max(), 'made_index'] = 200
  df1.loc[df1['interaction_term'] == df1['interaction_term'].min(), 'made_index'] = 0

  # initializing packages
  lr = LinearRegression()
  mms = MinMaxScaler()

  # Setting training and testing data, nulls = rows with null index values
  train = df1[df1['made_index'].isnull() == False]
  nulls = df1[df1['made_index'].isnull() == True]

  # Creating y/target
  y = train['made_index']
  train = train.drop(columns=['made_index'])
  nulls = nulls.drop(columns=['made_index'])

  # Scaling
  Xs_train = mms.fit_transform(train)
  Xs_nulls = mms.transform(nulls)

  # Fit and Predict
  lr.fit(Xs_train, y)
  pred = lr.predict(Xs_nulls)

  # Putting predictings into null made_index
  nulls['made_index'] = pred

  # Imputation
  df1['made_index'].fillna(nulls['made_index'], inplace=True)
  df1.index = df.index

  return df1


def sub_box_plot(df:pd.DataFrame, title):
  """Takes a pandas dataframe and returns boxplot subplots."""

  # Checks for datetime index
  df.index = pd.to_datetime(df.index)

  # Figure for subplots (boxplots)
  plt.figure(figsize=(16, 60))
  plt.subplots_adjust(hspace=0.1)
  plt.suptitle(title, fontsize=18, y=0.99) 

  for i, v in enumerate(df):
      # add a new subplot iteratively
      ax = plt.subplot(math.ceil(len(df.columns)), 2, i + 1)

      df.boxplot(v, vert=False, ax=ax)
    
      # chart formatting
      ax.set_title(v.upper())
      ax.set_xlabel("")

  plt.tight_layout(rect=[0, 0.03, 1, 0.99])
  plt.show()

def line_plot(df:pd.DataFrame, title, xlabels, ylabels):
  """Takes a pandas dataframe and returns a lineplot of all features."""

  # Checks for datetime index
  df.index = pd.to_datetime(df.index)

  # Figure for lineplot
  plt.figure(figsize=(20, 20))
  plt.title(title)
  
  for col in df:
    plt.plot(df.index, df[col], label=col)

  plt.legend()
  plt.xlabel(xlabels)
  plt.ylabel(ylabels)
  plt.show()

def eda_charts(df:pd.DataFrame, period=30, lags=15):
    """
    Takes a pandas dataframe and returns a series of charts
    for every feature in that dataframe:
     - histogram
     - boxplot
     - lineplot 
     - difference lineplot
     - percentage change lineplot
     - seasonal decomposition
     - acf plot
     - pacf plot
       """
    
    # Datetime Index check
    df.index = pd.to_datetime(df.index)

    # Descriptive statistics
    print(df.describe().T) #AS 7/6 added for formatting
    print()
    print(df.info())
    print()

    # Plots
    for col in df.resample('Y').mean():
        # Histogram
        plt.figure(figsize=(16, 9))
        plt.title(f'Histogram - {col.title()}')
        plt.hist(df[col], bins='fd')
        plt.tight_layout()

        # Boxplot
        plt.figure(figsize=(16, 9))
        plt.title(f'Boxplot - {col.title()}')
        plt.boxplot(df[col], vert=False)
        plt.tight_layout()

        # Lineplot
        plt.figure(figsize=(16, 9))
        plt.title(f'Lineplot - {col.title()}')
        plt.plot(df[col], linewidth=1)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Difference Lineplot
        #AS 7/6 added for completeness
        df1 = pd.DataFrame()
        df1['diff'] = df[[col]].diff()
        plt.figure(figsize=(16, 9))
        plt.title(f'Lineplot - {col.title()} Difference')
        plt.plot(df1['diff'], linewidth=1)
        plt.xticks(rotation=45)
        plt.tight_layout()      
        
        # Pct Change Lineplot
        df1 = pd.DataFrame()
        df1['pct_change'] = df[[col]].pct_change()
        plt.figure(figsize=(16, 9))
        plt.title(f'Lineplot - {col.title()} Percentage Change')
        plt.plot(df1['pct_change'], linewidth=1)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Seasonal Decompose Plot - Checks for stationarity, trend, and seasonality
        fig = seasonal_decompose(df[col].dropna(), period=period).plot()
        fig = plt.gcf()
        # plt.title('Seasonal Decomposition') #AS 7/6 can't figure out how to add a custom title here
        fig.set_size_inches(16,9)
        fig.set_tight_layout(True)

        # ACF Plot - Checks for autocorrelation/serial correlation
        fig = plot_acf(df[col].dropna(), lags=lags, alpha=0.01)
        fig = plt.gcf()
        fig.set_size_inches(16,9)
        fig.set_tight_layout(True)
        
        # PACF Plot - Checks for partial autocorrelation/serial correlation
        fig = plot_pacf(df[col].dropna(), lags=lags, alpha=0.1, method='ywm')
        fig = plt.gcf()
        fig.set_size_inches(16,9)
        fig.set_tight_layout(True)        

