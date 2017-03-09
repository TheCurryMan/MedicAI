from firebase import firebase
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import requests

gMapsAPI = "AIzaSyDBxoKIfmr4B2IVVupCeUlNPv9DyayIjN0"


def getNearestDoctor(number):

    geolocator = Nominatim()

    fb = firebase.FirebaseApplication("https://medicai-4e398.firebaseio.com/", None)
    user = fb.get('/Users', None)[number]

    location = geolocator.geocode(user["location"])
    curLatLong = [location.latitude, location.longitude]

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?location=" + ','.join([str(x) for x in curLatLong]) + "&type=doctor&key=" + gMapsAPI
    respjson = requests.get(url).json()

    doc = respjson["results"][0]
    docName = doc["name"]
    distance = vincenty(tuple(curLatLong),(float(doc["geometry"]["location"]["lat"]),float(doc["geometry"]["location"]["lng"]))).miles
    retstr = "Your nearest doctor is " + docName + ". He/She is " + str(round(distance,1)) + " miles away"

    return retstr
