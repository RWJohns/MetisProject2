# Predicting timelines for airline price changes
## Project Proposal, Metis Project #2

## Rob Johns

### Scope:
Travel is a huge part of our culture. It impacts keeping friends and families staying connected in an increasingly mobile and globalized culture, how businesses operate, and where and how people vacation to expand their experiences. Everyone knows that booking in advance can save you a lot of money, but how much in advance really makes a significant impact? In this project I will seek to investigate trends in airline pricing and use regression models to try to provide a tool for generally predicting the behavior of these prices over time.

### Methodology:
1. Scrape what price options are for flights for several given routes looking further into the future to build a time series by running queries for a trip of fixed length and non stop but with different arrive and leave dates
2. make a table that has date,airline,price,time of flights, length of trip. . .
3. calculate time in future to plot time from now versus flight
4. Look for other trends in flight pricing and see if other models may
5. Set up visualizations that could help a user demystify how soon is soon enough


### Data Sources:
* Google Flights
* Expedia
* alaska airlines website
* others?

### Target:
* MVP:
        a.Predict how far in advance flights need to be booked before the prices begin to rise
        b.Quantify how large of an impact waiting really has on total price for those who choose to wait



### Features:
* Date
    - Day of week
    - Month/time of year
    - Year
    - Holidays/events
    - Time in the future from now
    - Time of day of flight
* Flight path
    - all will originate in Seattle
    - will maybe distinguish one way and RT?
* Price



### Things to consider:
* There are likely weekly trends in price or random blackouts or issues, especially in flights that are very nearby to now so it will introduce a lot of noise in the data
* Holidays could change prices.
