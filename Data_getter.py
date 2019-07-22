##this will take the soupy html file and pull out data values for all flight results from a search##
# looking for [Date,DepartureCity,ArrivalCity,DepartureTime,
#               ArrivalTime,FlightDuration,Price,PlaneType,Airline,FlightNumber]
import re
#'https://www.google.com/flights?hl=en#flt=SFO.AUS.2019-08-21;b:1;c:USD;e:1;s:0;a:-F9;sd:1;t:f;tt:o'
#each page has a different number of flights on it, so for this URL we need to make a list of lists
#that is the length = number of flights on the page#

# before using this code make sure to find the list that reporesents the html item
# on google flights that has a big text block with most info and make sure it still has
#'jstcache': "8836", this number changes sometimes.

def DataGetter(URL,soup):

    Locations = re.search('#flt=(.+?);b:1', URL).group(1)
    Spots=Locations.split('.')
    Departure=Spots[0]
    Arrival = Spots[1]
    Date= Spots[2]



    flights=len(soup.find_all('div', attrs={'class': 'gws-flights-results__itinerary-duration'}))
    #print('num of flights:',flights)
    BigList = [[] for _ in range(flights)]
    for flight in BigList:
        flight.append(URL)
        flight.append(Date)
        flight.append(Departure)
        flight.append(Arrival)

    # Append flight durations onto each element of the list
    i=-1
    for li in soup.find_all('div', attrs={'class': 'gws-flights-results__duration flt-subhead1Normal'}):
        i+=1
        chonk=li.get_text()
        try:
            ch=chonk.split('h')
            onk=chonk.split(' ')
            num2=onk[1]
            flight_duration=float(ch[0])+(float(num2[:-1])/60)
            flight_duration = round(flight_duration,2)
            BigList[i].append(flight_duration)
            #print ('flight_duration:',flight_duration)
        except:
            BigList[i].append('NaN')
            print('There was a scraping issue')



    #for li in soup.find_all('div', attrs={'class': 'gws-flights-results__price'}):
        #print(li)


    #here we add more flight info from the jstcache. . . beware this number seems to change from day to day
    i=-1
    for li in soup.find_all('jsl', attrs={'jstcache': "8836"}):
        i+=1
        text = li.get_text()

          #finding price
        try:
            found = re.search('From (.+?)Trip', text).group(1)
            dollar=found.replace(',','')
            found=float(dollar[1:-1])
        except AttributeError:
        # if the sentence structure i didnt expect show up
            found = 'NaN' # apply your error handling
        #print('cost:',found)
        BigList[i].append(found)
        #finding departure and arrival times
        try:
            found = re.search('Departure time: (.+?)M', text).group(1)
            found2 = re.search('Arrival time: (.+?)M', text).group(1)

            #departure=found.replace(',','')
            #found=float(dollar[1:-1])
        except AttributeError:
        # if the sentence structure i didnt expect show up
            found = 'NaN' # apply your error handling
        #print('Departure Time:',found)
        #print('Arrival Time:',found2)
        BigList[i].append(found)
        BigList[i].append(found2)


        #grab airline
        try:
            found = re.search('by (.+?).Depa', text).group(1)

            #departure=found.replace(',','')
            #found=float(dollar[1:-1])
        except AttributeError:
        # if the sentence structure i didnt expect show up
            found = 'NaN' # apply your error handling
        #print('Airline:',found)
        BigList[i].append(found)
    #print('')
        #grab PlaneType and flight number
    i=-1
    for li in soup.find_all('div', attrs={'class': 'gws-flights-results__other-leg-info'}):
            i+=1
            #print(li.get_text())
            st=li.get_text()
            #st=str(st.text())
            result = re.match("(?P<PlaneType>[A-Za-z]+.[A-Za-z]*[0-9]+)(?P<FlightNum>[A-Za-z]+\s[0-9]+)", st)
            if result:
                Planetype=result.group('PlaneType')
                Flightnumber=result.group('FlightNum')
                Flightnumber=Flightnumber.replace('\xa0','')
                #print('Flightnum:',Flightnumber)
                #print('Planetype:',Planetype)
                BigList[i].append(Flightnumber)
                BigList[i].append(Planetype)
                #print("")
            else:
                errormsg=('REGEXerror:',st)
                BigList[i].append(errormsg)
                BigList[i].append(errormsg)

    return BigList
