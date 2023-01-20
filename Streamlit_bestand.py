#!/usr/bin/env python
# coding: utf-8

# # Bestand voor Streamlit

# ##### Gemaakt door:   Kevin Linders

# ## Importeren packages

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.express as px
import country_converter as coco
import plotly.graph_objects as go


# ## Data inladen en kleine toevoegingen

# In[2]:


#Hieronder laad ik de benodigde datasets in
Totaal_ATM = pd.read_csv("Total_ATM.csv")
Totaal_per_airport = pd.read_csv("Tot_per_airport.csv")
Totaal_per_land = pd.read_csv("Totaal_per_land.csv")
Totaal_per_continent = pd.read_csv("Totaal_per_continent.csv")
Voorspelling_best = pd.read_csv("Voorspelling_hoog.csv")
Voorspelling_average = pd.read_csv("Voorspelling_basis.csv")
Voorspelling_worst = pd.read_csv("Voorspelling_laag.csv")
df_CO2 = pd.read_csv("CO2_2.csv")


# In[3]:


#Hier verander ik de naam van de kolom met de jaartallen
Voorspelling_best = Voorspelling_best.rename(columns = {"2":"YEAR"})
Voorspelling_average = Voorspelling_average.rename(columns = {"2":"YEAR"})
Voorspelling_worst = Voorspelling_worst.rename(columns = {"2":"YEAR"})


# In[4]:


#Kolom Unnamed verwijderen van het dataframe "Totaal_per_continent"
Totaal_per_continent = Totaal_per_continent.drop(columns = "Unnamed: 0")


# In[5]:


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

opties_airport = ['Abad', 'Aberdeen', 'Agen-La Garenne', 'Ajaccio-Napoléon-Bonaparte', 'Aktion', 'Al Massira', 'Albacete', 
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

# In[6]:


st.set_page_config(page_title = "Airport Traffic",
                  page_icon = ":bar_chart:")


# In[7]:


#Tabbladen maken
hoofdtab, tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Hoofdpagina", "Algemeen Overzicht", "Overzicht per Airport", 
                                      "Overzicht per Land", "Voorspelling aantal Bewegingen", "Conclusie", "Gedane Aannames"])


# In[19]:


#Code voor de Hoofdpagina
with hoofdtab:
    st.header("Aantal ATM's van afgelopen jaren en in de toekomst (Focus Europa)")
    st.write("In dit dashboard wordt er laten zien wat het aantal Air Traffic Movements (ATM's) wereldwijd is geweest in de afgelopen jaren. Deze data is van ANSperformance (Eurocontrol). Daarnaast wordt er ook gekeken naar de toekomst en wordt er een voorspelling gedaan over het aantal ATM's. De voorspelling over het aantal ATM's wordt besproken aan de hand van de voorspelling van het aantal vliegbewegingen. De bron voor deze data is Eurocontrol, zij hebben een voorspelling gedaan t/m 2028. In dit dashboard ligt de focus op de landen in Europa. Het dashboard is op de volgende manier opgebouwd: ")
    st.markdown("- Tabblad 1 laat kort het aantal ATM's zien over de afgelopen jaren wereldwijd")
    st.markdown("- Tabblad 2 laat zien wat het aantal ATM's per airport was over de afgelopen jaren")
    st.markdown("- Tabblad 3 laat zien wat het aantal ATM's per land was over de afgelopen jaren")
    st.markdown("- Tabblad 4 geeft een inzicht in het aantal bewegingen in de toekomst per land, door middel van 3 scenario's")
    st.markdown("- Tabblad 5 geeft een korte conclusie over de inzichten die dit dashboard heeft gecreërd en welke vervolg onderzoeken nog uitgevoerd kunnen worden")
    st.markdown("- Tabblad 6 is een overzicht van de gedane aannames tijdens het creëren van dit dashboard")
    st.markdown("##")
    st.markdown("Bronnen:")
    st.markdown("- https://ansperformance.eu/reference/dataset/airport-traffic/")
    st.markdown("- https://www.eurocontrol.int/publication/eurocontrol-forecast-update-2022-2028")
    st.markdown("- https://ansperformance.eu/reference/dataset/emissions/")


# In[9]:


#Code voor het eerste tabblad
with tab1:
    
    st.header("Het aantal ATM's (Wereldwijd)")
    st.write("In dit tabblad wordt er laten zien wa het aantal ATM's is wereldwijd over de afgelopen jaren. En waarom er een eventuele daling/stijging in zat.")
    
#Code voor de lineplot
    algemeen = px.line(Totaal_ATM, x = "YEAR", y = Totaal_ATM.columns, title = "Totaal ATM's per Jaar")
    algemeen.update_xaxes(title = "Tijd (Jaren)")
    algemeen.update_yaxes(title = "Aantal ATM's")
    algemeen.update_layout(legend_title_text = "Variabele")
    st.plotly_chart(algemeen)
    
    st.markdown("Bron: https://www.icao.int/sustainability/Pages/Economic-Impacts-of-COVID-19.aspx")


# In[10]:


#Code voor het derde tabblad
with tab2:
    st.header("Het aantal ATM's per Airport")
    st.write("In dit tabblad wordt er laten zien wat het aantal ATM's per airport is over de afgelopen jaren. U kunt zelf een airport uitkiezen door middel van het dropdown menu. Ook kunt u twee airports met elkaar vergelijken door op de daarvoor bestemde checkbox te klikken. Vanuit daar kunt u de gewenste airport, waarmee u wilt vergelijken, kiezen uit het dropdown menu.")

#Keuze voor overzicht continent of voor een individueel land
    continent = st.checkbox("Klik hier als u het verloop in het aantal ATM's voor de continenten wilt zien")

#Code voor de plot van decontinenten
    if continent is True:
        lineplot = px.line(Totaal_per_continent, x = "YEAR", y = Totaal_per_continent.columns, 
                   title = "Totaal ATM's per Continent per Jaar")
        lineplot.update_xaxes(title = "Tijd (Jaren)")
        lineplot.update_yaxes(title = "Aantal ATM's")
        lineplot.update_layout(legend_title_text = "continent")
        st.plotly_chart(lineplot)

    else:
#Dropdown menu voor de variabele van de lineplot
        airport_variabele = st.selectbox("Kies hier een variabele voor de grafiek: ", airport_opties)

#Keuze voor het vergelijken van airports
        vergelijken = st.checkbox("Klik hier als u 2 airports met elkaar wilt vergelijken")
    
        if vergelijken is False:
#Code voor lineplot met 1 airport
            lineplot1 = px.line(Totaal_per_airport, x = "YEAR", y = airport_variabele, 
                              title = "Totaal ATM's per Jaar op '" + airport_variabele + "'")
            lineplot1.update_xaxes(title = "Tijd (Jaren)")
            lineplot1.update_yaxes(title = "Aantal ATM's")
            st.plotly_chart(lineplot1)
        
        else:
#Dropdown menu voor de tweede variabele van de airports
            airport_variabele2 = st.selectbox("Kies hier een tweede variabele voor de plot: ", airport_opties)
    
#Code voor lineplot met 2 airports
            lineplot2 = px.line(Totaal_per_airport, x = "YEAR", y = [airport_variabele, airport_variabele2], 
                              title = "Totaal ATM's per Jaar op '" + airport_variabele + "'")
            lineplot2.update_xaxes(title = "Tijd (Jaren)")
            lineplot2.update_yaxes(title = "Aantal ATM's")
            lineplot2.update_layout(legend_title_text = "Airport")
            st.plotly_chart(lineplot2)


# In[20]:


#Code voor het tweede tabblad
with tab3:
    
    st.header("Het aantal ATM's per Land")
    st.write("In dit tabblad wordt er laten zien wat het aantal ATM's per land is over de afgelopen jaren. U kunt zelf een land uitkiezen door middel van het dropdown menu. Ook kunt u ervoor kiezen om 2 landen met elkaar te vergelijken, daarvoor moet u de tweede checkbox aanvinken en het land waarmee u wilt vergelijken selecteren via het tweede dropdown menu.")

#Dropdown menu voor de variabele van de grafiek
    land_variabele = st.selectbox("Kies hier een variabele voor de grafiek: ", land_opties)
    
#Keuze voor het vergelijken van landen
    vergelijken = st.checkbox("Klik hier als u 2 landen met elkaar wilt vergelijken")
    
#Code voor de lineplots
    if vergelijken is False:
        lineplot = px.line(Totaal_per_land, x = "YEAR", y = land_variabele, 
                          title = "Totaal ATM's per Jaar in '" + land_variabele + "'")
        lineplot.update_xaxes(title = "Tijd (Jaren)")
        lineplot.update_yaxes(title = "Aantal ATM's")
        st.plotly_chart(lineplot)
        
        lineplot3 = px.line(df_CO2, x = "Jaar", y = land_variabele, 
                          title = "Totaal ATM's per Jaar in '" + land_variabele + "'")
        lineplot3.update_xaxes(title = "Tijd (Jaren)")
        lineplot3.update_yaxes(title = "CO2 in tonnen")
        st.plotly_chart(lineplot3)
    
    else:
#Dropdown menu voor de variabele van de grafiek
        land_variabele2 = st.selectbox("Kies hier een tweede variabele voor de plot: ", land_opties)        
        
#Code voor lineplot met 2 landen
        lineplot2 = px.line(Totaal_per_land, x = "YEAR", y = [land_variabele, land_variabele2], 
                          title = "Totaal ATM's per Jaar in '" + land_variabele + "'")
        lineplot2.update_xaxes(title = "Tijd (Jaren)")
        lineplot2.update_yaxes(title = "Aantal ATM's")
        lineplot2.update_layout(legend_title_text = "Land")
        st.plotly_chart(lineplot2)

#Code voor lineplot over het aantal CO2
        lineplot4 = px.line(df_CO2, x = "Jaar", y = [land_variabele, land_variabele2], 
                              title = "Aantal ton CO2 uitstoot per Jaar in '" + land_variabele + "'")
        lineplot4.update_xaxes(title = "Tijd (Jaren)")
        lineplot4.update_yaxes(title = "CO2 in tonnen")
        st.plotly_chart(lineplot4)
    
    st.markdown("- https://ansperformance.eu/reference/dataset/emissions/")


# In[17]:


#Code voor het vierde tabblad
with tab4:
    
    st.header("Voorspelling van het aantal ATM's")
    st.write("In dit tabblad wordt er laten zien wat het verwachte aantal ATM's gaat zijn in de komende jaren. U kunt hieronder een land kiezen waarvan u de data wilt zien. Na het aangeven welk land u wilt zien, krijgt u de plot met 3 mogelijke scenario's te zien.")
    
#Dropdown menu voor de verschillende landen
    land_variabele = st.selectbox("Kies hier een land waarvoor u de data wilt bekijken: ", land_opties)

#Code voor de plots over de voorspelling per land
    dfs = {"Beste Scenario" : Voorspelling_best, "Gemiddeld Scenario" : Voorspelling_average, 
           "Slechtste Scenario" : Voorspelling_worst}

    fig = go.Figure()

    for i in dfs:
        fig = fig.add_trace(go.Line(x = dfs[i]["YEAR"], y = dfs[i][land_variabele], name = i))
        fig.update_layout(title = "Voorspelling Scenario's in '" + land_variabele + "'")
        fig.update_layout(legend_title_text = "Scenario's")
    st.plotly_chart(fig)


# In[15]:


#Code voor het vijfde tabblad
with tab5:
    
    st.header("Conclusie")
    st.write("Al met al heeft u in dit dashboard kunnen zien wat het aantal ATM's per land en per airport was over de afgelopen jaren. Daarnaast heeft u kunnen zien dat het aantal ATM's de komende jaren kan gaan groeien in 3 verschillende scenario's. Dit brengt echter consequenties mee zich mee, want meer ATM's betekend ook dat er meer CO2 uitstoot zal zijn en accepteren de overheden dat. Maar ook het geluidsoverlast speelt een grote rol als het gaat om groeien in het aantal ATM's. Bijvoorbeeld in Nederland, Schiphol mag waarschijnlijk weer gaan groeien vanwege zuinigere vliegtuigen. Echter wordt de geluidsnorm strenger waardoor het aantal vluchten misschien toch niet mag groeien. (Volkskrant) Ook EASA zegt dat er 3 verschillende scenario's zijn met betrekking tot de uitstoot van de luchtvaart. (EASA)")
    st.markdown("##")
    st.subheader("Verder Onderzoek")
    st.write("Na het onderzoek wat ik heb gedaan en ik erachter ben gekomen dat er 3 verschillende scenario's zijn en dat het aantal ATM's gevolgen heeft voor de toekomst, benoemd door EASA. Daarnaast heb ik nog verdere ideeën die uitgevoerd kunnen worden: ")
    st.markdown("- De toename van het aantal precieze ATM's per land (rekeninghoudend met onder andere: GDP, CO2, geluidsoverlast)")
    st.markdown("- Wat voor invloed heeft het aantal ATM's op de klimaat verandering")
    st.markdown("- Wat is de verhouding van soort vluchten in de toekomst en heeft dat invloed")
    st.markdown("##")
    st.markdown("Bronnen: ")
    st.markdown("- https://www.volkskrant.nl/wetenschap/dankzij-schonere-vliegtuigen-mag-schiphol-straks-toch-weer-groeien-hoe-staat-het-ervoor-met-die-toestellen~b18b8c35/?referrer=https%3A%2F%2Fwww.google.com%2F")
    st.markdown("- https://www.easa.europa.eu/eco/eaer/topics/overview-aviation-sector/emissions#emissions-grew-steadily-between-2013-and-2019-and-may")


# In[16]:


#Code voor het zesde tabblad
with tab6:
    
    st.header("Gedane Aannames voor dit dashboard")
    st.write("Hieronder staat een lijst van aannames die zijn gemaakt voor het dashboard. Voor de Scenario's zijn er, zoals verwacht, verschillende aannames per scenario. De aannames zijn gemaakt door de maker zelf en de makers van de datasets. Er wordt dus vanuit gegaan dat:")
    st.markdown("- Het aantal ATM's toeneemt met ongeveer dezelfde stijging als het aantal vliegbewegingen")
    st.markdown("- De datasets van Eurocontrol de juiste informatie bevatten over de afgelopen jaren")
    st.markdown(" ")
    st.markdown("Scenario's Algemeen")
    st.markdown("- De vliegrestricties boven Oekraïne, Rusland, Belarus en Moldavië blijven gelden tot eind 2028")
    st.markdown("- De Covid pandemie vlakt af en de reisrestricties blijven vervallen")
    st.markdown("- Het aantal business passagiers na een sterke stijging redelijk afvlakt")
    st.markdown("- Het aantal mensen wat er tekort was in 2022, in 2023 misschien weer zo is")
    st.markdown("- De cargo vluchten minder snel zullen stijgen als voorheen, door de oorlog in Oekraïne")
    st.markdown(" ")
    st.markdown("Beste Scenario")
    st.markdown("- De meeste Europese landen een gematigde groei hebben van het BBP (GDP)")
    st.markdown("- De impact van de oorlog in Oekraïne op de vraag naar vluchten en brandstof laag blijft")
    st.markdown("- Passagiers weer graag willen gaan vliegen")
    st.markdown("- Het toerisme in de komende jaren nog verder gaat groeien dan de aantal van 2019")
    st.markdown("- Het aantal business snel en sterk toeneemt")
    st.markdown("- De meeste airports en airlines het lukt om op dezelfde capaciteit te zitten als voor de Covid pandemie")
    st.markdown("Gemiddeld Scenario")
    st.markdown("- De meeste Europese landen een zwak BBP (GDP) hebben")
    st.markdown("- Passagiers weer redelijk graag willen gaan vliegen")
    st.markdown("- Zakenreizen gedeeltelijk worden vervangen door online meetings")
    st.markdown("- Europese landen gaan zich meer zorgen maken over het klimaat en willen de CO2 uitstoot reduceren door het aantal vliegbewegingen in te perken")
    st.markdown("- De hoge inflatie de vraag naar beneden haalt")
    st.markdown("- De meeste airports en airlines ervaren problemen met de hoeveelheid bemanning")
    st.markdown("Slechtste Scenario")
    st.markdown("- Een aanzienlijke hoeveelheid Europese landen een sterke daling van de economie heeft")
    st.markdown("- De vraag naar vluchten sterk afneemt vanwege hoge inflatie")
    st.markdown("- De terugkomst van andere Covid varianten")
    st.markdown("- Er een grote hoeveelheid business passagiers overschakelt naar online meetings")
    st.markdown("- Er een groot aantal passagiers niet meer wilt vliegen vanwege de klimaatverandering")
    st.markdown("- De meeste airports en airlines grote problemen hebben met de hoeveelheid bemanning")

