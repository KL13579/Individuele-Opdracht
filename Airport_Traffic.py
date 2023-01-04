#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.express as px
import country_converter as coco
import statsmodels.api as sm


# In[18]:


st.set_page_config(page_title = "Airport Traffic",
                  page_icon = ":bar_chart:")


# In[2]:


#df = pd.read_excel('Airport_Traffic.xlsx', sheet_name = 'DATA')


# In[5]:


#df.shape


# In[6]:


#df.to_csv('Airport_data.csv')


# In[7]:


#df = pd.read_csv('Airport_data.csv')
#df.drop(columns='Unnamed: 0')


# In[8]:


#df['STATE_NAME'].unique()


# ##### Totaal ATM's per jaar Wereldwijd

# In[22]:


#DEP_per_year = df.groupby('YEAR')['FLT_DEP_1'].sum()
#ARR_per_year = df.groupby('YEAR')['FLT_ARR_1'].sum()
#TOT_per_year = df.groupby('YEAR')['FLT_TOT_1'].sum()


# In[23]:


#df2 = pd.DataFrame(DEP_per_year)


# In[49]:


#df3 = df2.rename(columns={'FLT_DEP_1': 'Departures'})
#df3['Arrivals'] = ARR_per_year
#df3['Total'] = TOT_per_year


# ##### Totaal ATM's per jaar per airport

# In[46]:


#DEP_per_year_per_airport = df.groupby(['YEAR', 'APT_NAME'])['FLT_DEP_1'].sum()
#ARR_per_year_per_airport = df.groupby(['YEAR', 'APT_NAME'])['FLT_ARR_1'].sum()
#TOT_per_year_per_airport = df.groupby(['YEAR', 'APT_NAME'])['FLT_TOT_1'].sum()


# In[47]:


#df4 = pd.DataFrame(DEP_per_year_per_airport)


# In[48]:


#df5 = df4.rename(columns={'FLT_DEP_1': 'Departures'})
#df5['Arrivals'] = ARR_per_year_per_airport
#df5['Total'] = TOT_per_year_per_airport


# ##### Totaal ATM's per jaar per land

# In[53]:


#DEP_per_year_per_state = df.groupby(['YEAR', 'STATE_NAME'])['FLT_DEP_1'].sum()
#ARR_per_year_per_state = df.groupby(['YEAR', 'STATE_NAME'])['FLT_ARR_1'].sum()
#TOT_per_year_per_state = df.groupby(['YEAR', 'STATE_NAME'])['FLT_TOT_1'].sum()


# In[54]:


#df6 = pd.DataFrame(DEP_per_year_per_state)


# In[ ]:


#df7 = df6.rename(columns={'FLT_DEP_1': 'Departures'})
#df7['Arrivals'] = ARR_per_year_per_state
#df7['Total'] = TOT_per_year_per_state


# ##### Dataframes omzetten naar CSV bestanden en inladen

# In[57]:


#Hier zet ik het bovenstaande bestand om naar CSV bestand om het sneller te laten werken in streamlit
#df3.to_csv('Total_ATM.csv')
#df5.to_csv('ATM_per_airport.csv')
#df7.to_csv('ATM_per_land.csv')

#Hier laad ik het bestand wat ik hierboven tot CSV heb gemaakt weer in
Totaal_ATM = pd.read_csv('Total_ATM.csv')
Totaal_per_airport = pd.read_csv('ATM_per_airport.csv')
Totaal_per_land = pd.read_csv('ATM_per_land.csv')


# In[62]:


#Hierin worden de mogelijkheden voor de verschillende dropdown menu's gemaakt
land_opties = ['Belgium', 'Germany', 'Estonia', 'Finland', 'United Kingdom', 
          'Netherlands', 'Ireland', 'Denmark', 'Luxembourg', 'Norway',
          'Poland', 'Sweden', 'Latvia', 'Lithuania', 'Spain', 'Albania',
          'Bulgaria', 'Cyprus', 'Croatia', 'France', 'Greece', 'Hungary',
          'Italy', 'Slovenia', 'Czech Republic', 'Malta', 'Austria',
          'Portugal', 'Bosnia and Herzegovina', 'Romania', 'Switzerland',
          'Türkiye', 'Moldova', 'Republic of North Macedonia', 'Serbia',
          'Montenegro', 'Slovakia', 'Armenia', 'Georgia', 'Ukraine',
          'Morocco', 'Israel']


# In[56]:


sns.set_style('whitegrid')
p = sns.lineplot(data=Totaal_ATM, x='YEAR', y='Total')
plt.title("Totaal ATM's per Jaar (Wereldwijd)")
plt.show()


# In[58]:


fig = px.line(Totaal_ATM, x = 'YEAR', y = 'Total', title = "Totaal ATM's per Jaar (Wereldwijd)")
fig.show()


# In[75]:


Tot_per_land = pd.pivot_table(Totaal_per_land, values = 'Total', index = 'YEAR', columns = 'STATE_NAME')
Tot_per_land


# In[80]:


fig = px.line(Tot_per_land, x = Tot_per_land.index, y = land_opties, title = "Totaal ATM's per Land per Jaar")
st.plotly_chart(fig)


# In[ ]:




