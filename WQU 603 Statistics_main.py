import numpy as np
import pandas as pd
import seaborn as sns

dfMSFT = pd.read_csv('MSFT.csv',header=0,index_col=0,na_values='NaN')
dfTSLA = pd.read_csv('TSLA.csv',header=0,index_col=0,na_values='NaN')
dfMSFT = dfMSFT.sort_index()
dfTSLA = dfTSLA.sort_index()
dfData = pd.DataFrame()
dfData['X1']=dfMSFT['open'].pct_change()
dfData['X2']=dfTSLA['open'].pct_change()
dfData = dfData.dropna()
dfSample = dfData.sample(n=30)
dfSample = dfSample.sort_index()

import seaborn as sns
from scipy import stats as scpstats
sns.distplot(dfSample['X1'],hist=True,kde=False,fit=scpstats.t)
sns.distplot(dfSample['X2'],hist=True,kde=False,fit=scpstats.norm)
