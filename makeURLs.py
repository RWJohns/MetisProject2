##This makes the URL lists##

#links look like this for one ways,nonstop, with overhead bags allowed, and frontier airlines excluded##
#'https://www.google.com/flights?hl=en#flt=SFO.AUS.2019-08-21;b:1;c:USD;e:1;s:0;a:-F9;sd:1;t:f;tt:o'
def URL_maker(cities):
#This makes all the dates from july 22nd to the end of the year, will update from date time later if i have time
    dates=['2019-07-22']
    for days in range(23,32):
        date = '2019-07-' + str(days)
        dates.append(date)
    for days in range(1,32):
        if days>=10:
            date = '2019-08-' + str(days)
            dates.append(date)
        else:
            date = '2019-08-0' + str(days)
            dates.append(date)
    for days in range(1,31):
        if days>=10:
            date = '2019-09-' + str(days)
            dates.append(date)
        else:
            date = '2019-09-0' + str(days)
            dates.append(date)
    for days in range(1,32):
        if days>=10:
            date = '2019-10-' + str(days)
            dates.append(date)
        else:
            date = '2019-10-0' + str(days)
            dates.append(date)

    for days in range(1,31):
        if days>=10:
            date = '2019-11-' + str(days)
            dates.append(date)
        else:
            date = '2019-11-0' + str(days)
            dates.append(date)

    for days in range(1,32):
        if days>=10:
            date = '2019-12-' + str(days)
            dates.append(date)
        else:
            date = '2019-12-0' + str(days)
            dates.append(date)

    ## This makes lists of URLS to use generating data##
    super_short_test_list=[]
    super_short_test_list_dates=[]
    for city in cities[::6]:
        URLc='https://www.google.com/flights?hl=en#flt=SEA.'+city+'.'

        for date in dates[::43]:
            URL=URLc+date+';b:1;c:USD;e:1;s:0;a:-F9;sd:1;t:f;tt:o'
            super_short_test_list.append(URL)
            super_short_test_list_dates.append(date)

#    print('super short test set has this many values:'+str(len(super_short_test_list)))

    test_urls=[]
    for city in cities[::5]:
        URLc='https://www.google.com/flights?hl=en#flt=SEA.'+city+'.'

        for date in dates[::29]:
            URL=URLc+date+';b:1;c:USD;e:1;s:0;a:-F9;sd:1;t:f;tt:o'
            test_urls.append(URL)
    print('test set has this many values:'+str(len(test_urls)))

    full_cities_lessdates_urls=[]
    for city in cities:
        URLc='https://www.google.com/flights?hl=en#flt=SEA.'+city+'.'

        for date in dates[::15]:
            URL=URLc+date+';b:1;c:USD;e:1;s:0;a:-F9;sd:1;t:f;tt:o'
            full_cities_lessdates_urls.append(URL)
#    print('full city set has this many values:'+str(len(full_cities_lessdates_urls)))

    full_dates_lesscities_urls=[]
    for city in cities[::3]:
        URLc='https://www.google.com/flights?hl=en#flt=SEA.'+city+'.'

        for date in dates:
            URL=URLc+date+';b:1;c:USD;e:1;s:0;a:-F9;sd:1;t:f;tt:o'
            full_dates_lesscities_urls.append(URL)
#    print('full date set has this many values:'+str(len(full_dates_lesscities_urls)))

    full_url_list=[]
    for city in cities:
        URLc='https://www.google.com/flights?hl=en#flt=SEA.'+city+'.'

        for date in dates:
            URL=URLc+date+';b:1;c:USD;e:1;s:0;a:-F9;sd:1;t:f;tt:o'
            full_url_list.append(URL)
#    print('full set has this many values:'+str(len(full_url_list)))
    return full_url_list

    come_home_URLS=[]
    for city in cities:
        URLc='https://www.google.com/flights?hl=en#flt='+city+'.'+'SEA.'
        for date in dates:
            URL=URLc+date+';b:1;c:USD;e:1;s:0;a:-F9;sd:1;t:f;tt:o'
            come_home_URLS.append(URL)
    #print('come home set has this many values:'+str(len(come_home_URLS)))
