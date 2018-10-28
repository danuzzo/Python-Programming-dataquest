
# coding: utf-8

# In[247]:


import pandas as pd
star_wars = pd.read_csv("star_wars.csv", encoding="ISO-8859-1")

star_wars.head(10)


# In[248]:


# See the columns
star_wars.columns


# In[249]:


# Remove NaN from Respondent ID
star_wars.dropna(axis=0,subset=['RespondentID'], inplace=True)

star_wars.head(10)


# In[250]:


# Convert column "Have you seen..." into boolean
yes_no = {
    "Yes": True,
    "No": False
}

column = "Have you seen any of the 6 films in the Star Wars franchise?"
star_wars[column] = star_wars[column].map(yes_no)

star_wars.head(10)


# In[251]:


# Convert column "Do you consider..." into boolean
yes_no = {
    "Yes": True,
    "No": False
}

column = "Do you consider yourself to be a fan of the Star Wars film franchise?"
star_wars[column] = star_wars[column].map(yes_no)
star_wars.head(10)


# In[252]:


# Convert columns "Which of the following Star..." and next 6 into booleans
import numpy as np
movies = {
    "Star Wars: Episode I  The Phantom Menace": True,
    "Star Wars: Episode II  Attack of the Clones": True,
    "Star Wars: Episode III  Revenge of the Sith": True,
    "Star Wars: Episode IV  A New Hope": True,
    "Star Wars: Episode V The Empire Strikes Back": True,
    "Star Wars: Episode VI Return of the Jedi": True,
    np.NaN: False
}

column = star_wars.columns[3:9]

for i in column:
    star_wars[i] = star_wars[i].map(movies)

star_wars = star_wars.rename(columns={
    "Which of the following Star Wars films have you seen? Please select all that apply.": "seen_1",
    "Unnamed: 4": "seen_2",
    "Unnamed: 5": "seen_3",
    "Unnamed: 6": "seen_4",
    "Unnamed: 7": "seen_5",
    "Unnamed: 8": "seen_6"
})
star_wars.head(10)


# In[253]:


star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype(float)

star_wars = star_wars.rename(columns={
    "Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.": "ranking_1",
    "Unnamed: 10": "ranking_2",
    "Unnamed: 11": "ranking_3",
    "Unnamed: 12": "ranking_4",
    "Unnamed: 13": "ranking_5",
    "Unnamed: 14": "ranking_6"
})
star_wars.head(10)


# In[254]:


get_ipython().magic('matplotlib inline')

import matplotlib.pyplot as plt
from numpy import arange
num_cols = [star_wars["ranking_1"].mean(),
star_wars["ranking_2"].mean(),
star_wars["ranking_3"].mean(),
star_wars["ranking_4"].mean(),
star_wars["ranking_5"].mean(),
star_wars["ranking_6"].mean()]
col_labels = ("ranking1" ,
"ranking2" ,
"ranking3" ,
"ranking4" ,
"ranking5" ,
"ranking6" )
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

bar_heights = num_cols
bar_positions = arange(6) 
plt.bar(bar_positions, bar_heights, align='center', alpha=0.5)
tick_positions = range(0,6)
ax.set_xticks(tick_positions)
ax.set_xticklabels(col_labels)
ax.set_xlabel("ranking/movie")
ax.set_ylabel("avg. rating")
ax.set_title("rating per Star Wars movies")

plt.show()


# In[255]:


get_ipython().magic('matplotlib inline')

import matplotlib.pyplot as plt
from numpy import arange
num_cols = [star_wars["seen_1"].sum(),
star_wars["seen_2"].sum(),
star_wars["seen_3"].sum(),
star_wars["seen_4"].sum(),
star_wars["seen_5"].sum(),
star_wars["seen_6"].sum()]
col_labels = ("seen1" ,
"seen2" ,
"seen3" ,
"seen4" ,
"seen5" ,
"seen6" )
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

bar_heights = num_cols
bar_positions = arange(6) 
plt.bar(bar_positions, bar_heights, align='center', alpha=0.5)
tick_positions = range(0,6)
ax.set_xticks(tick_positions)
ax.set_xticklabels(col_labels)
ax.set_xlabel("seen/movie")
ax.set_ylabel("# seen")
ax.set_title("# watches per Star Wars movies")

plt.show()


# In[256]:


males = star_wars[star_wars["Gender"] == "Male"]
females = star_wars[star_wars["Gender"] == "Female"]


# In[259]:


get_ipython().magic('matplotlib inline')

import matplotlib.pyplot as plt
from numpy import arange

num_cols_m = [males["ranking_1"].mean(),
males["ranking_2"].mean(),
males["ranking_3"].mean(),
males["ranking_4"].mean(),
males["ranking_5"].mean(),
males["ranking_6"].mean()]

num_cols_f = [females["ranking_1"].mean(),
females["ranking_2"].mean(),
females["ranking_3"].mean(),
females["ranking_4"].mean(),
females["ranking_5"].mean(),
females["ranking_6"].mean()]

col_labels = ("ranking1" ,
"ranking2" ,
"ranking3" ,
"ranking4" ,
"ranking5" ,
"ranking6" )

fig, ax = plt.subplots()


bar_heights = num_cols_m
bar_positions = arange(6) 
width = 0.35  
ranking1 = ax.bar(bar_positions, bar_heights, width, align='center', color='b', alpha=0.5)

bar_heights = num_cols_f
ranking2 = ax.bar(bar_positions+width, bar_heights, width, align='center', color='y', alpha=0.5)

tick_positions = range(0,6)
ax.set_xticks(tick_positions)
ax.set_xticklabels(col_labels)
ax.set_xlabel("ranking/movie")
ax.set_ylabel("avg. rating")
ax.set_title("rating per Star Wars movies")

ax.legend((ranking1[0], ranking2[0]), ('Males', 'Females'))

plt.show()


# In[261]:


get_ipython().magic('matplotlib inline')

import matplotlib.pyplot as plt
from numpy import arange

num_cols_m = [males["seen_1"].sum(),
males["seen_2"].sum(),
males["seen_3"].sum(),
males["seen_4"].sum(),
males["seen_5"].sum(),
males["seen_6"].sum()]

num_cols_f = [females["seen_1"].sum(),
females["seen_2"].sum(),
females["seen_3"].sum(),
females["seen_4"].sum(),
females["seen_5"].sum(),
females["seen_6"].sum()]

col_labels = ("seen1" ,
"seen2" ,
"seen3" ,
"seen4" ,
"seen5" ,
"seen6" )

fig, ax = plt.subplots()


bar_heights = num_cols_m
bar_positions = arange(6) 
width = 0.35  
seen1 = ax.bar(bar_positions, bar_heights, width, align='center', color='b', alpha=0.5)

bar_heights = num_cols_f
seen2 = ax.bar(bar_positions+width, bar_heights, width, align='center', color='y', alpha=0.5)

tick_positions = range(0,6)
ax.set_xticks(tick_positions)
ax.set_xticklabels(col_labels)
ax.set_xlabel("seen/movie")
ax.set_ylabel("avg. rating")
ax.set_title("rating per Star Wars movies")

ax.legend((seen1[0], seen2[0]), ('Males', 'Females'))

plt.show()

