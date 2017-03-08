from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from firebase import firebase

def getLocations(disease, currentPercent, number):

    #Initialize Nominatim
    geolocator = Nominatim()

    # Initialize Firebase Application and get user data
    fb = firebase.FirebaseApplication("https://medicai-4e398.firebaseio.com/", None)
    data = fb.get('/Diseases', None)
    current_user = fb.get('/Users', None)[number]

    total = 0

    for i in data:
        if i == disease:
            curLoc = geolocator.geocode(current_user["location"])
            curLatLong = (curLoc.latitude, curLoc.longitude)
            for location in data[i]:
                loc = geolocator.geocode(location)
                locLatLong = (loc.latitude, loc.longitude)

                if vincenty(curLatLong, locLatLong).miles <= 10:
                    total += 1

    return total


print(getLocations("Influenza", "80%", "+14252298079"))
