import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
import re
import pandas as pd
import os

import seaborn as sns

import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import patsy

import matplotlib.pyplot as plt

from sklearn.linear_model import RidgeCV
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, LassoCV, Ridge, RidgeCV
from sklearn.metrics import r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from makeURLs import URL_maker
from Data_getter import DataGetter
## Getting price information from the internet WOW!!!!###

cities=['SFO','AUS','ATL','BOI','BOS','ORD','DEN','DTW','FAI','JFK','SAN']

full_url_list=URL_maker(cities)

def Getting_Flight_Info(URL):
    driver = webdriver.Chrome('/Users/robjohns/Documents/Metis/Project2/chromedriver')
    driver.get(URL)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    driver.quit()
    data=DataGetter(URL,soup)
    return data
#print(len(soup.find_all('div', attrs={'class': 'gws-flights-results__itinerary-duration'})))



for URL in full_url_list[0:]:
    data=Getting_Flight_Info(URL)
    data=pd.DataFrame(data)

    Locations = re.search('#flt=(.+?);b:1', URL).group(1)
    Spots=Locations.split('.')
    Departure=Spots[0]
    Arrival = Spots[1]
    Date= Spots[2]
    Date=Date.replace('-',"_")

    data.to_pickle(f'Picklefolder/{Departure}_{Arrival}_{Date}')
