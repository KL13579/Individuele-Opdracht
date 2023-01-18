#!/usr/bin/env python
# coding: utf-8

# # Bestand voor Streamlit

# ## Importeren packages

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.express as px
import country_converter as coco
import plotly.graph_objects as go


# ## Data inladen en kleine toevoegingen

# In[26]:


#Hieronder laad ik de benodigde datasets in
Totaal_ATM = pd.read_csv("Total_ATM.csv")
Totaal_per_airport = pd.read_csv("Tot_per_airport.csv")
Totaal_per_land = pd.read_csv("Totaal_per_land.csv")
Totaal_per_continent = pd.read_csv("Totaal_per_continent.csv")
Voorspelling_best = pd.read_csv("Voorspelling_hoog.csv")
Voorspelling_average = pd.read_csv("Voorspelling_basis.csv")
Voorspelling_worst = pd.read_csv("Voorspelling_laag.csv")


# In[30]:


#Hier verander ik de naam van de kolom met de jaartallen
Voorspelling_best = Voorspelling_best.rename(columns = {"2":"YEAR"})
Voorspelling_average = Voorspelling_average.rename(columns = {"2":"YEAR"})
Voorspelling_worst = Voorspelling_worst.rename(columns = {"2":"YEAR"})


# In[34]:


#Kolom Unnamed verwijderen van het dataframe "Totaal_per_continent"
Totaal_per_continent = Totaal_per_continent.drop(columns = "Unnamed: 0")


# In[18]:


#Hieronder maak ik de mogelijkheden voor de dropdown menu's
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


# ## Code voor het dashboard

# In[19]:


st.set_page_config(page_title = "Airport Traffic",
                  page_icon = ":bar_chart:")


# In[20]:


#Tabbladen maken
hoofdtab, tab1, tab2, tab3, tab4 = st.tabs(["Hoofdpagina", "Algemeen Overzicht", "Overzicht per Airport", 
                                      "Overzicht per Land", "Voorspelling aantal Bewegingen"])


# In[37]:


#Code voor de Hoofdpagina
with hoofdtab:
    st.header("Aantal ATM's van afgelopen jaren en in de toekomst (Focus Europa)")
    st.write("In dit dashboard wordt er laten zien wat het aantal Air Traffic Movements (ATM's) wereldwijd is geweest in de afgelopen jaren. Deze data is van ANSperformance (Eurocontrol). Daarnaast wordt er ook gekeken naar de toekomst en wordt er een voorspelling gedaan over het aantal ATM's. De voorspelling over het aantal ATM's wordt besproken aan de hand van de voorspelling van het aantal vliegbewegingen. De bron voor deze data is Eurocontrol, zij hebben een voorspelling gedaan t/m 2028. In dit dashboard ligt de focus op de landen in Europa. Het dashboard is op de volgende manier opgebouwd: Tabblad 1 laat kort zien wat het totaal aantal ATM's wereldwijd was in de afgelopen jaren, Tabblad 2 laat zien wat het aantal ATM's per land was in de afgelopen jaren (d.m.v. het dropdown menu kunt u een land naar keuze invullen), Tabblad 3 laat zien wat de ")
    st.markdown("Bronnen:")
    st.markdown("https://ansperformance.eu/reference/dataset/airport-traffic/")
    st.markdown("https://www.eurocontrol.int/publication/eurocontrol-forecast-update-2022-2028")


# In[22]:


#Code voor het eerste tabblad
with tab1:
    
    st.header("Het aantal ATM's (Wereldwijd)")
    st.write("In dit tabblad wordt er laten zien wa het aantal ATM's is wereldwijd over de afgelopen jaren. En waarom er een eventuele daling/stijging in zat.")
    
#Code voor de lineplot
    algemeen = px.line(Totaal_ATM, x = "YEAR", y = Totaal_ATM.columns, title = "Totaal ATM's per Jaar")
    algemeen.update_xaxes(title = "Tijd (Jaren)")
    algemeen.update_yaxes(title = "Aantal ATM's")
    st.plotly_chart(algemeen)


# In[39]:


#Code voor het derde tabblad
with tab2:
    st.header("Het aantal ATM's per Airport")
    st.write("In dit tabblad wordt er laten zien wat het aantal ATM's per airport is over de afgelopen jaren. U kunt zelf een airport uitkiezen door middel van het dropdown menu.")

#Keuze voor overzicht continent of voor een individueel land
    continent = st.checkbox("Klik hier als u het verloop in het aantal ATM's voor een specifiek land wilt zien")

#Code voor de plot van decontinenten
    if continent is False:
        lineplot = px.line(Totaal_per_continent, x = "YEAR", y = Totaal_per_continent.columns, 
                   title = "Totaal ATM's per Continent per Jaar")
        lineplot.update_xaxes(title = "Tijd (Jaren)")
        lineplot.update_yaxes(title = "Aantal ATM's")
        st.plotly_chart(lineplot)

    else:
#Dropdown menu voor de variabele van de grafiek
        airport_variabele = st.selectbox("Kies hier een variabele voor de grafiek: ", airport_opties)
    
#Code voor de lineplots per airport
        lineplot = px.line(Totaal_per_airport, x = "YEAR", y = airport_variabele, 
                          title = "Totaal ATM's per Jaar op '" + airport_variabele + "'")
        lineplot.update_xaxes(title = "Tijd (Jaren)")
        lineplot.update_yaxes(title = "Aantal ATM's")
        st.plotly_chart(lineplot)


# In[23]:


#Code voor het tweede tabblad
with tab3:
    
    st.header("Het aantal ATM's per Land")
    st.write("In dit tabblad wordt er laten zien wat het aantal ATM's per land is over de afgelopen jaren. U kunt zelf een land uitkiezen door middel van het dropdown menu.")

#Dropdown menu voor de variabele van de grafiek
    land_variabele = st.selectbox("Kies hier een variabele voor de grafiek: ", land_opties)
    
#Code voor de lineplots
    lineplot = px.line(Totaal_per_land, x = "YEAR", y = land_variabele, 
                      title = "Totaal ATM's per Jaar in '" + land_variabele + "'")
    lineplot.update_xaxes(title = "Tijd (Jaren)")
    lineplot.update_yaxes(title = "Aantal ATM's")
    st.plotly_chart(lineplot)


# In[32]:


#Code voor het vierde tabblad
with tab4:
    
    st.header("Voorspelling van het aantal ATM's")
    st.write("In dit tabblad wordt er laten zien wat het verwachte aantal ATM's gaat zijn in de komende jaren.")
    
#Dropdown menu voor de verschillende landen
    land_variabele = st.selectbox("Kies hier een land waarvoor u de data wilt bekijken: ", land_opties)

#Code voor de plots over de voorspelling per land
    dfs = {"Beste Scenario" : Voorspelling_best, "Gemiddeld Scenario" : Voorspelling_average, 
           "Slechtste Scenario" : Voorspelling_worst}

    fig = go.Figure()

    for i in dfs:
        fig = fig.add_trace(go.Line(x = dfs[i]["YEAR"], y = dfs[i][land_variabele], name = i))
        fig.update_layout(title = "Voorspelling Scenario's in '" + land_variabele + "'")
    
    st.plotly_chart(fig)

