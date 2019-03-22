# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:43:10 2019

@author: Azni Aziz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')

df.info()
df.head()

cancer_df=df.drop(['id','Unnamed: 32'], axis =1)
cancer_df=pd.get_dummies(cancer_df,'diagnosis',drop_first=True)

cancer_df.head()

sns.countplot(x='diagnosis',data = df, palette='BrBG')

colors = np.array('b g r c m y k'.split())

fig,axes = plt.subplots(nrows =15, ncols=2, sharey=True, figsize =(15,50))
plt.tight_layout()
row=0
iteration=0
for j in range (0,len(cancer_df.columns[:-1])):
    iteration +=1
    if (j%2 == 0):
        k=0
    else:
        k=1
    
    sns.distplot(cancer_df[cancer_df.columns[j]],kde=False,hist_kws=dict(edgecolor="w", linewidth=2),color=
    np.random.choice(colors), ax=axes[row][k])
    if(iteration%2==0):
        row+=1
        plt.ylim(0,200)

plt.figure(figsize =(10,3))
sns.barplot(x='radius_mean',y='texture_mean',data =df, hue= 'diagnosis',palette='viridis')
plt.xlabel('Mean Radius of the lump')
plt.ylabel('Texture of the lump')

        