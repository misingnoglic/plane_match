__author__ = 'jacob'
import requests

class Hotel():
	def __init__(self,name,address):
		self.name=name
		self.address=address
		#address contains values for the keys line1, city, region (the state in the US), postal_code, and country

def airportLocationUrl(airport):
	return "http://api.sandbox.amadeus.com/v1.2/location/" + airport + "/?apikey=BN5GcXUGdrdDhdFiGOISx6Z09mmaDb7Q"

def getAirportInfo(airport):
	return requests.request('GET',airportLocationUrl(airport)).json()

def extractLatAndLong(airportinfo):
	airports = airportinfo['airports']
	location = airports[0]['location']
	return location

#search radius is kilometers
def getHotelUrl(location, radius):
	checkin = "2015-03-01"#temporary date for demo purposes
	checkout = "2015-03-04"#temporary date for demo purposes
	latitude = location['latitude']
	longitude = location['longitude']
	return "http://api.sandbox.amadeus.com/v1.2/hotels/search-circle?latitude=" + str(latitude) + "&longitude=" + str(longitude) + "&radius=" + str(radius) + "&check_in="+ checkin + "&check_out=" + checkout + "&apikey=BN5GcXUGdrdDhdFiGOISx6Z09mmaDb7Q"

def getHotelInfo(airport, radius):
	location = extractLatAndLong(getAirportInfo(airport))
	url = getHotelUrl(location,radius)
	return requests.request('GET',url).json()

def getHotelList(hotelInfo):
	hotelList = []
	for hotel in hotelInfo['results']:
		h = Hotel(hotel['property_name'],hotel['address'])
		hotelList.append(h)
	return hotelList

def hotelsNearAirport(airport,radius):
	info = getHotelInfo(airport,radius)
	return getHotelList(info)