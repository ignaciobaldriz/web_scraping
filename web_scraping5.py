# WEB SCRAPING

############################################################################################################

# Libraries

from urllib.request import urlopen
from bs4 import BeautifulSoup
from scrapy import Selector

import requests
import re

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import json

############################################################################################################

# Selectro path for the element price of an item price in MercadoLibre
# To get the link: price of clouth / inspect / right click copy selector / grab only the unique part from right to left comeared with other elements
link = 'div > div > a > div > div.ui-search-item__group.ui-search-item__group--price > div > div > span.price-tag.ui-search-price__part > span.price-tag-fraction'

# Function that takes a url and the price link, and returns all the prices as a list
def get_link(url, link):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    prices = soup.select(link)

    cash_list = []
    
    for price in prices:
        price_str = str(price)   # Convert the price to a string
        price_str_notdot = price_str.replace(".","")   # Eliminate the "." so all numbers has the same format
        cash = re.search('\d+', price_str_notdot).group()   # Grab the number with regex
        cash = int(cash)             # Convert the string number to integer
        cash_list.append(cash)       # Append to the empty list
    
    return cash_list

# Function that takes a lists of urls and the price link, and applies to every url the get_link function,
# It returns the list of prices for each clouthes
def total_articles_sum(urls, link):
    
    cash_sum = []

    for url in urls:
        cash = get_link(url, link)
        cash_sum += cash
    
    return cash_sum

# Generate a pandas dataframe to populate it with the extracted data
df2 = pd.DataFrame(columns=['price', 'type', 'company'])
df2

# Function that takes a price_company function, a company name and a data frame, and populate the data frame by rows with the info of the company
def populate_df(prices_company, company, df2):
        
        for price in prices_company['tshirts']:
                df2 = df2.append({'price': price, 'type':'tshirt', 'company':company}, ignore_index=True)
        
        for price in prices_company['pants']:
                df2 = df2.append({'price': price, 'type':'pant', 'company':company}, ignore_index=True)
        
        for price in prices_company['jackets']:
                df2 = df2.append({'price': price, 'type':'jacket', 'company':company}, ignore_index=True)
        
        for price in prices_company['boxers']:
                df2 = df2.append({'price': price, 'type':'boxer', 'company':company}, ignore_index=True)
        
        for price in prices_company['sweaters']:
                df2 = df2.append({'price': price, 'type':'sweater', 'company':company}, ignore_index=True)
        
        for price in prices_company['shirts']:
                df2 = df2.append({'price': price, 'type':'shirt', 'company':company}, ignore_index=True)
        
        for price in prices_company['shorts']:
                df2 = df2.append({'price': price, 'type':'short', 'company':company}, ignore_index=True)
        
        return df2

############################################################################################################
############################################################################################################

# LEVIS

# Generate a dictionary of urls: each component of the dictinary is a list of all the pages (urls) of a clouthes
URLS_LEVIS = {
        'urls_levis_tshirts': 
                    ["https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Tienda_levis#origin=os_carousel&position=1&id=572",
                     "https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Desde_49_Tienda_levis",
                     "https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Desde_97_Tienda_levis" ],
        
        'urls_levis_pants': 
                   ["https://listado.mercadolibre.com.uy/pantalones-jeans-joggings/_Tienda_levis",
                    "https://listado.mercadolibre.com.uy/pantalones-jeans-joggings/_Desde_49_Tienda_levis",
                    "https://listado.mercadolibre.com.uy/pantalones-jeans-joggings/_Desde_97_Tienda_levis"],
        
        'urls_levis_jackets': 
                   ["https://listado.mercadolibre.com.uy/camperas-tapados-gabardinas/_Tienda_levis"],

        'urls_levis_boxers': 
                   ["https://listado.mercadolibre.com.uy/ropa-interior-dormir/_Tienda_levis"],

        'urls_levis_sweaters': 
                   ["https://listado.mercadolibre.com.uy/ropa/buzos-canguros/_Tienda_levis"],

        'urls_levis_shirts': 
                   ["https://listado.mercadolibre.com.uy/ropa/camisas/_Tienda_levis"],

        'urls_levis_shorts': 
                   ["https://listado.mercadolibre.com.uy/ropa/bermudas-shorts/_Tienda_levis"]
        }

# Generate a dictionary with each prices list

prices_levis = { 'tshirts': total_articles_sum(URLS_LEVIS['urls_levis_tshirts'], link), 
                 'pants': total_articles_sum(URLS_LEVIS['urls_levis_pants'], link),
                 'jackets': total_articles_sum(URLS_LEVIS['urls_levis_jackets'], link),
                 'boxers': total_articles_sum(URLS_LEVIS['urls_levis_boxers'], link), 
                 'sweaters': total_articles_sum(URLS_LEVIS['urls_levis_sweaters'], link),
                 'shirts': total_articles_sum(URLS_LEVIS['urls_levis_shirts'], link),
                 'shorts': total_articles_sum(URLS_LEVIS['urls_levis_shorts'], link)}

# Populate de DataFrame with the average price for each clouthes
levis = 'levis'
df2 = populate_df(prices_levis, levis, df2)

############################################################################################################

# BAS

# Generate a dictionary of urls: each component of the dictinary is a list of all the pages (urls) of a clouthes
URLS_BAS = {
        'urls_bas_tshirts': 
                    ["https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Tienda_bas",
                     "https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Desde_49_Tienda_bas",
                     "https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Desde_97_Tienda_bas"],       
        'urls_bas_pants': 
                   ["https://listado.mercadolibre.com.uy/pantalones-jeans-joggings/_Tienda_bas",
                    "https://listado.mercadolibre.com.uy/pantalones-jeans-joggings/_Desde_49_Tienda_bas"],        
        'urls_bas_jackets': 
                   ["https://listado.mercadolibre.com.uy/camperas-tapados-gabardinas/_Tienda_bas"],
        'urls_bas_boxers': 
                   ["https://listado.mercadolibre.com.uy/ropa-interior-dormir/_Tienda_bas"],
        'urls_bas_sweaters': 
                   ["https://listado.mercadolibre.com.uy/camperas-tapados-gabardinas/_Tienda_bas"],
        'urls_bas_shirts': 
                   ["https://listado.mercadolibre.com.uy/ropa/camisas/_Tienda_bas"],
        'urls_bas_shorts': 
                   ["https://listado.mercadolibre.com.uy/ropa/bermudas-shorts/_Tienda_bas"]
        }

# Generate a dictionary with each prices list

prices_bas = { 'tshirts': total_articles_sum(URLS_BAS['urls_bas_tshirts'], link), 
                 'pants': total_articles_sum(URLS_BAS['urls_bas_pants'], link),
                 'jackets': total_articles_sum(URLS_BAS['urls_bas_jackets'], link),
                 'boxers': total_articles_sum(URLS_BAS['urls_bas_boxers'], link), 
                 'sweaters': total_articles_sum(URLS_BAS['urls_bas_sweaters'], link),
                 'shirts': total_articles_sum(URLS_BAS['urls_bas_shirts'], link),
                 'shorts': total_articles_sum(URLS_BAS['urls_bas_shorts'], link)}

# Populate de DataFrame with the average price for each clouthes
bas = 'bas'
df2 = populate_df(prices_bas, bas, df2)

############################################################################################################

# KEVINGSTON

# Generate a dictionary of urls: each component of the dictinary is a list of all the pages (urls) of a clouthes
URLS_KEVINGSTON = {
        'urls_kevingston_tshirts': 
                    ["https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Tienda_kevingston",
                     "https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Desde_49_Tienda_kevingston"],
        
        'urls_kevingston_pants': 
                   ["https://listado.mercadolibre.com.uy/pantalones-jeans-joggings/_Tienda_kevingston"],
        
        'urls_kevingston_jackets': 
                   ["https://listado.mercadolibre.com.uy/camperas-tapados-gabardinas/_Tienda_kevingston"],

        'urls_kevingston_boxers': 
                   ["https://listado.mercadolibre.com.uy/ropa-interior-dormir/_Tienda_kevingston",
                    "https://listado.mercadolibre.com.uy/ropa-interior-dormir/_Desde_49_Tienda_kevingston"],

        'urls_kevingston_sweaters': 
                   ["https://listado.mercadolibre.com.uy/ropa/buzos-canguros/_Tienda_kevingston"],

        'urls_kevingston_shirts': 
                   ["https://listado.mercadolibre.com.uy/ropa/camisas/_Tienda_kevingston"],

        'urls_kevingston_shorts': 
                   ["https://listado.mercadolibre.com.uy/ropa/bermudas-shorts/_Tienda_kevingston"]
        }

# Generate a dictionary with each prices list
prices_kevingston = { 'tshirts': total_articles_sum(URLS_KEVINGSTON['urls_kevingston_tshirts'], link), 
                      'pants': total_articles_sum(URLS_KEVINGSTON['urls_kevingston_pants'], link),
                      'jackets': total_articles_sum(URLS_KEVINGSTON['urls_kevingston_jackets'], link),
                      'boxers': total_articles_sum(URLS_KEVINGSTON['urls_kevingston_boxers'], link), 
                      'sweaters': total_articles_sum(URLS_KEVINGSTON['urls_kevingston_sweaters'], link),
                      'shirts': total_articles_sum(URLS_KEVINGSTON['urls_kevingston_shirts'], link),
                      'shorts': total_articles_sum(URLS_KEVINGSTON['urls_kevingston_shorts'], link)}

# Populate de DataFrame with the average price for each clouthes
kevingston = 'kevingston'
df2 = populate_df(prices_kevingston, kevingston, df2)

############################################################################################################

# LAISLA

# Generate a dictionary of urls: each component of the dictinary is a list of all the pages (urls) of a clouthes
URLS_LAISLA = {
        'urls_laisla_tshirts': 
                    ["https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Tienda_la-isla",
                     "https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Desde_49_Tienda_la-isla"],
        
        'urls_laisla_pants': 
                   ["https://listado.mercadolibre.com.uy/pantalones-jeans-joggings/_Tienda_la-isla"],
        
        'urls_laisla_jackets': 
                   ["https://listado.mercadolibre.com.uy/camperas-tapados-gabardinas/_Tienda_la-isla"],

        'urls_laisla_boxers': 
                   [],

        'urls_laisla_sweaters': 
                   ["https://listado.mercadolibre.com.uy/ropa/buzos-canguros/_Tienda_la-isla"],

        'urls_laisla_shirts': 
                   ["https://listado.mercadolibre.com.uy/ropa/camisas/_Tienda_la-isla"],

        'urls_laisla_shorts': 
                   ["https://listado.mercadolibre.com.uy/ropa/bermudas-shorts/_Tienda_la-isla",
                    "https://listado.mercadolibre.com.uy/ropa/bermudas-shorts/_Desde_49_Tienda_la-isla",
                    "https://listado.mercadolibre.com.uy/ropa/bermudas-shorts/_Desde_97_Tienda_la-isla"]
        }

# Generate a dictionary with each prices list

prices_laisla = { 'tshirts': total_articles_sum(URLS_LAISLA['urls_laisla_tshirts'], link), 
                 'pants': total_articles_sum(URLS_LAISLA['urls_laisla_pants'], link),
                 'jackets': total_articles_sum(URLS_LAISLA['urls_laisla_jackets'], link),
                 'boxers': total_articles_sum(URLS_LAISLA['urls_laisla_boxers'], link), 
                 'sweaters': total_articles_sum(URLS_LAISLA['urls_laisla_sweaters'], link),
                 'shirts': total_articles_sum(URLS_LAISLA['urls_laisla_shirts'], link),
                 'shorts': total_articles_sum(URLS_LAISLA['urls_laisla_shorts'], link)}

# Populate de DataFrame with the average price for each clouthes
laisla = 'laisla'
df2 = populate_df(prices_laisla, laisla, df2)

###########################################################################################################

# NORTHSALES

# Generate a dictionary of urls: each component of the dictinary is a list of all the pages (urls) of a clouthes
URLS_NORTHSALES = {
        'urls_northsales_tshirts': 
                    ["https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Tienda_northsales-performance",
                     "https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Desde_49_Tienda_northsales-performance"],
        
        'urls_northsales_pants': 
                   ["https://listado.mercadolibre.com.uy/pantalones-jeans-joggings/_Tienda_northsales-performance"],
        
        'urls_northsales_jackets': 
                   ["https://listado.mercadolibre.com.uy/camperas-tapados-gabardinas/_Tienda_north-sails"],

        'urls_northsales_boxers': 
                   [],

        'urls_northsales_sweaters': 
                   ["https://listado.mercadolibre.com.uy/ropa/buzos-canguros/_Tienda_north-sails"],

        'urls_northsales_shirts': 
                   ["https://listado.mercadolibre.com.uy/ropa/camisas/_Tienda_north-sails"],

        'urls_northsales_shorts': 
                   ["https://listado.mercadolibre.com.uy/ropa/bermudas-shorts/_Tienda_north-sails"]
        }

# Generate a dictionary with each prices list

prices_northsales = { 'tshirts': total_articles_sum(URLS_NORTHSALES['urls_northsales_tshirts'], link), 
                 'pants': total_articles_sum(URLS_NORTHSALES['urls_northsales_pants'], link),
                 'jackets': total_articles_sum(URLS_NORTHSALES['urls_northsales_jackets'], link),
                 'boxers': total_articles_sum(URLS_NORTHSALES['urls_northsales_boxers'], link), 
                 'sweaters': total_articles_sum(URLS_NORTHSALES['urls_northsales_sweaters'], link),
                 'shirts': total_articles_sum(URLS_NORTHSALES['urls_northsales_shirts'], link),
                 'shorts': total_articles_sum(URLS_NORTHSALES['urls_northsales_shorts'], link)}

# Populate de DataFrame with the average price for each clouthes
northsales = 'northsales'
df2 = populate_df(prices_northsales, northsales, df2)

#########################################################################################################################

# CAT

# Generate a dictionary of urls: each component of the dictinary is a list of all the pages (urls) of a clouthes
URLS_CAT = {
        'urls_cat_tshirts': 
                    ["https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Tienda_cat-lifestyle"],
        
        'urls_cat_pants': 
                   ["https://listado.mercadolibre.com.uy/pantalones-jeans-joggings/_Tienda_cat-lifestyle"],
        
        'urls_cat_jackets': 
                   ["https://listado.mercadolibre.com.uy/camperas-tapados-gabardinas/_Tienda_cat-lifestyle_NoIndex_True"],

        'urls_cat_boxers': 
                   [],

        'urls_cat_sweaters': 
                   [],

        'urls_cat_shirts': 
                   ["https://listado.mercadolibre.com.uy/ropa/camisas/_Tienda_cat-lifestyle"],

        'urls_cat_shorts': 
                   []
        }

# Generate a dictionary with each prices list

prices_cat = { 'tshirts': total_articles_sum(URLS_CAT['urls_cat_tshirts'], link), 
                 'pants': total_articles_sum(URLS_CAT['urls_cat_pants'], link),
                 'jackets': total_articles_sum(URLS_CAT['urls_cat_jackets'], link),
                 'boxers': total_articles_sum(URLS_CAT['urls_cat_boxers'], link), 
                 'sweaters': total_articles_sum(URLS_CAT['urls_cat_sweaters'], link),
                 'shirts': total_articles_sum(URLS_CAT['urls_cat_shirts'], link),
                 'shorts': total_articles_sum(URLS_CAT['urls_cat_shorts'], link)}

# Populate de DataFrame with the average price for each clouthes
cat = 'cat'
df2 = populate_df(prices_cat, cat, df2)

############################################################################

# COLUMBIA

# Generate a dictionary of urls: each component of the dictinary is a list of all the pages (urls) of a clouthes
URLS_COLUMBIA = {
        'urls_columbia_tshirts': 
                    ["https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Tienda_columbia-sportwear"],
        
        'urls_columbia_pants': 
                   ["https://listado.mercadolibre.com.uy/pantalones-jeans-joggings/_Tienda_columbia-sportwear"],
        
        'urls_columbia_jackets': 
                   ["https://listado.mercadolibre.com.uy/camperas-tapados-gabardinas/_Tienda_columbia-sportwear"],

        'urls_columbia_boxers': 
                   [],

        'urls_columbia_sweaters': 
                   ["https://listado.mercadolibre.com.uy/ropa/buzos-canguros/_Tienda_columbia-sportwear"],

        'urls_columbia_shirts': 
                   ["https://listado.mercadolibre.com.uy/ropa/camisas/_Tienda_columbia-sportwear"],

        'urls_columbia_shorts': 
                   ["https://listado.mercadolibre.com.uy/ropa/bermudas-shorts/_Tienda_columbia-sportwear"]
        }

# Generate a dictionary with each prices list

prices_columbia = { 'tshirts': total_articles_sum(URLS_COLUMBIA['urls_columbia_tshirts'], link), 
                 'pants': total_articles_sum(URLS_COLUMBIA['urls_columbia_pants'], link),
                 'jackets': total_articles_sum(URLS_COLUMBIA['urls_columbia_jackets'], link),
                 'boxers': total_articles_sum(URLS_COLUMBIA['urls_columbia_boxers'], link), 
                 'sweaters': total_articles_sum(URLS_COLUMBIA['urls_columbia_sweaters'], link),
                 'shirts': total_articles_sum(URLS_COLUMBIA['urls_columbia_shirts'], link),
                 'shorts': total_articles_sum(URLS_COLUMBIA['urls_columbia_shorts'], link)}

# Populate de DataFrame with the average price for each clouthes
columbia = 'columbia'
df2 = populate_df(prices_columbia, columbia, df2)

############################################################################

# JACKJONES

# Generate a dictionary of urls: each component of the dictinary is a list of all the pages (urls) of a clouthes
URLS_JACKJONES = {
        'urls_jackjones_tshirts': 
                    ["https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Tienda_jack-jones"],
        
        'urls_jackjones_pants': 
                   ["https://listado.mercadolibre.com.uy/pantalones-jeans-joggings/_Tienda_jack-jonesr",
                   "https://listado.mercadolibre.com.uy/pantalones-jeans-joggings/_Desde_49_Tienda_jack-jones"],
        
        'urls_jackjones_jackets': 
                   ["https://listado.mercadolibre.com.uy/camperas-tapados-gabardinas/_Tienda_jack-jones"],

        'urls_jackjones_boxers': 
                   ["https://listado.mercadolibre.com.uy/ropa-interior-dormir/_Tienda_jack-jones"],

        'urls_jackjones_sweaters': 
                   ["https://listado.mercadolibre.com.uy/ropa/buzos-canguros/_Tienda_jack-jones"],

        'urls_jackjones_shirts': 
                   ["https://listado.mercadolibre.com.uy/ropa/camisas/_Tienda_jack-jones"],

        'urls_jackjones_shorts': 
                   []
        }

# Generate a dictionary with each prices list

prices_jackjones = { 'tshirts': total_articles_sum(URLS_JACKJONES['urls_jackjones_tshirts'], link), 
                 'pants': total_articles_sum(URLS_JACKJONES['urls_jackjones_pants'], link),
                 'jackets': total_articles_sum(URLS_JACKJONES['urls_jackjones_jackets'], link),
                 'boxers': total_articles_sum(URLS_JACKJONES['urls_jackjones_boxers'], link), 
                 'sweaters': total_articles_sum(URLS_JACKJONES['urls_jackjones_sweaters'], link),
                 'shirts': total_articles_sum(URLS_JACKJONES['urls_jackjones_shirts'], link),
                 'shorts': total_articles_sum(URLS_JACKJONES['urls_jackjones_shorts'], link)}

# Populate de DataFrame with the average price for each clouthes
jackjones = 'jackjones'
df2 = populate_df(prices_jackjones, jackjones, df2)

############################################################################

# JEANVERNIER

# Generate a dictionary of urls: each component of the dictinary is a list of all the pages (urls) of a clouthes
URLS_JEANVERNIER = {
        'urls_jeanvernier_tshirts': 
                    ["https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Tienda_jean-vernier"],
        
        'urls_jeanvernier_pants': 
                   ["https://listado.mercadolibre.com.uy/pantalones-jeans-joggings/_Tienda_jean-vernier"],
        
        'urls_jeanvernier_jackets': 
                   ["https://listado.mercadolibre.com.uy/camperas-tapados-gabardinas/_Tienda_jean-vernier"],

        'urls_jeanvernier_boxers': 
                   [],

        'urls_jeanvernier_sweaters': 
                   ["https://listado.mercadolibre.com.uy/saquitos-sweaters-chalecos/_Tienda_jean-vernier"],

        'urls_jeanvernier_shirts': 
                   ["https://listado.mercadolibre.com.uy/ropa/camisas/_Tienda_jean-vernier",
                    "https://listado.mercadolibre.com.uy/ropa/camisas/_Desde_49_Tienda_jean-vernier"],

        'urls_jeanvernier_shorts': 
                   ["https://listado.mercadolibre.com.uy/ropa/bermudas-shorts/_Tienda_jean-vernier"]
        }

# Generate a dictionary with each prices list

prices_jeanvernier = { 'tshirts': total_articles_sum(URLS_JEANVERNIER['urls_jeanvernier_tshirts'], link), 
                 'pants': total_articles_sum(URLS_JEANVERNIER['urls_jeanvernier_pants'], link),
                 'jackets': total_articles_sum(URLS_JEANVERNIER['urls_jeanvernier_jackets'], link),
                 'boxers': total_articles_sum(URLS_JEANVERNIER['urls_jeanvernier_boxers'], link), 
                 'sweaters': total_articles_sum(URLS_JEANVERNIER['urls_jeanvernier_sweaters'], link),
                 'shirts': total_articles_sum(URLS_JEANVERNIER['urls_jeanvernier_shirts'], link),
                 'shorts': total_articles_sum(URLS_JEANVERNIER['urls_jeanvernier_shorts'], link)}

# Populate de DataFrame with the average price for each clouthes
jeanvernier = 'jeanvernier'
df2 = populate_df(prices_jeanvernier, jeanvernier, df2)

############################################################################

# PAMPERO

# Generate a dictionary of urls: each component of the dictinary is a list of all the pages (urls) of a clouthes
URLS_PAMPERO = {
        'urls_pampero_tshirts': 
                    ["https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Tienda_pampero"],
        
        'urls_pampero_pants': 
                   ["https://listado.mercadolibre.com.uy/pantalones-jeans-joggings/_Tienda_pampero"],
        
        'urls_pampero_jackets': 
                   ["https://listado.mercadolibre.com.uy/camperas-tapados-gabardinas/_Tienda_pampero"],

        'urls_pampero_boxers': 
                   [],

        'urls_pampero_sweaters': 
                   ["https://listado.mercadolibre.com.uy/saquitos-sweaters-chalecos/_Tienda_pampero"],

        'urls_pampero_shirts': 
                   ["https://listado.mercadolibre.com.uy/ropa/camisas/_Tienda_pampero"],

        'urls_pampero_shorts': 
                   ["https://listado.mercadolibre.com.uy/ropa/bermudas-shorts/_Tienda_pampero"]
        }

# Generate a dictionary with each prices list

prices_pampero = { 'tshirts': total_articles_sum(URLS_PAMPERO['urls_pampero_tshirts'], link), 
                 'pants': total_articles_sum(URLS_PAMPERO['urls_pampero_pants'], link),
                 'jackets': total_articles_sum(URLS_PAMPERO['urls_pampero_jackets'], link),
                 'boxers': total_articles_sum(URLS_PAMPERO['urls_pampero_boxers'], link), 
                 'sweaters': total_articles_sum(URLS_PAMPERO['urls_pampero_sweaters'], link),
                 'shirts': total_articles_sum(URLS_PAMPERO['urls_pampero_shirts'], link),
                 'shorts': total_articles_sum(URLS_PAMPERO['urls_pampero_shorts'], link)}

# Populate de DataFrame with the average price for each clouthes
pampero = 'pampero'
df2 = populate_df(prices_pampero, pampero, df2)
   
############################################################################

# ROCKFORD

# Generate a dictionary of urls: each component of the dictinary is a list of all the pages (urls) of a clouthes
URLS_ROCKFORD = {
        'urls_rockford_tshirts': 
                    ["https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Tienda_rockford"],
        
        'urls_rockford_pants': 
                   ["https://listado.mercadolibre.com.uy/pantalones-jeans-joggings/_Tienda_rockford"],
        
        'urls_rockford_jackets': 
                   ["https://listado.mercadolibre.com.uy/camperas-tapados-gabardinas/_Tienda_rockford"],

        'urls_rockford_boxers': 
                   [],

        'urls_rockford_sweaters': 
                   ["https://listado.mercadolibre.com.uy/saquitos-sweaters-chalecos/_Tienda_rockford"],

        'urls_rockford_shirts': 
                   ["https://listado.mercadolibre.com.uy/ropa/camisas/_Tienda_rockford"],

        'urls_rockford_shorts': 
                   ["https://listado.mercadolibre.com.uy/ropa/bermudas-shorts/_Tienda_rockford"]
        }

# Generate a dictionary with each prices list

prices_rockford = { 'tshirts': total_articles_sum(URLS_ROCKFORD['urls_rockford_tshirts'], link), 
                 'pants': total_articles_sum(URLS_ROCKFORD['urls_rockford_pants'], link),
                 'jackets': total_articles_sum(URLS_ROCKFORD['urls_rockford_jackets'], link),
                 'boxers': total_articles_sum(URLS_ROCKFORD['urls_rockford_boxers'], link), 
                 'sweaters': total_articles_sum(URLS_ROCKFORD['urls_rockford_sweaters'], link),
                 'shirts': total_articles_sum(URLS_ROCKFORD['urls_rockford_shirts'], link),
                 'shorts': total_articles_sum(URLS_ROCKFORD['urls_rockford_shorts'], link)}

# Populate de DataFrame with the average price for each clouthes
rockford = 'rockford'
df2 = populate_df(prices_rockford, rockford, df2)

############################################################################

# HERING

# Generate a dictionary of urls: each component of the dictinary is a list of all the pages (urls) of a clouthes
URLS_HERING = {
        'urls_hering_tshirts': 
                    ["https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Tienda_hering",
                     "https://listado.mercadolibre.com.uy/remeras-musculosas-chombas/_Desde_49_Tienda_hering"],
        
        'urls_hering_pants': 
                   ["https://listado.mercadolibre.com.uy/pantalones-jeans-joggings/_Tienda_hering"],
        
        'urls_hering_jackets': 
                   ["https://listado.mercadolibre.com.uy/camperas-tapados-gabardinas/_Tienda_hering"],

        'urls_hering_boxers': 
                   ["https://listado.mercadolibre.com.uy/ropa-interior-dormir/_Tienda_hering"],

        'urls_hering_sweaters': 
                   ["https://listado.mercadolibre.com.uy/ropa/buzos-canguros/_Tienda_hering"],

        'urls_hering_shirts': 
                   [],

        'urls_hering_shorts': 
                   ["https://listado.mercadolibre.com.uy/ropa/bermudas-shorts/_Tienda_hering"]
        }

# Generate a dictionary with each prices list

prices_hering = { 'tshirts': total_articles_sum(URLS_HERING['urls_hering_tshirts'], link), 
                 'pants': total_articles_sum(URLS_HERING['urls_hering_pants'], link),
                 'jackets': total_articles_sum(URLS_HERING['urls_hering_jackets'], link),
                 'boxers': total_articles_sum(URLS_HERING['urls_hering_boxers'], link), 
                 'sweaters': total_articles_sum(URLS_HERING['urls_hering_sweaters'], link),
                 'shirts': total_articles_sum(URLS_HERING['urls_hering_shirts'], link),
                 'shorts': total_articles_sum(URLS_HERING['urls_hering_shorts'], link)}

# Populate de DataFrame with the average price for each clouthes
hering = 'hering'
df2 = populate_df(prices_hering, hering, df2)

############################################################################

# Check consistency of the data frame

df2.head()
df2.info()
df2.describe # 2071 rows x 3 columns

df2['company'].value_counts()   # https://www.datacamp.com/community/tutorials/categorical-data
df2['type'].value_counts()
df2['price'].describe

# Convert variables to the apropiate format
df2["price"] = df2["price"].astype(str).astype(int)
df2.info()

# Save df2
df2.to_csv("df2_23_11_20.csv")

# Open last saved df2
df2 = pd.read_csv("df2_23_11_20.csv")

#####################################################################

# DESCRIPTIVE GRAPHICS

#####

# General

# Scatterplot of all company prices
sns.scatterplot(x = "company", y = "price", data = df2, hue = "type")
plt.xticks(rotation=30)
plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)
plt.title("Companies Prices for Each Clothe")
plt.show()

# Heat map of counts company vs type
cross = pd.crosstab(index = df2['company'],
                    columns = df2['type'])
sns.heatmap(cross, cmap='rocket_r', annot=True, fmt='g')
plt.title("Counts of clothes for Each Company")
plt.show()

#####

# Filttered by company: ex. Levis

# Boxplot of clothes
sns.catplot(x="type", y="price", 
            data=df2[df2["company"]=="levis"],
            kind="box",
            palette = "RdPu")
plt.title("Levi's Clothes Prices")
plt.show()

# Group_by table: prices of each clothes
df2[df2["company"]=="levis"].groupby('type')['price']\
        .agg([np.min, np.mean, np.max]).reset_index()

# Count prices of shirts filtered by Levis
sns.countplot(data = df2[(df2.company == "levis") & (df2.type == "shirt")],
              y = "price",
              palette = "RdPu")
plt.title("Levi's Shirts Counts for Each Price")
plt.show()

#####

# Filttered by clothes: ex. pant

# Ex. boxplot of pants
sns.catplot(x="company", y="price", 
            data=df2[df2["type"]=="pant"],
            kind="box",
            palette = "PuOr")
plt.xticks(rotation=45)
plt.title("Pants Prices for Each Company")
plt.show()

# Group by table pants
df2[df2["type"]=="pant"].groupby('company')['price']\
        .agg([np.min, np.mean, np.max]).reset_index()

# Count prices of Hering filttered by pants
sns.countplot(data = df2[(df2.type == "pant") & (df2.company == "hering")],
              y = "price",
            palette = "PuOr")
plt.title("Hering Pants Count for Each Price")
plt.show()


