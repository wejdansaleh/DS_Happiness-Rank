
# import an entire library
import math # Functions beyond the basic maths



# Import an entire library and give it an alias
import pandas as pd # For DataFrame and handling
import numpy as np # Array and numerical processing
import matplotlib.pyplot as plt # Low level plottingsource .venv/bin/activate
import seaborn as sns # High level Plotting
import statsmodels.api as sm # Modeling, e.g. ANOVA
import plotly.express as px

## loading  dataset
df_2017 = pd.read_csv("data/2017.csv")
df_2018 = pd.read_csv("data/2018.csv")
df_2019 = pd.read_csv("data/2019.csv")

## Clean data and rename some column to easier to join.
df_2017['year'] = 2017
df_2018['year'] = 2018
df_2019['year'] = 2019

df_2017.rename({'Happiness.Rank': 'Rank',
'Happiness.Score':'Score',
'Economy..GDP.per.Capita.':'Economy',
'Health..Life.Expectancy.':'Healthy',
'Freedom to make life choices':'Freedom',
'Trust..Government.Corruption.':'Government corruption'}, axis=1, inplace=True)
df_2017.head()

df_2018.rename({'Overall rank': 'Rank',
'GDP per capita':'Economy',
'Healthy life expectancy':'Healthy',
'Freedom to make life choices':'Freedom',
'Perceptions of corruption':'Government corruption'}, axis=1, inplace=True)
df_2018.head()

df_2019.rename({'Overall rank': 'Rank',
'GDP per capita':'Economy',
'Healthy life expectancy':'Healthy',
'Freedom to make life choices':'Freedom',
'Perceptions of corruption':'Government corruption'}, axis=1, inplace=True)
df_2019.head()


## Combine df_2019, df_2018, and  df_2017
df_join = pd.concat([df_2018, df_2019,df_2017])

# Calculate the mean and standard deviation for each group.
#df1 = df_join.groupby(['year']).mean()
meanScore = df_join.groupby(['year'])['Score'].mean()
print(meanScore)
stdScore = df_join.groupby(['year'])['Score'].std()
print(stdScore)

# corrleation data
corrMatrix = df_join.corr()
sns.heatmap(corrMatrix, annot=True)
plt.suptitle("Correlation Map", fontsize=20)
plt.show()

## Happiness Score Vs Economy
p1 = sns.FacetGrid(df_join, col = "year", hue = "year", col_wrap=3)
p1.map(sns.scatterplot, "Economy", "Score")
p1.add_legend()
plt.show()


 #Happiness Score Vs Healthy

p2 = sns.FacetGrid(df_join, col = "year", hue = "year", col_wrap=3)
p2.map(sns.scatterplot, "Healthy", "Score")
p2.add_legend()
plt.show()

# Happiness Score Vs  Freedom
p3 = sns.FacetGrid(df_join, col = "year", hue = "year", col_wrap=3)
p3.map(sns.scatterplot, "Freedom", "Score")
p3.add_legend()
plt.show()

#Calculate a 1-way ANOVA
from statsmodels.formula.api import ols
lm = ols('Score ~ year', data=df_join).fit()
anovatest = sm.stats.anova_lm(lm)

