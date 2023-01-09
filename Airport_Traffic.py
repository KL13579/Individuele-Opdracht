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


# In[2]:


st.set_page_config(page_title = "Airport Traffic",
                  page_icon = ":bar_chart:")


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


#Hier gebruik ik de Country Converter om een kolom aan te maken waar de ISO3 codes van de landen in staan
#cc = coco.CountryConverter()
#df['iso3_codes'] = cc.convert(df['STATE_NAME'], to='ISO3')


# In[8]:


#Kolom met continent toevoegen
#df['Continent'] = cc.convert(df['iso3_codes'], src = 'ISO3', to = 'continent')


# ##### Totaal ATM's per jaar Wereldwijd

# In[9]:


#DEP_per_year = df.groupby('YEAR')['FLT_DEP_1'].sum()
#ARR_per_year = df.groupby('YEAR')['FLT_ARR_1'].sum()
#TOT_per_year = df.groupby('YEAR')['FLT_TOT_1'].sum()


# In[10]:


#df2 = pd.DataFrame(DEP_per_year)


# In[11]:


#df3 = df2.rename(columns={'FLT_DEP_1': 'Departures'})
#df3['Arrivals'] = ARR_per_year
#df3['Total'] = TOT_per_year


# ##### Totaal ATM's per jaar per airport

# In[12]:


#DEP_per_year_per_airport = df.groupby(['YEAR', 'APT_NAME'])['FLT_DEP_1'].sum()
#ARR_per_year_per_airport = df.groupby(['YEAR', 'APT_NAME'])['FLT_ARR_1'].sum()
#TOT_per_year_per_airport = df.groupby(['YEAR', 'APT_NAME'])['FLT_TOT_1'].sum()


# In[13]:


#df4 = pd.DataFrame(DEP_per_year_per_airport)


# In[14]:


#df5 = df4.rename(columns={'FLT_DEP_1': 'Departures'})
#df5['Arrivals'] = ARR_per_year_per_airport
#df5['Total'] = TOT_per_year_per_airport


# In[15]:


#Hier zorg ik ervoor dat de table zo is dat de landnamen de kolommen zijn waardoor ik later een dropdown menu kan maken
#Tot_per_airport = pd.pivot_table(Totaal_per_airport, values = 'Total', index = 'YEAR', columns = 'APT_NAME')


# In[16]:


#Hier maak ik er een csv bestand van
#Tot_per_airport.to_csv('Tot_per_airport.csv')


# ##### Totaal ATM's per jaar per land

# In[17]:


#DEP_per_year_per_state = df.groupby(['YEAR', 'STATE_NAME'])['FLT_DEP_1'].sum()
#ARR_per_year_per_state = df.groupby(['YEAR', 'STATE_NAME'])['FLT_ARR_1'].sum()
#TOT_per_year_per_state = df.groupby(['YEAR', 'STATE_NAME'])['FLT_TOT_1'].sum()


# In[18]:


#df6 = pd.DataFrame(DEP_per_year_per_state)


# In[19]:


#df7 = df6.rename(columns={'FLT_DEP_1': 'Departures'})
#df7['Arrivals'] = ARR_per_year_per_state
#df7['Total'] = TOT_per_year_per_state


# In[20]:


#Hier zorg ik ervoor dat de table zo is dat de landnamen de kolommen zijn waardoor ik later een dropdown menu kan maken
#Tot_per_land = pd.pivot_table(Totaal_per_land, values = 'Total', index = 'YEAR', columns = 'STATE_NAME')


# In[21]:


#Hier maak ik er een csv bestand van
#Tot_per_land.to_csv('Tot_per_land.csv')


# ##### Totaal ATM's per jaar per continent

# In[22]:


#DEP_per_year_per_continent = df.groupby(['YEAR', 'Continent'])['FLT_DEP_1'].sum()
#ARR_per_year_per_continent = df.groupby(['YEAR', 'Continent'])['FLT_ARR_1'].sum()
#TOT_per_year_per_continent = df.groupby(['YEAR', 'Continent'])['FLT_TOT_1'].sum()


# In[23]:


#df8 = pd.DataFrame(DEP_per_year_per_continent)


# In[24]:


#df9 = df8.rename(columns={'FLT_DEP_1': 'Departures'})
#df9['Arrivals'] = ARR_per_year_per_continent
#df9['Total'] = TOT_per_year_per_continent


# In[25]:


#Hier zorg ik ervoor dat de table zo is dat de landnamen de kolommen zijn waardoor ik later een dropdown menu kan maken
#Tot_per_continent = pd.pivot_table(df9, values = 'Total', index = 'YEAR', columns = 'Continent')


# In[26]:


#Hier maak ik er een csv bestand van
#Tot_per_continent.to_csv('Tot_per_continent.csv')


# ##### Dataframes omzetten naar CSV bestanden en inladen

# In[27]:


#Hier zet ik het bovenstaande bestand om naar CSV bestand om het sneller te laten werken in streamlit, dit heb ik ook bij 
#de andere bestanden hierboven gedaan
#df3.to_csv('Total_ATM.csv')

#Hier laad ik het bestand wat ik hierboven tot CSV heb gemaakt weer in
Totaal_ATM = pd.read_csv('Total_ATM.csv')
Totaal_per_airport = pd.read_csv('Tot_per_airport.csv')
Totaal_per_land = pd.read_csv('Tot_per_land.csv')
Totaal_per_continent = pd.read_csv('Tot_per_continent.csv')


# #### Het aanpassen van de data

# In[28]:


#Hier worden de landen vertaald naar het Nederlands
Totaal_per_land = Totaal_per_land.rename(columns = {'Belgium':'België', 'Germany':'Duitsland', 'Estonia':'Estland', 
                                          'Finland':'Finland', 'United Kingdom':'Verenigd Koninkrijk', 
                                          'Netherlands':'Nederland', 'Ireland':'Ierland', 'Denmark':'Denemarken', 
                                          'Luxembourg':'Luxemburg', 'Norway':'Noorwegen', 'Poland':'Polen', 
                                          'Sweden':'Zweden', 'Latvia':'Letland', 'Lithuania':'Litouwen', 'Spain':'Spanje', 
                                          'Albania':'Albanië', 'Bulgaria':'Bulgarije', 'Cyprus':'Cyprus', 
                                          'Croatia':'Kroatië', 'France':'Frankrijk', 'Greece':'Griekenland', 
                                          'Hungary':'Hongarije', 'Italy':'Italië', 'Slovenia':'Slovenië', 
                                          'Czech Republic':'Tsjechië', 'Malta':'Malta', 'Austria':'Oostenrijk',
                                          'Portugal':'Portugal', 'Bosnia and Herzegovina':'Bosnië en Herzegovina', 
                                          'Romania':'Roemenië', 'Switzerland':'Zwitserland', 'Türkiye':'Turkije', 
                                          'Moldova':'Moldavië', 'Republic of North Macedonia':'Noord-Macedonië', 
                                          'Serbia':'Servië', 'Montenegro':'Montenegro', 'Slovakia':'Slowakije', 
                                          'Armenia':'Armenië', 'Georgia':'Georgië', 'Ukraine':'Oekraïne', 
                                          'Morocco':'Marokko', 'Israel':'Israël'})

#Hier worden de continenten vertaald naar het Nederlands
Totaal_per_continent = Totaal_per_continent.rename(columns = {'Africa':'Afrika', 'Asia':'Azië', 'Europe':'Europa'})


# In[29]:


#Hierin worden de mogelijkheden voor de verschillende dropdown menu's gemaakt
land_opties = ['België', 'Duitsland', 'Estland', 'Finland', 
               'Verenigd Koninkrijk', 'Nederland', 'Ierland', 
               'Denemarken', 'Luxemburg', 'Noorwegen', 'Polen', 
               'Zweden', 'Letland', 'Litouwen', 'Spanje', 
               'Albanië', 'Bulgarije', 'Cyprus', 'Kroatië', 'Frankrijk', 
               'Griekenland', 'Hongarije', 'Italië', 'Slovenië', 
               'Tsjechië', 'Malta', 'Oostenrijk', 'Portugal', 
               'Bosnië en Herzegovina', 'Roemenië', 'Zwitserland', 
               'Turkije', 'Moldavië', 'Noord-Macedonië', 'Servië', 
               'Montenegro', 'Slowakije', 'Armenië', 'Georgië', 
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

# In[30]:


#Tabbladen maken
hoofdtab, tab1, tab2, tab3, tab4 = st.tabs(["Hoofdpagina", "Algemeen Overzicht", "Overzicht per Land", 
                                      "Overzicht per Airport", "Voorspelling"])


# In[31]:


#Code voor de Hoofdpagina
with hoofdtab:
    st.header("Aantal ATM's van afgelopen jaren en in de toekomst (Wereldwijd)")
    st.write("In dit dashboard wordt er laten zien wat het aantal Air Traffic Movements (ATM's) wereldwijd is geweest in de afgelopen jaren. Daarnaast wordt er ook gekeken naar de toekomst en wordt er een voorspelling gedaan over het aantal ATM's. Alle data wordt laten zien aan de hand van onder andere een lijngrafiek, een kaart en een voorspellingsmodel.")
    st.markdown("https://ansperformance.eu/reference/dataset/airport-traffic/")


# In[36]:


#Code voor het eerste tabblad
with tab1:
    
    st.header("Het aantal ATM's Wereldwijd")
    st.write("In dit tabblad wordt er laten zien wa het aantal ATM's is wereldwijd over de afgelopen jaren. En waarom er een eventuele daling/stijging in zat.")
    
#Code voor de lineplot
    algemeen = px.line(Totaal_ATM, x = "YEAR", y = Totaal_ATM.columns, title = "Totaal ATM's per Jaar")
    algemeen.update_xaxes(title = "Tijd (Jaren)")
    algemeen.update_yaxes(title = "Aantal ATM's")
    st.plotly_chart(algemeen)


# In[35]:


#Code voor het tweede tabblad
with tab2:
    
    st.header("Het aantal ATM's per Land")
    st.write("In dit tabblad word er laten zien wat het aantal ATM's per land is over de afgelopen jaren. U kunt zelf een land uitkiezen door middel van het dropdown menu.")

#Dropdown menu voor de variabele van de grafiek
    land_variabele = st.selectbox("Kies hier een variabele voor de grafiek: ", land_opties)
    
#Keuze voor per continent of voor een individueel land
    continent = st.checkbox("Klik hier als u het histogram voor een specifiek land wilt zien")
    
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
                      title = "Totaal ATM's per Land per Jaar '" + land_variabele + "'")
        lineplot.update_xaxes(title = "Tijd (Jaren)")
        lineplot.update_yaxes(title = "Aantal ATM's")
        st.plotly_chart(lineplot)


# In[34]:


#Code voor het derde tabblad

