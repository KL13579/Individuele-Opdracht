#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.express as px
import country_converter as coco
import statsmodels.api as sm
from plotly.subplots import make_subplots
import plotly.graph_objects as go


# In[2]:


st.set_page_config(page_title = "Airport Traffic",
                  page_icon = ":bar_chart:")


# ### Inladen van de Data

# In[3]:


#df = pd.read_excel('Airport_Traffic.xlsx', sheet_name = 'DATA')


# In[4]:


#df.shape


# In[5]:


#df.to_csv('Airport_data.csv')


# In[6]:


#df = pd.read_csv('Airport_data.csv')
#df.drop(columns='Unnamed: 0')


# In[7]:


#df_eurocontrol = pd.read_excel("eurocontrol-forecast-2021-2027-traffic-table.xlsx", sheet_name = "IFR Movements")


# In[8]:


#df_eurocontrol = pd.read_excel("eurocontrol-forecast-2022-2028-traffic-table_Oct22.xlsx", sheet_name = "IFR Movements")


# ### Data manipulatie

# In[9]:


#Hier gebruik ik de Country Converter om een kolom aan te maken waar de ISO3 codes van de landen in staan

#cc = coco.CountryConverter()
#df['iso3_codes'] = cc.convert(df['STATE_NAME'], to='ISO3')


# In[10]:


#Kolom met continent toevoegen
    #df['Continent'] = cc.convert(df['iso3_codes'], src = 'ISO3', to = 'continent')


# In[11]:


#df_eurocontrol


# In[12]:


#Hier maak ik het Dataframe in het goede format
#df_eurocontrol.columns = df_eurocontrol.iloc[2]
#df_eurocontrol2 = df_eurocontrol.drop(labels = [0, 1, 2, 3, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 
#                                                151, 152, 153, 154, 155, 156, 157, 158], axis = 0)


# In[13]:


#Kolommen die niet nodig zijn
#df_eurocontrol3 = df_eurocontrol2.drop(columns = ["AAGR \n2022-2028 ", "RP3 AAGR 2020-2024"])


# In[14]:


#Kolom naam veranderen
#df_eurocontrol3 = df_eurocontrol3.rename(columns = {"IFR Movements (Thousands)":"Land"})


# In[15]:


#Hier vul ik alle lege waardes van de kolom "Land" in met het land wat erboven staat
#df_eurocontrol3["Land"] = df_eurocontrol3["Land"].fillna(method = 'ffill')


# In[16]:


#Hier controleer ik of alle landen 3 keer voorkomen
    #df_eurocontrol3["Land"].value_counts()


# In[17]:


#Hier kopieer ik de kolom die aangeeft wat voor scenario het is om dit hierna te kunnen gebruiken bij de voorspellingen
#df_eurocontrol3["Scenario"] = df_eurocontrol3.iloc[:, 1]


# In[18]:


#Hier drop ik de kolom die NaN als naam heeft omdat ik geen andere manier vond om dit makkelijk te doen
#df_eurocontrol4 = df_eurocontrol3.drop(df_eurocontrol3.columns[1], axis = 1)


# In[19]:


#Selecteren van de benodigde kolommen
#df_eurocontrol5 = df_eurocontrol4[["Land", 2023.0, 2024.0, 2025.0, 2026.0, 2027.0, 2028.0, "Scenario"]]


# In[20]:


#Hier maak ik data sets van de verschillende scenarios
    #Voorspelling_hoog = df_eurocontrol5[df_eurocontrol5["Scenario"] == "High"]
    #Voorspelling_basis = df_eurocontrol5[df_eurocontrol5["Scenario"] == "Base"]
    #Voorspelling_laag = df_eurocontrol5[df_eurocontrol5["Scenario"] == "Low"]


# In[21]:


#Hier vermenigvuldig ik alle Jaar kolommen met 1000, alle waardes uit df_eurocontrol zijn namelijk duizendtallen
    #Voorspelling_hoog[[2023.0, 2024.0, 2025.0, 2026.0, 2027.0]] = Voorspelling_hoog[[2023.0, 2024.0, 2025.0, 2026.0, 2027.0]] * 1000
    #Voorspelling_basis[[2023.0, 2024.0, 2025.0, 2026.0, 2027.0]] = Voorspelling_basis[[2023.0, 2024.0, 2025.0, 2026.0, 2027.0]] * 1000
    #Voorspelling_laag[[2023.0, 2024.0, 2025.0, 2026.0, 2027.0]] = Voorspelling_laag[[2023.0, 2024.0, 2025.0, 2026.0, 2027.0]] * 1000


# In[22]:


#Hier vermenigvuldig ik alle Jaar kolommen met 1000, alle waardes uit df_eurocontrol zijn namelijk duizendtallen
#df_eurocontrol5[[2023.0, 2024.0, 2025.0, 2026.0, 2027.0, 2028.0]] = df_eurocontrol5[[2023.0, 2024.0, 2025.0, 2026.0, 2027.0, 2028.0]] * 1000


# In[23]:


#Hier drop ik bij alle bovenstaande dataframes de kolom "Scenario" want die heb ik niet meer nodig
    #Voorspelling_hoog = Voorspelling_hoog.drop(columns = "Scenario")
    #Voorspelling_basis = Voorspelling_basis.drop(columns = "Scenario")
    #Voorspelling_laag = Voorspelling_laag.drop(columns = "Scenario")


# In[24]:


#Land als index zetten bij elk van de bovenstaande dataframes
    #Voorspelling_hoog = Voorspelling_hoog.set_index("Land")
    #Voorspelling_basis = Voorspelling_basis.set_index("Land")
    #Voorspelling_laag = Voorspelling_laag.set_index("Land")


# In[25]:


#Hier wissel ik de index en de kolommen om van plaats
    #Voorspelling_hoog = Voorspelling_hoog.transpose()
    #Voorspelling_basis = Voorspelling_basis.transpose()
    #Voorspelling_laag = Voorspelling_laag.transpose()


# In[26]:


#Kolommen die ik niet nodig heb verwijderen
    #Voorspelling_hoog = Voorspelling_hoog.drop(columns = ["Spain-Canaries*", "Spain-Continental*", "Iceland", "Santa Maria FIR", "Azerbaijan"])
    #Voorspelling_basis = Voorspelling_basis.drop(columns = ["Spain-Canaries*", "Spain-Continental*", "Iceland", "Santa Maria FIR", "Azerbaijan"])
    #Voorspelling_laag = Voorspelling_laag.drop(columns = ["Spain-Canaries*", "Spain-Continental*", "Iceland", "Santa Maria FIR", "Azerbaijan"])


# In[27]:


#CSV maken van de Dataframes
    #Voorspelling_hoog.to_csv("Voorspelling_hoog.csv")
    #Voorspelling_basis.to_csv("Voorspelling_basis.csv")
    #Voorspelling_laag.to_csv("Voorspelling_laag.csv")


# ##### Totaal ATM's per jaar Wereldwijd

# In[28]:


#DEP_per_year = df.groupby('YEAR')['FLT_DEP_1'].sum()
#ARR_per_year = df.groupby('YEAR')['FLT_ARR_1'].sum()
#TOT_per_year = df.groupby('YEAR')['FLT_TOT_1'].sum()


# In[29]:


#df2 = pd.DataFrame(DEP_per_year)


# In[30]:


#df3 = df2.rename(columns={'FLT_DEP_1': 'Departures'})
#df3['Arrivals'] = ARR_per_year
#df3['Total'] = TOT_per_year


# ##### Totaal ATM's per jaar per airport

# In[31]:


#DEP_per_year_per_airport = df.groupby(['YEAR', 'APT_NAME'])['FLT_DEP_1'].sum()
#ARR_per_year_per_airport = df.groupby(['YEAR', 'APT_NAME'])['FLT_ARR_1'].sum()
#TOT_per_year_per_airport = df.groupby(['YEAR', 'APT_NAME'])['FLT_TOT_1'].sum()


# In[32]:


#df4 = pd.DataFrame(DEP_per_year_per_airport)


# In[33]:


#df5 = df4.rename(columns={'FLT_DEP_1': 'Departures'})
#df5['Arrivals'] = ARR_per_year_per_airport
#df5['Total'] = TOT_per_year_per_airport


# In[34]:


#Hier zorg ik ervoor dat de table zo is dat de landnamen de kolommen zijn waardoor ik later een dropdown menu kan maken
#Tot_per_airport = pd.pivot_table(Totaal_per_airport, values = 'Total', index = 'YEAR', columns = 'APT_NAME')


# In[35]:


#Hier maak ik er een csv bestand van
#Tot_per_airport.to_csv('Tot_per_airport.csv')


# ##### Totaal ATM's per jaar per land

# In[36]:


#DEP_per_year_per_state = df.groupby(['YEAR', 'STATE_NAME'])['FLT_DEP_1'].sum()
#ARR_per_year_per_state = df.groupby(['YEAR', 'STATE_NAME'])['FLT_ARR_1'].sum()
#TOT_per_year_per_state = df.groupby(['YEAR', 'STATE_NAME'])['FLT_TOT_1'].sum()


# In[37]:


#df6 = pd.DataFrame(DEP_per_year_per_state)


# In[38]:


#df7 = df6.rename(columns={'FLT_DEP_1': 'Departures'})
#df7['Arrivals'] = ARR_per_year_per_state
#df7['Total'] = TOT_per_year_per_state


# In[39]:


#Hier zorg ik ervoor dat de table zo is dat de landnamen de kolommen zijn waardoor ik later een dropdown menu kan maken
#Tot_per_land = pd.pivot_table(Totaal_per_land, values = 'Total', index = 'YEAR', columns = 'STATE_NAME')


# In[40]:


#Hier maak ik er een csv bestand van
#Tot_per_land.to_csv('Tot_per_land.csv')


# ##### Totaal ATM's per jaar per continent

# In[41]:


#DEP_per_year_per_continent = df.groupby(['YEAR', 'Continent'])['FLT_DEP_1'].sum()
#ARR_per_year_per_continent = df.groupby(['YEAR', 'Continent'])['FLT_ARR_1'].sum()
#TOT_per_year_per_continent = df.groupby(['YEAR', 'Continent'])['FLT_TOT_1'].sum()


# In[42]:


#df8 = pd.DataFrame(DEP_per_year_per_continent)


# In[43]:


#df9 = df8.rename(columns={'FLT_DEP_1': 'Departures'})
#df9['Arrivals'] = ARR_per_year_per_continent
#df9['Total'] = TOT_per_year_per_continent


# In[44]:


#Hier zorg ik ervoor dat de table zo is dat de landnamen de kolommen zijn waardoor ik later een dropdown menu kan maken
#Tot_per_continent = pd.pivot_table(df9, values = 'Total', index = 'YEAR', columns = 'Continent')


# In[45]:


#Hier maak ik er een csv bestand van
#Tot_per_continent.to_csv('Tot_per_continent.csv')


# ##### Dataframes omzetten naar CSV bestanden en inladen

# In[46]:


#Hier zet ik het bovenstaande bestand om naar CSV bestand om het sneller te laten werken in streamlit, dit heb ik ook bij 
#de andere bestanden hierboven gedaan
#df3.to_csv('Total_ATM.csv')

#Hier laad ik het bestand wat ik hierboven tot CSV heb gemaakt weer in
Totaal_ATM = pd.read_csv("Total_ATM.csv")
Totaal_per_airport = pd.read_csv("Tot_per_airport.csv")
Totaal_per_land = pd.read_csv("Tot_per_land.csv")
Totaal_per_continent = pd.read_csv("Tot_per_continent.csv")
Voorspelling_hoog = pd.read_csv("Voorspelling_hoog.csv")
Voorspelling_basis = pd.read_csv("Voorspelling_basis.csv")
Voorspelling_laag = pd.read_csv("Voorspelling_laag.csv")


# ### Het vertalen van de data

# In[47]:


#Hier maak ik nieuwe kolommen aan, zodat ik de landen later met elkaar kan koppelen
Totaal_per_land["Belgium/Luxembourg"] = Totaal_per_land["Belgium"] + Totaal_per_land["Luxembourg"]
Totaal_per_land["Serbia/Montenegro"] = Totaal_per_land["Serbia"] + Totaal_per_land["Montenegro"]


# In[48]:


#Hier drop ik de kolommen waarmee ik hierboven nieuwe kolommen heb aangemaakt
Totaal_per_land = Totaal_per_land.drop(columns = ["Serbia", "Belgium", "Luxembourg", "Montenegro"])


# In[49]:


#Hier verander ik de naam van de kolom met de jaartallen
Voorspelling_hoog = Voorspelling_hoog.rename(columns = {"2":"YEAR"})
Voorspelling_basis = Voorspelling_basis.rename(columns = {"2":"YEAR"})
Voorspelling_laag = Voorspelling_laag.rename(columns = {"2":"YEAR"})


# In[50]:


#Hier worden de landen vertaald naar het Nederlands
Totaal_per_land = Totaal_per_land.rename(columns = {'Germany':'Duitsland', 'Estonia':'Estland', 
                                          'Finland':'Finland', 'United Kingdom':'Verenigd Koninkrijk', 
                                          'Netherlands':'Nederland', 'Ireland':'Ierland', 'Denmark':'Denemarken', 
                                          'Belgium/Luxembourg':'België/Luxemburg', 'Norway':'Noorwegen', 'Poland':'Polen', 
                                          'Sweden':'Zweden', 'Latvia':'Letland', 'Lithuania':'Litouwen', 'Spain':'Spanje', 
                                          'Albania':'Albanië', 'Bulgaria':'Bulgarije', 'Cyprus':'Cyprus', 
                                          'Croatia':'Kroatië', 'France':'Frankrijk', 'Greece':'Griekenland', 
                                          'Hungary':'Hongarije', 'Italy':'Italië', 'Slovenia':'Slovenië', 
                                          'Czech Republic':'Tsjechië', 'Malta':'Malta', 'Austria':'Oostenrijk',
                                          'Portugal':'Portugal', 'Bosnia and Herzegovina':'Bosnië en Herzegovina', 
                                          'Romania':'Roemenië', 'Switzerland':'Zwitserland', 'Türkiye':'Turkije', 
                                          'Moldova':'Moldavië', 'Republic of North Macedonia':'Noord-Macedonië', 
                                          'Serbia/Montenegro':'Servië/Montenegro', 'Slovakia':'Slowakije', 
                                          'Armenia':'Armenië', 'Georgia':'Georgië', 'Ukraine':'Oekraïne', 
                                          'Morocco':'Marokko', 'Israel':'Israël'})

Voorspelling_hoog = Voorspelling_hoog.rename(columns = {'Albania':'Albanië', 'Armenia':'Armenië', 'Austria':'Oostenrijk', 
                                                        'Belgium/Luxembourg':'België/Luxemburg', 'Bulgaria':'Bulgarije',
                                                        'Bosnia and Herzego':'Bosnië en Herzegovina', 'Croatia':'Kroatië', 
                                                        'Cyprus':'Cyprus', 'Czech Republic':'Tsjechië',
                                                        'Denmark':'Denemarken', 'Estonia':'Estland', 'Finland':'Finland', 
                                                        'France':'Frankrijk', 'Georgia':'Georgië', 'Germany':'Duitsland',
                                                        'Greece':'Griekenland', 'Hungary':'Hongarije', 'Ireland':'Ierland', 
                                                        'Israel':'Israël', 'Italy':'Italië', 'Latvia':'Letland',
                                                        'Lisbon FIR':'Portugal', 'Lithuania':'Litouwen', 'Malta':'Malta', 
                                                        'Moldova':'Moldavië', 'Morocco':'Marokko', 'Netherlands':'Nederland', 
                                                        'North Macedonia':'Noord-Macedonië', 'Norway':'Noorwegen', 
                                                        'Poland':'Polen', 'Romania':'Roemenië', 
                                                        'Serbia/Montenegro':'Servië/Montenegro', 'Slovakia':'Slowakije', 
                                                        'Slovenia':'Slovenië', 'Spain*':'Spanje', 'Sweden':'Zweden',
                                                        'Switzerland':'Zwitserland', 'Turkey':'Turkije', 
                                                        'UK':'Verenigd Koninkrijk', 'Ukraine':'Oekraïne'})

Voorspelling_basis = Voorspelling_basis.rename(columns = {'Albania':'Albanië', 'Armenia':'Armenië', 'Austria':'Oostenrijk', 
                                                        'Belgium/Luxembourg':'België/Luxemburg', 'Bulgaria':'Bulgarije',
                                                        'Bosnia and Herzego':'Bosnië en Herzegovina', 'Croatia':'Kroatië', 
                                                        'Cyprus':'Cyprus', 'Czech Republic':'Tsjechië',
                                                        'Denmark':'Denemarken', 'Estonia':'Estland', 'Finland':'Finland', 
                                                        'France':'Frankrijk', 'Georgia':'Georgië', 'Germany':'Duitsland',
                                                        'Greece':'Griekenland', 'Hungary':'Hongarije', 'Ireland':'Ierland', 
                                                        'Israel':'Israël', 'Italy':'Italië', 'Latvia':'Letland',
                                                        'Lisbon FIR':'Portugal', 'Lithuania':'Litouwen', 'Malta':'Malta', 
                                                        'Moldova':'Moldavië', 'Morocco':'Marokko', 'Netherlands':'Nederland', 
                                                        'North Macedonia':'Noord-Macedonië', 'Norway':'Noorwegen', 
                                                        'Poland':'Polen', 'Romania':'Roemenië', 
                                                        'Serbia/Montenegro':'Servië/Montenegro', 'Slovakia':'Slowakije', 
                                                        'Slovenia':'Slovenië', 'Spain*':'Spanje', 'Sweden':'Zweden',
                                                        'Switzerland':'Zwitserland', 'Turkey':'Turkije', 
                                                        'UK':'Verenigd Koninkrijk', 'Ukraine':'Oekraïne'})

Voorspelling_laag = Voorspelling_laag.rename(columns = {'Albania':'Albanië', 'Armenia':'Armenië', 'Austria':'Oostenrijk', 
                                                        'Belgium/Luxembourg':'België/Luxemburg', 'Bulgaria':'Bulgarije',
                                                        'Bosnia and Herzego':'Bosnië en Herzegovina', 'Croatia':'Kroatië', 
                                                        'Cyprus':'Cyprus', 'Czech Republic':'Tsjechië',
                                                        'Denmark':'Denemarken', 'Estonia':'Estland', 'Finland':'Finland', 
                                                        'France':'Frankrijk', 'Georgia':'Georgië', 'Germany':'Duitsland',
                                                        'Greece':'Griekenland', 'Hungary':'Hongarije', 'Ireland':'Ierland', 
                                                        'Israel':'Israël', 'Italy':'Italië', 'Latvia':'Letland',
                                                        'Lisbon FIR':'Portugal', 'Lithuania':'Litouwen', 'Malta':'Malta', 
                                                        'Moldova':'Moldavië', 'Morocco':'Marokko', 'Netherlands':'Nederland', 
                                                        'North Macedonia':'Noord-Macedonië', 'Norway':'Noorwegen', 
                                                        'Poland':'Polen', 'Romania':'Roemenië', 
                                                        'Serbia/Montenegro':'Servië/Montenegro', 'Slovakia':'Slowakije', 
                                                        'Slovenia':'Slovenië', 'Spain*':'Spanje', 'Sweden':'Zweden',
                                                        'Switzerland':'Zwitserland', 'Turkey':'Turkije', 
                                                        'UK':'Verenigd Koninkrijk', 'Ukraine':'Oekraïne'})

#Hier worden de continenten vertaald naar het Nederlands
Totaal_per_continent = Totaal_per_continent.rename(columns = {'Africa':'Afrika', 'Asia':'Azië', 'Europe':'Europa'})


# In[51]:


#Hierin worden de mogelijkheden voor de verschillende dropdown menu's gemaakt
land_opties = ['België/Luxemburg', 'Duitsland', 'Estland', 'Finland', 
               'Verenigd Koninkrijk', 'Nederland', 'Ierland', 
               'Denemarken', 'Noorwegen', 'Polen', 
               'Zweden', 'Letland', 'Litouwen', 'Spanje', 
               'Albanië', 'Bulgarije', 'Cyprus', 'Kroatië', 'Frankrijk', 
               'Griekenland', 'Hongarije', 'Italië', 'Slovenië', 
               'Tsjechië', 'Malta', 'Oostenrijk', 'Portugal', 
               'Bosnië en Herzegovina', 'Roemenië', 'Zwitserland', 
               'Turkije', 'Moldavië', 'Noord-Macedonië', 
               'Servië/Montenegro', 'Slowakije', 'Armenië', 'Georgië', 
               'Oekraïne', 'Marokko', 'Israël']

airport_opties = ['Abad', 'Aberdeen', 'Agen-La Garenne', 'Ajaccio-Napoléon-Bonaparte', 'Aktion', 'Al Massira', 'Albacete', 
                  'Albert-Bray', 'Alesund', 'Alicante', 'Almeria', 'Alta', 'Amsterdam - Schiphol', 'Andenes', 
                  'Angers-Marcé', 'Ankara - Esenboğa', 'Annecy-Meythet', 'Annemasse', 'Antalya', 'Antwerp', 'Asturias', 
                  'Athens', 'Avignon-Caumont', 'Badajoz', 'Barcelona', 'Bardufoss', 'Bastia-Poretta', 'Batsfjord',
                  'Beauvais-Tillé', 'Belfast - Aldergrove', 'Belfast - City Airport', 'Belgrade - Nikola Tesla', 
                  'Ben Gurion International', 'Bergamo', 'Bergen', 'Bergerac-Roumanière', 'Berlevåg', 
                  'Berlin - Brandenburg', 'Berlin - Tegel', 'Biarritz-Bayonne-Anglet', 'Biggin Hill', 'Bilbao', 
                  'Birmingham', 'Bodø', 'Bologna', 'Bordeaux-Mérignac', 'Bratislava', 'Bremen', 'Brest-Bretagne', 
                  'Brindisi', 'Bristol', 'Brive-Souillac', 'Brno-Tuřany', 'Bronnoysund Bronnoy', 'Brussels', 
                  'Bucharest - Băneasa', 'Bucharest - Otopeni', 'Budapest - Ferihegy', 'Burgos', 'Bydgoszcz', 
                  'Bâle-Mulhouse', 'Béziers-Vias', 'Caen-Carpiquet', 'Calvi-Sainte-Catherine', 'Cannes-Mandelieu', 
                  'Carcassonne-Salvaza', 'Cascais', 'Catania', 'Chambéry-Aix-les-Bains', 'Charleroi', 'Chișinău',
                  'Châlons-Vatry', 'Châteauroux-Déols', 'Ciudad Real Central', 'Clermont-Ferrand-Auvergne', 
                  'Cologne-Bonn', 'Connaught', 'Copenhagen - Kastrup', 'Cordoba', 'Corfu', 'Cork', 'Deauville-Normandie', 
                  'Dinard-Pleurtuit-Saint-Malo', 'Donegal', 'Dresden', 'Dublin', 'Dusseldorf', 'Dôle-Tavaux', 
                  'East Midlands', 'Edinburgh', 'Erfurt', 'Farnborough', 'Faro', 'Figari-Sud Corse', 'Flores', 'Florø', 
                  'Forde Bringeland', 'Frankfurt', 'Fuerteventura', 'Gdansk', 'Geneva', 'Gerona', 'Glasgow', 
                  'Gran Canaria', 'Granada', 'Graz', 'Grenoble-Isère', 'Groningen', 'Göteborg', 'Hamburg', 'Hammerfest', 
                  'Hanover', 'Harstad - Narvik Evenes', 'Haugesund', 'Helsinki - Vantaa', 'Heraklion', 'Hierro', 
                  'Honningsvåg Valan', 'Horta', 'Hyères-Le Palyvestre', 'Ibiza', 'Ibn Batouta', 'Innsbruck', 
                  'Istanbul Atatürk', 'Istanbul Sabiha Gökçen', 'Istres-Le Tubé', 'Izmir - Adnan Menderes', 
                  'Jerez De La Frontera', 'Karlovy Vary', 'Katowice - Pyrzowice', 'Kaunas', 'Kefallinia', 
                  'Kerry - Farranfore', 'Khania - Souda', 'Kiev - Boryspil', 'Kirkenes Høybuktmoen', 'Klagenfurt', 'Kos',
                  'Krakow - Balice', 'Kristiansand Kjevik', 'Kristiansund Kvernberget', 'La Coruna', 'La Gomera', 
                  'La Palma', 'La Rochelle-Ile de Ré', 'Lakselv Banak', 'Lannion', 'Lanzarote', 'Larnaca', 
                  'Le Havre-Octeville', 'Le Mans', 'Leipzig-Halle', 'Leknes', 'Lelystad', 'Leon', 'Liepaja', 
                  'Lille-Lesquin', 'Limoges-Bellegarde', 'Linz', 'Lisbon', 'Liège', 'Ljubljana', 'Lleida - Alguaire', 
                  'Lodz - Lublinek', 'Logrono', 'London - City', 'London - Gatwick', 'London - Heathrow', 
                  'London - Luton', 'London - Stansted', 'Londonderry - Eglinton', 'Lorient-Lann Bihoué', 'Lublin', 
                  'Luxembourg', 'Lučko', 'Lyon-Bron', 'Lyon-Saint-Exupéry', 'Maastricht-Aachen', 'Madeira', 
                  'Madrid - Barajas', 'Madrid - Cuatro Viento', 'Madrid - Getafe', 'Madrid - Torrejon', 'Mahon', 'Malta', 
                  'Manchester', 'Maribor', 'Marseille-Provence', 'Mehamn', 'Melilla', 'Menara', 'Metz-Nancy-Lorraine', 
                  'Mikonos', 'Milan - Linate', 'Milan - Malpensa', 'Mo i Rana Røssvoll', 'Mohammed V International', 
                  'Molde Årø', 'Montijo', 'Montpellier-Méditerranée', 'Mosjøen Kjærstad', 'Muenster-Osnabrueck', 'Munich', 
                  'Murcia San Javier', 'Málaga', 'Namsos Høknesøra', 'Nantes-Atlantique', 'Naples', 'Newcastle', 
                  'Nice-Côte d’Azur', 'Noain Pamplona', 'Nuremberg', 'Nîmes-Garons', 'Olsztyn-Mazury', 
                  'Orsta¿Volda Hovden', 'Oslo - Gardermoen', 'Ostend-Bruges', 'Ostrava', 'Palanga', 
                  'Palermo Falcone-Borsellino', 'Palma - Son San Juan', 'Palma de Mallorca', 'Paphos', 
                  'Paris-Charles-de-Gaulle', 'Paris-Le Bourget', 'Paris-Orly', 'Pau-Pyrénées', 'Perpignan-Rivesaltes', 
                  'Pisa San Giusto', 'Podgorica', 'Poitiers-Biard', 'Ponta Delgada', 'Porto', 'Porto Santo', 'Portorož',
                  'Poznan - Lawica', 'Prague', 'Quimper-Pluguffan', 'Rabat-Salé', 'Radom',
                  'Región de Murcia International Airport', 'Rennes-Saint-Jacques', 'Reus', 'Riga', 'Rodez-Marcillac', 
                  'Rodos', 'Rome - Ciampino', 'Rome - Fiumicino', 'Roros', 'Rorvik Ryum', 'Rost', 'Rota', 'Rotterdam', 
                  'Rouen', 'Rzeszow - Jasionka', 'Saarbruecken', 'Sabadell', 'Saint-Etienne-Bouthéon', 
                  'Saint-Nazaire-Montoir', 'Salamanca Matalan', 'Salzburg', 'San Sebastian', 'Sandane  Anda', 
                  'Sandnessjøen Stokka', 'Santa Maria', 'Santander', 'Santiago', 'Santorini', 'Sarajevo', 'Saïss', 
                  'Sevilla', 'Seville - Moron', 'Shannon', 'Siauliai', 'Sion', 'Skiathos', 'Skopje', 'Sligo', 'Sofia', 
                  'Sogndal Haukåsen', 'Son Bonet', 'Sorkjosen', 'Southampton', 'Stavanger', 'Stockholm - Arlanda',
                  'Stockholm - Bromma', 'Stokmarknes Skagen', 'Strasbourg-Entzheim', 'Stuttgart', 'Svalbard Longyear', 
                  'Svolvær Helle', 'Szczecin - Goleniów', 'Tallinn', 'Tarbes-Lourdes Pyrénées', 'Tartu', 'Tbilisi', 
                  'Tel Aviv - Ben Gurion International', 'Tenerife North', 'Tenerife Sur - Reina Sofia', 'Thessaloniki', 
                  'Tirana', 'Torino Caselle', 'Toulouse-Blagnac', 'Tours-Val de Loire', 'Toussus-le-Noble', 'Treviso', 
                  'Tromsø', 'Trondheim', 'Tukums Jurmala', 'Vadsø', 'Valencia', 'Valencia - Requena', 'Valladolid', 
                  'Vardø Svartnes', 'Venice', 'Ventspils', 'Vienna', 'Vigo', 'Vilnius', 'Vitoria', 'Værøy', 
                  'Warszawa - Chopina', 'Warszawa - Modlin', 'Waterford', 'Weston', 'Wroclaw - Strachowice', 'Yerevan', 
                  'Zagreb', 'Zakinthos', 'Zaragoza', 'Zielona Gora - Babimost', 'Zürich', 'iGA Istanbul Airport']


# #### Code voor het dashboard

# In[52]:


#Tabbladen maken
hoofdtab, tab1, tab2, tab3, tab4 = st.tabs(["Hoofdpagina", "Algemeen Overzicht", "Overzicht per Land", 
                                      "Overzicht per Airport", "Voorspelling"])


# In[53]:


#Code voor de Hoofdpagina
with hoofdtab:
    st.header("Aantal ATM's van afgelopen jaren en in de toekomst (Wereldwijd)")
    st.write("In dit dashboard wordt er laten zien wat het aantal Air Traffic Movements (ATM's) wereldwijd is geweest in de afgelopen jaren. Daarnaast wordt er ook gekeken naar de toekomst en wordt er een voorspelling gedaan over het aantal ATM's. Alle data wordt laten zien aan de hand van onder andere een lijngrafiek, een kaart en een voorspellingsmodel.")
    st.markdown("Bronnen:")
    st.markdown("https://ansperformance.eu/reference/dataset/airport-traffic/")
    st.markdown("https://www.eurocontrol.int/publication/eurocontrol-forecast-update-2021-2027")


# In[54]:


#Code voor het eerste tabblad
with tab1:
    
    st.header("Het aantal ATM's Wereldwijd")
    st.write("In dit tabblad wordt er laten zien wa het aantal ATM's is wereldwijd over de afgelopen jaren. En waarom er een eventuele daling/stijging in zat.")
    
#Code voor de lineplot
    algemeen = px.line(Totaal_ATM, x = "YEAR", y = Totaal_ATM.columns, title = "Totaal ATM's per Jaar")
    algemeen.update_xaxes(title = "Tijd (Jaren)")
    algemeen.update_yaxes(title = "Aantal ATM's")
    st.plotly_chart(algemeen)


# In[55]:


#Code voor het tweede tabblad
with tab2:
    
    st.header("Het aantal ATM's per Land")
    st.write("In dit tabblad wordt er laten zien wat het aantal ATM's per land is over de afgelopen jaren. U kunt zelf een land uitkiezen door middel van het dropdown menu.")

#Dropdown menu voor de variabele van de grafiek
    land_variabele = st.selectbox("Kies hier een variabele voor de grafiek: ", land_opties)
    
#Keuze voor per continent of voor een individueel land
    continent = st.checkbox("Klik hier als u het verloop in het aantal ATM's voor een specifiek land wilt zien")
    
#Grafiek voor de continenten
    if continent is False:
        lineplot = px.line(Totaal_per_continent, x = "YEAR", y = Totaal_per_continent.columns, 
                   title = "Totaal ATM's per Continent per Jaar")
        lineplot.update_xaxes(title = "Tijd (Jaren)")
        lineplot.update_yaxes(title = "Aantal ATM's")
        st.plotly_chart(lineplot)

#Code voor de lineplots
    else:
        lineplot = px.line(Totaal_per_land, x = "YEAR", y = land_variabele, 
                      title = "Totaal ATM's per Jaar in '" + land_variabele + "'")
        lineplot.update_xaxes(title = "Tijd (Jaren)")
        lineplot.update_yaxes(title = "Aantal ATM's")
        st.plotly_chart(lineplot)


# In[56]:


#Code voor het derde tabblad
with tab3:
    st.header("Het aantal ATM's per Airport")
    st.write("In dit tabblad wordt er laten zien wat het aantal ATM's per airport is over de afgelopen jaren. U kunt zelf een airport uitkiezen door middel van het dropdown menu.")
    
#Dropdown menu voor de variabele van de grafiek
    airport_variabele = st.selectbox("Kies hier een variabele voor de grafiek: ", airport_opties)
    
#Code voor de lineplots per airport
    lineplot = px.line(Totaal_per_airport, x = "YEAR", y = airport_variabele, 
                      title = "Totaal ATM's per Jaar op '" + airport_variabele + "'")
    lineplot.update_xaxes(title = "Tijd (Jaren)")
    lineplot.update_yaxes(title = "Aantal ATM's")
    st.plotly_chart(lineplot)


# In[57]:


#Code voor het vierde tabblad
with tab4:
    
    st.header("Voorspelling van het aantal ATM's")
    st.write("In dit tabblad wordt er laten zien wat het verwachte aantal ATM's gaat zijn in de komende jaren.")
    
#Dropdown menu voor de verschillende landen
    land_variabele = st.selectbox("Kies hier een land waarvoor u de data wilt bekijken: ", land_opties)

#Code voor de plots over de voorspelling per land
    dfs = {"Beste Scenario" : Voorspelling_hoog, "Gemiddeld Scenario" : Voorspelling_basis, 
           "Slechtste Scenario" : Voorspelling_laag}

    fig = go.Figure()

    for i in dfs:
        fig = fig.add_trace(go.Line(x = dfs[i]["YEAR"], y = dfs[i][land_variabele], name = i))
        fig.update_layout(title = "Voorspelling Scenario's in '" + land_variabele + "'")
    
    st.plotly_chart(fig)

