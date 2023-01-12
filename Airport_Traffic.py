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


# In[50]:


#df_eurocontrol = pd.read_excel("eurocontrol-forecast-2021-2027-traffic-table.xlsx", sheet_name = "IFR Movements")


# ### Data manipulatie

# In[7]:


#Hier gebruik ik de Country Converter om een kolom aan te maken waar de ISO3 codes van de landen in staan

#cc = coco.CountryConverter()
#df['iso3_codes'] = cc.convert(df['STATE_NAME'], to='ISO3')


# In[8]:


#Kolom met continent toevoegen
    #df['Continent'] = cc.convert(df['iso3_codes'], src = 'ISO3', to = 'continent')


# In[53]:


#Hier maak ik het Dataframe in het goede format
    #df_eurocontrol.columns = df_eurocontrol.iloc[2]
    #df_eurocontrol2 = df_eurocontrol.drop(labels = [0, 1, 2, 3, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 
    #                                                151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161], axis = 0)


# In[54]:


#Kolommen die niet nodig zijn
#df_eurocontrol3 = df_eurocontrol2.drop(columns = ["AAGR 2020-2027 (vs 2019)", "RP2 AAGR 2015-2019 \n(vs 2014)", "RP3 AAGR 2020-2024 \n(vs 2019)"])


# In[55]:


#Kolom naam veranderen
    #df10 = df_eurocontrol3.rename(columns = {"IFR Movements (Thousands)":"Land"})


# In[56]:


#Dataframe filteren op de landen en omzetten naar CSV zodat het lokaal makkelijker runt
    #df11 = df10[~df10["Land"].isna()]
    #df12 = df11[["Land", 2023.0, 2024.0, 2025.0, 2026.0, 2027.0]]
    #df12.to_csv("Voorspelling ATM's")


# In[15]:


#CSV bestand opnieuw inladen
    #Voorspelling = pd.read_csv("Voorspelling ATM's")
    #Voorspelling = Voorspelling.drop(columns = "Unnamed: 0")


# In[16]:


#Datatype van de kolommen omzetten naar integer
    #for col in ['2023.0', '2024.0', '2025.0', '2026.0', '2027.0']:
    #    Voorspelling[col] = Voorspelling[col].astype("int64")


# In[17]:


#De kolom 'Land' als index inzetten en de index en kolommen omdraaien
    #Voorspelling = Voorspelling.set_index("Land")
    #Voorspelling_goed = Voorspelling.transpose()


# In[58]:


#Kolommen die ik niet nodig heb verwijderen
    #Voorspelling_goed = Voorspelling_goed.drop(columns = ["Spain-Canaries*", "Spain-Continental*"])


# In[20]:


#Dataset filteren op de landen die ik kan gebruiken
    #Voorspelling_ATM = Voorspelling_goed[['Albania', 'Armenia', 'Austria', 'Belgium/Luxembourg',
    #                                      'Bosnia and Herzego', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic',
    #                                      'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany',
    #                                      'Greece', 'Hungary', 'Ireland', 'Israel', 'Italy', 'Latvia',
    #                                      'Lisbon FIR', 'Lithuania', 'Malta', 'Moldova', 'Morocco', 'Netherlands',
    #                                      'North Macedonia', 'Norway', 'Poland', 'Romania',
    #                                      'Serbia/Montenegro', 'Slovakia', 'Slovenia', 'Spain*', 'Sweden',
    #                                      'Switzerland', 'Turkey', 'UK', 'Ukraine']]


# In[49]:


#CSV maken van het Dataframe
    #Voorspelling_ATM.to_csv("Voorspelling_aantal_ATM's.csv")


# ##### Totaal ATM's per jaar Wereldwijd

# In[21]:


#DEP_per_year = df.groupby('YEAR')['FLT_DEP_1'].sum()
#ARR_per_year = df.groupby('YEAR')['FLT_ARR_1'].sum()
#TOT_per_year = df.groupby('YEAR')['FLT_TOT_1'].sum()


# In[22]:


#df2 = pd.DataFrame(DEP_per_year)


# In[23]:


#df3 = df2.rename(columns={'FLT_DEP_1': 'Departures'})
#df3['Arrivals'] = ARR_per_year
#df3['Total'] = TOT_per_year


# ##### Totaal ATM's per jaar per airport

# In[24]:


#DEP_per_year_per_airport = df.groupby(['YEAR', 'APT_NAME'])['FLT_DEP_1'].sum()
#ARR_per_year_per_airport = df.groupby(['YEAR', 'APT_NAME'])['FLT_ARR_1'].sum()
#TOT_per_year_per_airport = df.groupby(['YEAR', 'APT_NAME'])['FLT_TOT_1'].sum()


# In[25]:


#df4 = pd.DataFrame(DEP_per_year_per_airport)


# In[26]:


#df5 = df4.rename(columns={'FLT_DEP_1': 'Departures'})
#df5['Arrivals'] = ARR_per_year_per_airport
#df5['Total'] = TOT_per_year_per_airport


# In[27]:


#Hier zorg ik ervoor dat de table zo is dat de landnamen de kolommen zijn waardoor ik later een dropdown menu kan maken
#Tot_per_airport = pd.pivot_table(Totaal_per_airport, values = 'Total', index = 'YEAR', columns = 'APT_NAME')


# In[28]:


#Hier maak ik er een csv bestand van
#Tot_per_airport.to_csv('Tot_per_airport.csv')


# ##### Totaal ATM's per jaar per land

# In[29]:


#DEP_per_year_per_state = df.groupby(['YEAR', 'STATE_NAME'])['FLT_DEP_1'].sum()
#ARR_per_year_per_state = df.groupby(['YEAR', 'STATE_NAME'])['FLT_ARR_1'].sum()
#TOT_per_year_per_state = df.groupby(['YEAR', 'STATE_NAME'])['FLT_TOT_1'].sum()


# In[30]:


#df6 = pd.DataFrame(DEP_per_year_per_state)


# In[31]:


#df7 = df6.rename(columns={'FLT_DEP_1': 'Departures'})
#df7['Arrivals'] = ARR_per_year_per_state
#df7['Total'] = TOT_per_year_per_state


# In[32]:


#Hier zorg ik ervoor dat de table zo is dat de landnamen de kolommen zijn waardoor ik later een dropdown menu kan maken
#Tot_per_land = pd.pivot_table(Totaal_per_land, values = 'Total', index = 'YEAR', columns = 'STATE_NAME')


# In[33]:


#Hier maak ik er een csv bestand van
#Tot_per_land.to_csv('Tot_per_land.csv')


# ##### Totaal ATM's per jaar per continent

# In[34]:


#DEP_per_year_per_continent = df.groupby(['YEAR', 'Continent'])['FLT_DEP_1'].sum()
#ARR_per_year_per_continent = df.groupby(['YEAR', 'Continent'])['FLT_ARR_1'].sum()
#TOT_per_year_per_continent = df.groupby(['YEAR', 'Continent'])['FLT_TOT_1'].sum()


# In[35]:


#df8 = pd.DataFrame(DEP_per_year_per_continent)


# In[36]:


#df9 = df8.rename(columns={'FLT_DEP_1': 'Departures'})
#df9['Arrivals'] = ARR_per_year_per_continent
#df9['Total'] = TOT_per_year_per_continent


# In[37]:


#Hier zorg ik ervoor dat de table zo is dat de landnamen de kolommen zijn waardoor ik later een dropdown menu kan maken
#Tot_per_continent = pd.pivot_table(df9, values = 'Total', index = 'YEAR', columns = 'Continent')


# In[38]:


#Hier maak ik er een csv bestand van
#Tot_per_continent.to_csv('Tot_per_continent.csv')


# ##### Dataframes omzetten naar CSV bestanden en inladen

# In[59]:


#Hier zet ik het bovenstaande bestand om naar CSV bestand om het sneller te laten werken in streamlit, dit heb ik ook bij 
#de andere bestanden hierboven gedaan
#df3.to_csv('Total_ATM.csv')

#Hier laad ik het bestand wat ik hierboven tot CSV heb gemaakt weer in
Totaal_ATM = pd.read_csv("Total_ATM.csv")
Totaal_per_airport = pd.read_csv("Tot_per_airport.csv")
Totaal_per_land = pd.read_csv("Tot_per_land.csv")
Totaal_per_continent = pd.read_csv("Tot_per_continent.csv")
Voorspelling_ATM = pd.read_csv("Voorspelling_aantal_ATM's.csv")


# #### Het aanpassen van de data

# In[61]:


#Hier maak ik nieuwe kolommen aan, zodat ik de landen later met elkaar kan koppelen
Totaal_per_land["Belgium/Luxembourg"] = Totaal_per_land["Belgium"] + Totaal_per_land["Luxembourg"]
Totaal_per_land["Serbia/Montenegro"] = Totaal_per_land["Serbia"] + Totaal_per_land["Montenegro"]


# In[63]:


Totaal_per_land.drop(columns = ["Serbia", "Belgium", "Luxembourg", "Montenegro"])


# In[74]:


Voorspelling_ATM = Voorspelling_ATM.rename(columns = {'Unnamed: 0':"Jaar"})


# In[64]:


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

Voorspelling_ATM = Voorspelling_ATM.rename(columns = {'Albania':'Albanië', 'Armenia':'Armenië', 'Austria':'Oostenrijk', 
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


# In[65]:


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

# In[42]:


#Tabbladen maken
hoofdtab, tab1, tab2, tab3, tab4 = st.tabs(["Hoofdpagina", "Algemeen Overzicht", "Overzicht per Land", 
                                      "Overzicht per Airport", "Voorspelling"])


# In[67]:


#Code voor de Hoofdpagina
with hoofdtab:
    st.header("Aantal ATM's van afgelopen jaren en in de toekomst (Wereldwijd)")
    st.write("In dit dashboard wordt er laten zien wat het aantal Air Traffic Movements (ATM's) wereldwijd is geweest in de afgelopen jaren. Daarnaast wordt er ook gekeken naar de toekomst en wordt er een voorspelling gedaan over het aantal ATM's. Alle data wordt laten zien aan de hand van onder andere een lijngrafiek, een kaart en een voorspellingsmodel.")
    st.markdown("https://ansperformance.eu/reference/dataset/airport-traffic/")
    st.markdown("https://www.eurocontrol.int/publication/eurocontrol-forecast-update-2021-2027")


# In[44]:


#Code voor het eerste tabblad
with tab1:
    
    st.header("Het aantal ATM's Wereldwijd")
    st.write("In dit tabblad wordt er laten zien wa het aantal ATM's is wereldwijd over de afgelopen jaren. En waarom er een eventuele daling/stijging in zat.")
    
#Code voor de lineplot
    algemeen = px.line(Totaal_ATM, x = "YEAR", y = Totaal_ATM.columns, title = "Totaal ATM's per Jaar")
    algemeen.update_xaxes(title = "Tijd (Jaren)")
    algemeen.update_yaxes(title = "Aantal ATM's")
    st.plotly_chart(algemeen)


# In[45]:


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


# In[68]:


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


# In[75]:


#Code voor het vierde tabblad
with tab4:
    
    st.header("Voorspelling van het aantal ATM's")
    st.write("In dit tabblad wordt er laten zien wat het verwachte aantal ATM's gaat zijn in de komende jaren")
    
#Dropdown menu voor de verschillende landen
    land_variabele = st.selectbox("Kies hier een land waarvoor u de data wilt bekijken: ", land_opties)
    
#Code voor de plots over de voorspelling per land
    fig = px.line(Voorspelling_ATM, x = "Jaar", y = land_variabele, 
                      title = "Totaal ATM's per Jaar op '" + land_variabele + "'")
    fig.update_xaxes(title = "Tijd (Jaren)")
    fig.update_yaxes(title = "Aantal ATM's")
    st.plotly_chart(fig)


# In[ ]:




