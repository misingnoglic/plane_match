#@author = Jacob Regenstein
import requests
from secrets import amadeus_key

class FlightObject():
    def __init__(self,departureTime,arrivalTime,flightNumber,aircraft):
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
        self.flightNumber = flightNumber
        self.aircraft = aircraft
    def __str__(self):
        short_time = self.departureTime.split("T")[1]
        return str("Flight number "+str(self.flightNumber)+" departing at "+str(short_time))

#date should be formatted yyyy-MM-dd,
#origin and destination should be 3 digit airport codes 
#the airline should be a 2 digit IATA code
def getUrl(date, origin, destination, airline):
	return "http://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?origin=" + origin + "&destination=" + destination + "&departure_date=" + date + "&include_airlines=" + airline + "&direct=true&apikey="+amadeus_key

#print getUrl(testDate, testOrigin, testDestination, testAirline)
def getFlights(date,origin,destination,airline):
	planelist = requests.request('GET', getUrl(date,origin,destination,airline))
	planelist = planelist.json()
	list_of_departures = []
	if planelist.get('results', None)!=None:
		for results in planelist['results']:
			for itineraries in results[u'itineraries']:
				d = itineraries

				firstFlight = d['outbound'][u'flights'][0]
				lastFlight = d['outbound'][u'flights'][-1]
				depart = firstFlight['departs_at']
				arrival = lastFlight['arrives_at']
				number =  firstFlight['flight_number']
				aircraft = firstFlight['aircraft']

				a = FlightObject(depart,arrival,number,aircraft)
				list_of_departures.append(a)
	return list_of_departures



#for flight in getFlights(testDate,testOrigin,testDestination,testAirline):
#	print flight